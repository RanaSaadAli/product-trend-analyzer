
# 

#=============================================================

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import time
from bs4 import BeautifulSoup
import pandas as pd

# -----------------------------------------------------------
def extract_file_name(link):
    return link.split(".com/")[1].split("/dp/")[0]

# -----------------------------------------------------------
def save_file(all_dates, all_reviews, file_name):
    data_dir = 'data'
    os.makedirs(data_dir, exist_ok=True)

    file_path = os.path.join(data_dir, file_name + ".csv")

    if all_reviews:
        df = pd.DataFrame({
            "Review Date": all_dates,
            "Review Text": all_reviews
        })
        df.to_csv(file_path, index=False, encoding='utf-8-sig')
    else:
        print("❌ No reviews found.")
    return file_path

# -----------------------------------------------------------
def get_reviews_html(product_url, email, password, max_pages):
    login_url = "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=3600&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fproduct-reviews%2FB0B5FDNQSG%2Fref%3Dcm_cr_dp_d_show_all_btm%3Fie%3DUTF8%26reviewerType%3Dall_reviews&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"

    # 👇 Use local chromedriver from 'driver/' folder
    driver_path = os.path.join("driver", "chromedriver")  # Use .exe on Windows
    service = Service(driver_path)

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)

    all_reviews = []
    all_dates = []

    try:
        driver.get(login_url)

        email_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "ap_email"))
        )
        email_input.send_keys(email)
        driver.find_element(By.ID, "continue").click()

        password_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "ap_password"))
        )
        password_input.send_keys(password)
        driver.find_element(By.ID, "signInSubmit").click()

        time.sleep(5)

        driver.get(product_url)
        time.sleep(4)

        try:
            see_all_reviews = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//a[contains(@data-hook,"see-all-reviews-link-foot")]'))
            )
            see_all_reviews.click()
            time.sleep(4)
        except:
            print("⚠️ 'See all reviews' link not found. Staying on product page.")

        for page_number in range(1, max_pages + 1):
            time.sleep(4)
            soup = BeautifulSoup(driver.page_source, "html.parser")

            reviews = soup.find_all("span", {"data-hook": "review-body"})
            dates = soup.find_all("span", {"data-hook": "review-date"})

            for review, date in zip(reviews, dates):
                all_reviews.append(review.get_text(strip=True))
                all_dates.append(date.get_text(strip=True))

            print(f"✅ Scraped page {page_number}")

            if page_number != max_pages:
                try:
                    next_button = driver.find_element(By.XPATH, '//li[@class="a-last"]/a')
                    driver.execute_script("arguments[0].click();", next_button)
                except:
                    print("⛔ 'Next' button not found. Ending early.")
                    break

    finally:
        driver.quit()

    return all_dates, all_reviews



