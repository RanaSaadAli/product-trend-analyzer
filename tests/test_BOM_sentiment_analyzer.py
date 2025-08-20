from trend_analyzer import BOM_sentiment_analyzer
import pytest
import pandas as pd

#test for demojized
def test_demojized():
    #text for testing the function
    text = "I love pizza 🍕 but running 🏃 is hard 😓"

    #expected result of the test
    expected = "I love pizza :pizza: but running :person_running: is hard :downcast_face_with_sweat:"

    result = BOM_sentiment_analyzer.demojized(text)

    assert result == expected

#test for get_sentiment function
def test_get_sentiment():
    result = BOM_sentiment_analyzer.get_sentiment("I love this product! 😍")

    #asseritons
    assert result[0] > 0
    assert 0 <= result[1] <= 1

#using parameterize testing for next function
@pytest.mark.parametrize(
    "score, expected",
    [
        (0.5, "Positive"),
        (-0.5, "Negative"),
        (0.0, "Neutral")
    ]
)

#testing classify_sentiment function
def test_classify_sentiment(score,expected):
    assert BOM_sentiment_analyzer.classify_sentiment(score) == expected

#testing sentiment_analyzer function
def test_sentiment_analyzer(mocker):
    #fake dataframe
    fake_df = pd.DataFrame({
        "Location":["Reviewed in the United States on","Reviewed in the United States on"],
        "Date":["6/20/2025","6/27/2025"],
        "Review Text":["It works good, good value for money, thank you!","The battery health is at 75 percent only problem to be honest"],
    })

    #expected outptut
    expected = pd.DataFrame({
        "Location":["Reviewed in the United States on","Reviewed in the United States on"],
        "Date":["6/20/2025","6/27/2025"],
        "Review Text":["It works good, good value for money, thank you!","The battery health is at 75 percent only problem to be honest"],
        "Polarity":[0.7875, 0.3],
        "Subjectivity":[0.6, 0.95],
        "Label":["Positive","Positive"]
    })

    #patching to_csv method of the function
    mock_to_csv = mocker.patch("pandas.DataFrame.to_csv")

    #testing function
    result = BOM_sentiment_analyzer.sentiment_analyzer(fake_df.copy())

    #checking if the mock_to_csv runned once 
    mock_to_csv.assert_called_once()

    #assertion
    pd.testing.assert_frame_equal(result, expected)
