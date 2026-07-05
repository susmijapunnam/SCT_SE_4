import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"

# Send GET request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Store product data
products = []

# Find all books
books = soup.find_all("article", class_="product_pod")

for book in books:
    # Product Name
    name = book.h3.a["title"]

    # Price
    price = book.find("p", class_="price_color").text

    # Rating
    rating = book.p["class"][1]

    products.append({
        "Product Name": name,
        "Price": price,
        "Rating": rating
    })

# Convert to DataFrame
df = pd.DataFrame(products)

# Save CSV
df.to_csv("products.csv", index=False)

print("Data saved successfully!")
print(df.head())