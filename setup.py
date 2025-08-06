from setuptools import setup, find_packages
setup(
    name = "trend_analyzer",
    version = "1.0.0",
    author = "Rana Saad Ali Khan",
    author_email = "saadalikhanrana86@gmail.com",
    description = "A tool for analyzing products on amazon using scraping and sentiment analysis.",
    url = "https://github.com/RanaSaadAli/product-trend-analyzer.git",
    packages = find_packages(include=['module','module.*']),
    install_requires = [
        'beautifulsoup4==4.13.4',
        'emoji==2.14.1',
        'matplotlib==3.10.3',
        'numpy==2.3.2',
        'pandas==2.3.1',
        'selenium==4.34.2',
        'textblob==0.19.0',
        'undetected-chromedriver==3.5.5'
    ]
)