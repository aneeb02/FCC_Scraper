import requests
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import quote_plus
import time


with open("articles.csv", "w") as articles:
  csv_writer = csv.writer(articles)
  csv_writer.writerow(['Title', 'URL'])
  

  driver = webdriver.Chrome()
  topic = input("What topic would you like to search?")
  encoded_topic = quote_plus(topic)
  query = f"https://www.freecodecamp.org/news/search?query={encoded_topic}"

  driver.get(query)
  time.sleep(3) # wait for site to load completely

  source = driver.page_source
  soup = BeautifulSoup(source, 'lxml')

  articles = soup.select('div.post-feed')
  for article in articles:
    titles = article.select('h2.post-card-title')
    for title in titles:
      text = title.select('a')
      for t in text:
        csv_writer.writerow([t.text.strip(), t.get('href')])  # write title, url to csv file
        
  print("Successfully added all relevant articles in file!")