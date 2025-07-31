

import pandas as pd
import os

# -----------------------------------------------------------
def read_csv(name):
    """This function reads a dataset"""
    return pd.read_csv("data/"+ name + ".csv")

# -----------------------------------------------------------
def split_location_date(dataset):
    """
    Splits 'Review Date' into 'Location' and 'Date', drops the old column,
    and rearranges columns.
    """
    split_column = dataset["Review Date"].str.split()
    dataset[["Location", "Date"]] = split_column.apply(lambda x: pd.Series([" ".join(x[:-3]), " ".join(x[-3:])]))
    dataset.drop(columns=["Review Date"], inplace=True)
    dataset = dataset[['Location', 'Date', 'Review Text']]
    return dataset

# -----------------------------------------------------------
def remove_duplicates(dataset):
    """Removes duplicate reviews based on 'Review Text'"""
    return dataset.drop_duplicates(subset='Review Text')

# -----------------------------------------------------------
def convert_dates(dataset):
    """
    Converts 'Date' column to pandas datetime format,
    adds month/year, sorts chronologically, and cleans up.
    """
    dataset["Date"] = pd.to_datetime(dataset["Date"])
    dataset["month"] = dataset["Date"].dt.month
    dataset["year"] = dataset["Date"].dt.year
    dataset = dataset.sort_values(by=["year", "month"]).drop(columns=["month", "year"])
    return dataset

# -----------------------------------------------------------
def cleaner(file_name, output_file="Updated_cleaned_dataset.csv"):
    # Read input CSV
    reviews = read_csv(file_name)

    # Clean and process the data
    reviews = split_location_date(reviews)
    reviews = remove_duplicates(reviews)
    reviews = convert_dates(reviews)

    # Ensure the 'data' directory exists
    data_dir = "data"
    os.makedirs(data_dir, exist_ok=True)

    # Construct full output path
    output_path = os.path.join(data_dir, output_file)

    # Save the updated dataset
    reviews.to_csv(output_path, index=False, encoding='utf-8-sig')

    return reviews





