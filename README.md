# 📦 Product Trend Analyzer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> *A modular pipeline to scrape, clean, analyze, and visualize Amazon product reviews using Python, pandas, numpy, matplotlib, selenium, Beautifulsoup4 and textblob*

## 🚀 Quick Start

Follow these steps to get the project up and running on your local machine.

### 1. Clone the Repository


```bash
git clone https://github.com/RanaSaadAli/product-trend-analyzer.git
cd your-repo-name
```

**Create and activate virtual enviroment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**Install dependencies**

```bash
pip install -r requirements.txt
```

**Run the project**

```bash
python main.py
```

## Sample Output

This project generates graphs based on the dataset provided. Here's a preview:

## 🗂️ Table of Contents

- [🚀 Quick Start](#-Quick-Start)
- [📊 Sample Output](#Sample-Output)
- [📖 About the Project](#-About-the-Project)
  - [🤔 Why I built this?](#-Why-I-built-this)
  - [📚 Learning Goal](#-Learning-Goal)
  - [🚀 What this project means to me](#-What-this-project-means-to-me)
  - [🧩 Challenges & How I Solved Them](#-Challenges-&-How-I-Solved-Them)
    - [🚀 What I Learned](#-What-I-Learned)
- [⚙️ Features](#️-Features)
- [🛠️ Prerequisites](#️-Prerequisites)
- [🧪 Getting Started](#Getting-started)
- [📁 Folder Structure](#-Folder-Structure)
- [🧪 Testing Instructions](#-Testing-Instructions)
- [🛠️ Developer Setup](#️-Developer-Setup)
- [🚀 Future Releases](#Future-releases)
- [🤝 Contributions](#Contributions)
- [📬 Contact](#Contact)


## 📖 About the Project

Product trend analyzer is a data-driven project that analyzes the hype vs reality of Amazon products based on customer reviews. Often, when a new product launches, it generates a lot of excitement — early reviews are mostly positive due to novelty. However, as more users start using it, the actual feedback may turn negative, revealing real-world flaws and usability issues.

This mismatch can mislead Amazon sellers who rely on early reviews when deciding to list a product — only to find later that the product doesn’t perform well in sales due to declining customer sentiment.

To solve this problem, product trend analyzer offers a complete pipeline:

📥 Scraping Reviews: Users enter an Amazon product link and their login credentials (for access to all reviews), and the tool scrapes reviews from the number of pages they choose.

- 📄 **Data Export:** The reviews are saved in a CSV file.

- 🧹 **Data Cleaning:** Using Pandas, the data is cleaned and prepped for analysis.

- 🧠 **Sentiment Analysis:** Each review is scored using TextBlob to understand customer sentiment.

- 📊 **Hype Analysis:** With NumPy, the project compares early and late review trends to detect whether a product was truly worth the hype.
 
- 📈 **Visualization:** Finally, results are visualized using Matplotlib, helping sellers make smarter product decisions backed by data.

Whether you're a data science enthusiast or an Amazon seller, this project showcases the power of Python, web scraping, and sentiment analysis to uncover valuable insights from real customer voices.

## 🤔 Why I built this?

The idea for Product trend analyzer actually sparked from a mix of curiosity and learning. I had previously learned how Amazon sellers often avoid trending products and instead look for less competitive or under-the-radar items to add to their stores. During that exploration, I realized how misleading early product reviews can be — creating a temporary buzz that fades once real user experiences start coming in.

Later, while learning data science, I came across the concept of analyzing customer sentiment through reviews — and that’s when everything clicked. I realized I could turn this idea into a real project to apply the skills I’ve been learning like web scraping, data cleaning, sentiment analysis, and data visualization.

More than just building a tool, this project was a personal challenge. I wanted to boost my confidence, prove to myself that I can turn raw data into real insights, and build something practical that connects technology with real-world problems.

This is one step in my journey to becoming a data scientist — and I hope others find it inspiring or useful too.

### 📚 Learning Goal

I wanted to apply the skills I’ve been learning on my data science journey — from web scraping and data cleaning to sentiment analysis and data visualization. But once I started, I gained much more than technical practice.

This project taught me how to plan, organize, and structure a project from scratch. Most importantly, I learned how to learn — how to navigate new challenges, break down problems, and stay consistent.

I’ve also documented my learnings along the way. If you’re someone eager to learn the same tools and mindset, check out the docs folder — you might find something valuable there.

### 🚀 What this project means to me

This project isn’t just a portfolio piece — it’s a milestone in my journey to becoming a confident and capable data scientist. Through Product trend analyzer I proved to myself that I can take an idea, break it down, and turn it into something real with code.

My bigger ambition is to keep solving real-world problems using data — and build tools that don’t just run, but make sense. This was one small project, but for me, it marks the beginning of thinking like a builder, not just a learner

### 🧩 Challenges & How I Solved Them

**From Confusion to Clarity: Turning Review Data Into Business Insights**
When I started working on Product trend analyzer, I had a basic idea of how Amazon sellers operate — I knew they often look for low-competition products with decent early feedback. But when it came to analyzing real customer reviews using NumPy, I hit a wall.

I wasn’t just trying to crunch numbers — I needed to answer a real question: What exactly do e-commerce sellers look for in reviews before investing in a product?

At first, I had no clear direction. That’s when I decided to pause the coding and dig deeper into the business side. I researched how online sellers interpret reviews — how they look for recurring customer complaints, trends in satisfaction, and signals of long-term demand.

With that understanding, everything clicked.

I went back to my data with new eyes. I redefined my analysis goals, used NumPy to uncover patterns, and turned raw text data into actionable insights. The challenge helped me shift my thinking from "how do I analyze this data?" to "how can this analysis solve a real business problem?"

#### 🚀 What I Learned
**Start with clarity:** Don’t jump into code without understanding the "why."

**Think like a problem-solver:** Align your technical tools with real-world decisions.

**Research is part of development:** Sometimes the best debugging is done in your browser, not your IDE.

This wasn’t just a technical challenge — it was a mindset shift. And if you've ever worked on product analytics or struggled to connect code with business needs, I’d love to hear how you tackled it. Let’s grow together!

## ⚙️ Features

- 🔐 Logs into Amazon using Selenium to access complete review data.

- 🧾 Scrapes review text and dates from multiple pages per user input.

- 📁 Saves scraped data as a structured CSV file for analysis.

- 🧹 Cleans the dataset by splitting location/date, removing duplicates, and sorting.

- 🧠 Performs sentiment analysis using TextBlob for polarity and subjectivity.

- 🏷️ Labels reviews as Positive, Negative, or Neutral.

- 📊 Calculates hype score by analyzing average sentiment with NumPy.

- 📈 Distinguishes between subjective (opinion-based) and objective (factual) reviews.

- 📊 Summarizes insights like total reviews, polarity trends, and subjectivity percentages.

- 📂 Stores all output neatly in the data/ folder for easy access.

## 🛠️ Prerequisites

Before running Product trend analyzer, make sure you have the following installed:

**🔧 Python & Libraries**

Python 3.13 or higher

Google Chrome (latest version)

## Getting started

### 1️⃣ Clone the Repository


```bash
git clone https://github.com/RanaSaadAli/product-trend-analyzer.git
cd product-trend-analyzer
```

### 2️⃣ Install the Required Libraries

Make sure you have Python 3.13+ installed.

Then install all dependencies using pip:

```bash
pip install -r requirements.txt
```

### 3️⃣ SetUp ChromeDriver

ChromeDriver (compatible with your Chrome version)

**you can download ChromeDriver by following given instructions** 

📌 Go to [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)

First, check your Chrome version by visiting chrome://settings/help in your browser.

Download the matching ChromeDriver version from the link above.

Unzip the ChromeDriver

After downloading, unzip the file.

You will get an executable file:

    chromedriver.exe on Windows

    chromedriver on macOS/Linux

Place the File in the Project

Create a folder named driver in the root of your project (if it doesn't already exist).

Move or copy the unzipped ChromeDriver file into the driver folder.

### 4️⃣ Run the Script

Now run the main script:

```bash
python main.py
```
You'll be prompted to enter:

    Your Amazon email

    Your password

    The product URL

    Number of pages to scrape

Scraped reviews will be saved in the data/ folder.

## 📁 Folder Structure

```
product_trend_analyzer/
├─ data/                            # Raw and processed data files
├─ DOCS/                            # Documentation notes
│  └─ README.md
├─ Drivers/                         # Any driver scripts or dependencies
├─ graphs/                          # Sample graph output
│  ├─ sample_graph1.png
│  └─ sample_graph2.png
├─ Leanings_from_errors/            # Lessons learned or debugging notes
│  └─ README.md
├─ module/  
│  ├─ __init__.py
│  ├─ BOM_Cleaner.py
│  ├─ BOM_collection.py
│  ├─ BOM_hype_analysis.py
│  ├─ BOM_sentiment_analyzer.py
│  └─ BOM_visualize.py
├─ tests/                           # Will contain test files
│  └─ README.md
├─ main.ipynb                       # Main Jupyter notebook (change to .py if script)
├─ README.md                        # Main project README
├─ requirement.txt                  # requirements.txt
└─ setup.ipynb                      # Setup steps in notebook form
```
## 🧪 Testing Instructions

Testing is not yet implemented in this version of the project.  
I plan to write unit tests using `pytest` to ensure the code works as expected.

Once tests are added, you’ll be able to run them using:

```bash
pytest
```
## 🛠️ Developer Setup

Follow these steps to set up the project locally as a developer:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/RanaSaadAli/product-trend-analyzer.git
cd product-trend-analyzer
```

### 2️⃣ Set Up a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup ChromeDriver

Please follow the [Getting Started](#setup-chromedriver) section for detailed steps on downloading and placing ChromeDriver in the correct folder.

### 5️⃣ Run the Project

```bash
python main.py
```

## Future releases

- 🌍 **Multi-region Support**: Add support for scraping reviews from different Amazon country domains (e.g., .co.uk, .de, .in).

- 📊 **Interactive Dashboard**: Integrate a Streamlit or Plotly Dash app for live visualizations.

- 🔁 **Scheduled Scraping**: Enable periodic scraping using schedulers like cron or APScheduler.

## Contributions

Contributions are welcome! Whether it’s fixing bugs, improving documentation, or suggesting new features — all help is appreciated.

### 📌 How to contribute:

1. Fork the repository.
2. Create a new branch:

```bash
git checkout -b your-feature-name
```
3. Make your changes.
4. Commit and push:

```bash
git commit -m "Your meaningful message"
git push origin your-feature-name
```
5. Open a Pull Request.

Feel free to open an issue first if you want to discuss an idea before working on it.
Thank you for making this project better! 💡

## license

This project is licensed under the terms of the [MIT License](LICENSE).

## Contact

If you have any questions, suggestions, or feedback, feel free to reach out:

- **Name**: Rana Saad Ali Khan
- **Email**: saad@example.com
- **GitHub**: [@RanaSaadAli](https://github.com/RanaSaadAli)
- **LinkedIn**: [Rana Saad Ali ](www.linkedin.com/in/rana-saad-ali-khan)

I'm happy to connect and collaborate!