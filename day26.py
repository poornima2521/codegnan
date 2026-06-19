import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import re
from bs4 import BeautifulSoup
url="https://books.toscrape.com/"
try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text,"html.parser")
    books = []
    for article in soup.find_all("article",class_="product_pod"):
        title = article.h3.a["title"]
        price = article.find("p",class_="price_color").text
        books.append({"Title": title, "Price": price})
    df = pd.DataFrame(books)
    print(df.head())
    df["Price"] = (
        df["Price"]
        .str.replace("Â","", regex=False)  
        .str.replace("£","", regex=False)   
        .astype(float)                       
    )
    plt.bar(df["Title"],df["Price"],color="skyblue", edgecolor="black")
    plt.xlabel("Price (£)")
    plt.ylabel("Number of Books")
    plt.title("Book Price Distribution")
    plt.show()
except Exception as e:
    print("Error occurred:", e)
