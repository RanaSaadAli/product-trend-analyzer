#!/usr/bin/env python
# coding: utf-8

# In[1]:


from module.BOM_collection import extract_file_name,save_file,get_reviews_html
from module.BOM_Cleaner import cleaner,read_csv
from module.BOM_sentiment_analyzer import sentiment_analyzer
from module.BOM_hype_analysis import hype_analysis
from module.BOM_visualize import visualizations


# In[2]:


def BOM():
    # ======================
    # === USER INPUTS ====
    # ======================
    print("🟡 ENTER AMAZON LOGIN DETAILS AND PRODUCT INFO 🟡")
    #login_url = input("🔑 Enter the Amazon login page URL: ").strip()
    email = input("📧 Enter your Amazon email: ").strip()
    password = input("🔒 Enter your Amazon password: ").strip()
    product_url = input("🛒 Enter the Amazon product URL: ").strip()
    max_pages = int(input("📄 Enter the number of review pages to scrape: ").strip())
    
    # ======================
    # === scrape data from website ====
    # ======================
    all_dates, all_reviews = get_reviews_html(product_url, email, password, max_pages)

    # ======================
    # === Extract product name ====
    # ======================
    file_name = extract_file_name(product_url)

    # ======================
    # === save scraped data into a csv file ====
    # ======================
    save_file(all_dates, all_reviews, file_name)

    # ======================
    # === Clean data ====
    # ======================
    cleaned_dataset = cleaner(file_name)

    # ======================
    # === perform sentiment analysis ====
    # ======================
    sentimentized_dataset = sentiment_analyzer(cleaned_dataset)

    # ======================
    # === perform hype analysis ====
    # ======================
    compared_result, subjective_per, avg_sub_rev, total_of_obv_rev, total_of_sub_rev = hype_analysis(sentimentized_dataset)
    

    # ======================
    # === show visual analsis ====
    # ======================
    visualizations(sentimentized_dataset)
    
    # ======================
    # === show performed analysis ====
    # ======================
    return compared_result, subjective_per, avg_sub_rev, total_of_obv_rev, total_of_sub_rev


# In[3]:


BOM()


# In[ ]:


url = "https://www.amazon.com/Apple-iPhone-13-256GB-Green/dp/B0B5FDNQSG/ref=sr_1_1?crid=I3MIDTFTH42M&dib=eyJ2IjoiMSJ9.0PtuXvPMvsUstRNwZ_q5lzgJM4kMUCCV13s0iF5Cp2tKyaAYxsuNbDBd4U8gkJzTvMZ73e4wOCTEyACSMHnMtfLxhMmRVX9DOkNz68kfSz4LZZNsfM4QPY2fNPbYupECgzW-cDL-MlKPl_18x12i9wTWZLIsUJNXXWrZBdS0UQCri5vkXpV7CBIB1Yrt8rIXFykmr6a-SGc0DivR4KSf7bh44gE-ZuXIb3M-f2wWdsU.eO_8kd4PiaSzGmp_NYw2ouXk80YbXD18OBLpyFuhaNc&dib_tag=se&keywords=iphone%2B13&qid=1750765144&sprefix=iphone%2B1%2Caps%2C422&sr=8-1&th=1a"
pro_url = extract_file_name(url)


# In[5]:




