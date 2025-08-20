from trend_analyzer import BOM_hype_analysis
import pytest
import pandas as pd

#test for polarity_avg function
def test_polarity_avg():
    #fake dataset to test the function
    fake_df = pd.DataFrame({
        "Polarity":[0.30254065,0.181423611,0.245959596]
    })

    #expected output of the dataset
    expected = 0.24

    # running the test 
    result = BOM_hype_analysis.polarity_avg(fake_df.copy())

    #assertion
    assert result == expected

#parametrize testing for threshold_comparison
@pytest.mark.parametrize(
    "avg, result", 
    [
        (0.6, "This product have higher positive reviews"),
        (-0.6,"This product have higher negative reviews"),
        (0.3, "People have slighlty positive reviews"),
        (-0.1,"People have slightly negative reviews"),
        (0,"People reviews are neutral about this product")
    ]
)

def test_threshold_comparison(avg,result):
    assert BOM_hype_analysis.threshold_comparison(avg) == result

#testing subjective_percentage function
def test_subjective_percentage():
    #creating lists required to pass in the function
    list1 = [0.56680217, 0.50782828, 0.54902597, 0.51111111, 0.63412698, 0.60502645]
    list2 = [0.56680217, 0.45777778, 0.50782828, 0.54902597, 0.2995098,  0.51111111, 0.63412698, 0.60502645]

    #running test
    result = BOM_hype_analysis.subjective_percentage(list1, list2)

    assert result == "Percentage of opinion based reviews is: 75.0"

#testing subjective_avg function
def test_subjective_avg():
    #list to pass in function as a parameter
    list1 = [0.56680217, 0.50782828, 0.54902597, 0.51111111, 0.63412698, 0.60502645]

    #exptected result of the list
    expected = "Average of opinion based reviews is: 0.56"

    #running test
    result = BOM_hype_analysis.subjective_avg(list1)

    #assertion
    assert result == expected

#testing total_sub_rev function
def test_total_sub_rev():
    #dummy list for testing the function
    list1 = [0.56680217, 0.50782828, 0.54902597, 0.51111111, 0.63412698, 0.60502645]

    #running test
    result = BOM_hype_analysis.total_sub_rev(list1)

    #assertion
    assert result == "Total opinion based reviews are: 6"

#testing  total_ob_rev function
def test_total_ob_rev():
    #dummy list to test function
    list1 = [0.45777778, 0.2995098 ]

    #running test 
    result = BOM_hype_analysis.total_ob_rev(list1)

    #assertion
    assert result == "Total factual based reviews are: 2"


#testing hype_analysis function
def test_hype_analysis():
    #dummy dataset
    fake_df = pd.DataFrame({
    "Location":["Reviewed in the United States on", "Reviewed in the United States on"],
    "Date":["8/23/2024","3/31/2025"],
    "Review Text":["Good", "Very Good"],
    "Polarity":[0.30254065, 0.181423611],
    "Subjectivity":[0.566802168, 0.457777778],
    "Label":["Positive", "Positive"]
    })

    #dummy dataset's result
    expected = ('People have slighlty positive reviews', 'Percentage of opinion based reviews is: 50.0', 'Average of opinion based reviews is: 0.57', 'Total factual based reviews are: 1', 'Total opinion based reviews are: 1')

    #running test
    result = BOM_hype_analysis.hype_analysis(fake_df.copy())

    #assertions
    assert result == expected