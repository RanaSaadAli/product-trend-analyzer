import pandas as pd
from trend_analyzer import BOM_Cleaner 

#writing function for my read_csv function from BOM_Cleaner
def test_read_csv(mocker):
    #create a fake Dataframe
    fake_df = pd.DataFrame({"col1":[1,2], "col2":["a","b"]})

    #patch pd.read to return fake dataframe
    mocker.patch("trend_analyzer.BOM_Cleaner.pd.read_csv", return_value=fake_df)
    result = BOM_Cleaner.read_csv("dummy")

    pd.testing.assert_frame_equal(result, fake_df)

#writing test function for split_location_date
def test_split_location_date():
    fake_df = pd.DataFrame({
         "Review Date": ["Reviewed in the United Arab Emirates on 11 May 2025"],
         "Review Text": ["Very satisfied!"]
    })

    exptected_df = pd.DataFrame({
        "Location":["Reviewed in the United Arab Emirates on"],
        "Date":["11 May 2025"],
        "Review Text":["Very satisfied!"]
    })

    result = BOM_Cleaner.split_location_date(fake_df.copy())

    pd.testing.assert_frame_equal(result, exptected_df)

#test function for remove_duplicates
def test_remove_duplicates():
    #Dummy dataframe to pass in function for test
    fake_df = pd.DataFrame({
        "Review Text":["Very good quality","Very good quality"]
    })

    #dummy dataframe to check the test results
    expected_df = pd.DataFrame({
        "Review Text":["Very good quality"],
    })

    result = BOM_Cleaner.remove_duplicates(fake_df.copy())

    pd.testing.assert_frame_equal(result, expected_df)

# test function for convert_dates
def test_convert_dates():
    #fake_df to pass in function for test
    fake_df = pd.DataFrame({
        "Date":["11 May 2025","25 May 2025","14 May 2025","26 June 2024","17 August 2024"]
    })

    #expected dataset to check results
    expected_df = pd.DataFrame({
    "Date": pd.to_datetime([
        "26 June 2024",
        "17 August 2024",
        "11 May 2025",
        "25 May 2025",
        "14 May 2025",
    ])
})
    
    #calling function to test
    result = BOM_Cleaner.convert_dates(fake_df.copy()).reset_index(drop=True)

    #assertion
    pd.testing.assert_frame_equal(result, expected_df)

# test for cleaner function of BOM_Cleaner module.
def test_cleaner(mocker):
    #fake dataset for testing the function
    fake_df = pd.DataFrame({
        "Review Date":["Reviewed in the United Arab Emirates on 11 May 2025","Reviewed in the United Arab Emirates on 25 May 2025","Reviewed in the United Arab Emirates on 11 May 2025",],
        "Review Text":["very good quality", "thumbs up", "very good quality"]
    })

    #expected dataframe to compare results
    expected_df = pd.DataFrame({
    "Location": [
        "Reviewed in the United Arab Emirates on",
        "Reviewed in the United Arab Emirates on"
    ],
    "Date": [
        pd.Timestamp("2025-05-11"),
        pd.Timestamp("2025-05-25")
    ],
    "Review Text": [
        "very good quality",
        "thumbs up"
    ]
    })

    #mocking the to_csv function
    mock_to_csv = mocker.patch("pandas.DataFrame.to_csv")

    #mocking read_csv method
    mocker.patch("trend_analyzer.BOM_Cleaner.read_csv", return_value=fake_df)

    #testing the function
    result = BOM_Cleaner.cleaner("dummy")

    #checking if the patch runs atleat for once
    mock_to_csv.assert_called_once()

    #assertion
    pd.testing.assert_frame_equal(result, expected_df)
