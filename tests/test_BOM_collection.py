import pandas
import os
import pytest
from trend_analyzer.BOM_collection import extract_file_name, save_file
import trend_analyzer.BOM_collection as bom

#test function for extract_file_name function from BOM_collection
def test_extract_file():
    link = "https://www.amazon.com/SAMSUNG-Unlocked-Smartphone-Charging-Expandable/dp/B0DLHLRDBY/ref=sr_1_2?crid=2I4QQL2P4R5W7&dib=eyJ2IjoiMSJ9.9mch-OhRrotziNS58gzOb4su0D5pyEH-5ypAc01hP0vVljh_U2AMQWEDRXTRZ2QBe9gIPj4v7YrJRaPGl3D4efw1_q-4X_p7GVCUL3aMGjlHmJIpxVayugRc_aTetvbPF6ilP8SphRjIcEwss8Km3YDrMGk3116Z8heRyHS05WOdyvl5UAGooOp3t9P9yPJ_eDWSKKRddLIVxod__AWouD5hM_R2j95G_mBY1BiVPuc.AfKoBpudd-aXpQRt99l12pBMMgO6nH6PrC7vuJGWCGM&dib_tag=se&keywords=samsung&qid=1754985201&sprefix=samsu%2Caps%2C1497&sr=8-2"
    expected = "SAMSUNG-Unlocked-Smartphone-Charging-Expandable"
    assert extract_file_name(link) == expected

#test function for save_file function from BOM_collection
def test_save_file(mocker):
    #create fake data
    fake_dates = ["Reviewed in the United States on 3/9/2025"]
    fake_reviews = ["Amazing product!"]
    fake_name = "test_function"

    #mock the method that is writing to the disk
    mock_to_csv = mocker.patch("pandas.DataFrame.to_csv")

    #call the real function
    result_path = save_file(fake_dates,fake_reviews,fake_name)

    #assertions and check if the mocker called once.
    #check if the mocked method is called exactly once.
    mock_to_csv.assert_called_once()

    #check if returned path is correct
    expected_path = os.path.join("data",fake_name +".csv")
    assert result_path == expected_path

    #check to_csv was called with the expected path
    mock_to_csv.assert_called_once_with(expected_path, index=False, encoding='utf-8-sig')

#test function for get_reviews_html function from BOM_collection
def test_get_reviews(mocker):
    #create fake dates and reviews for mock function to scrape
    fake_dates = ["Reviewed in the United States on August 4, 2025","Reviewed in the United States on July 29, 2025"]
    fake_reviews = ["Amazing product, would buy again. was a tad pricey but much worth it. i got this beautiful blue color, and thesr camerad really bring out a vibrant array of design. when i opened the box, there were no visible scuffs or marks and any scratches. on the interior, batter was 100%, and storage was exactly what i paid for. easy to use, comes w a sim card ejector and original packaging. seems very durable, and not heavy at all, light weight.", "I bought this refurbished pink iPhone 13 (256 GB) and was genuinely impressed. No scratches or dents, it looks brand new. Battery arrived at 97%, and performance has been flawless. It s a great way to save money without compromising quality. Highly recommend!"]
    
    #create mock of the real function
    mock_get_reviews_html = mocker.patch("trend_analyzer.BOM_collection.get_reviews_html", return_value=(fake_dates,fake_reviews))

    dates, reviews = bom.get_reviews_html("https://www.amazon.com/Apple-iPhone-13-256GB-Green/dp/B0B5FDNQSG/ref=sr_1_1?crid=I3MIDTFTH42M&dib=eyJ2IjoiMSJ9.0PtuXvPMvsUstRNwZ_q5lzgJM4kMUCCV13s0iF5Cp2tKyaAYxsuNbDBd4U8gkJzTvMZ73e4wOCTEyACSMHnMtfLxhMmRVX9DOkNz68kfSz4LZZNsfM4QPY2fNPbYupECgzW-cDL-MlKPl_18x12i9wTWZLIsUJNXXWrZBdS0UQCri5vkXpV7CBIB1Yrt8rIXFykmr6a-SGc0DivR4KSf7bh44gE-ZuXIb3M-f2wWdsU.eO_8kd4PiaSzGmp_NYw2ouXk80YbXD18OBLpyFuhaNc&dib_tag=se&keywords=iphone%2B13&qid=1750765144&sprefix=iphone%2B1%2Caps%2C422&sr=8-1&th=1", "testemail@gmail.com", "password",1)

    #assertions 
    assert dates == fake_dates
    assert fake_reviews == fake_reviews
