# Zyte-Assignment-1
Basic Spider and Deploy in Scrapy Cloud

Developed by Phillip Gallas, as a coding challenge for Zyte (formerly known as ScrapingHub).
This spider navigates through all categories in the website and scrapes the information for each book in each page. In total, the title, the price, the URL for the image of the book and the URL for the detailed page were gathered for all 1000 books of the website.

Firstly, install the scrapy module by executing:
```sh
$ pip3 install scrapy
```

To run the spider via the Terminal (saving the output), run:
```sh
$ scrapy runspider zyte_assignment1.py -o scraped_books.csv
```
