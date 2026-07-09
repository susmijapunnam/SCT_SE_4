# SCT_SE_4 - Web Scraping

## SkillCraft Technology Internship

### Task 04 - Web Scraping

---

## 📌 Project Overview

This project was developed as part of the **SkillCraft Technology Software Engineering Internship**.

The objective of this project is to build a Python-based web scraper that extracts product information from an e-commerce website and stores the extracted data in a structured CSV file.

The scraper collects important product details such as product name, price, and rating from the website **Books to Scrape**, a website specifically designed for practicing web scraping.

---

## 🎯 Objectives

The main objectives of this project are:

- Develop a Python web scraping application.
- Send HTTP requests to a website.
- Parse HTML pages using BeautifulSoup.
- Extract product information.
- Store extracted data in CSV format.
- Understand real-world data collection techniques.

---

## ⚙️ Algorithm / Methodology Used

### Web Scraping using Requests and BeautifulSoup

The application follows these steps:

1. Send an HTTP GET request to the website.
2. Receive the webpage HTML.
3. Parse the HTML using BeautifulSoup.
4. Locate each product using HTML tags and CSS classes.
5. Extract:
   - Product Name
   - Product Price
   - Product Rating
6. Store all extracted information in a Python list.
7. Convert the list into a Pandas DataFrame.
8. Export the DataFrame to a CSV file.

---

## ✨ Features

- Extracts product names.
- Extracts product prices.
- Extracts product ratings.
- Stores data in CSV format.
- Beginner-friendly implementation.
- Easy to modify for other websites.

---

## 🛠 Technologies Used

- Python 3
- Requests
- BeautifulSoup4
- Pandas
- CSV

---

## 📂 Project Structure

```
SCT_SE_4/
│
├── scraper.py
├── products.csv
├── requirements.txt
├── README.md
├── .gitignore
├── LICENSE
└── screenshots/
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/your-username/SCT_SE_4.git
```

Move into the project

```bash
cd SCT_SE_4
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python scraper.py
```

---

## 📊 Output

The program creates

```
products.csv
```

Example Output

| Product Name | Price | Rating |
|--------------|-------|--------|
| A Light in the Attic | £51.77 | Three |
| Tipping the Velvet | £53.74 | One |
| Sharp Objects | £47.82 | Four |

---

## 📚 Learning Outcomes

Through this project, I learned:

- Web Scraping
- HTTP Requests
- HTML Parsing
- BeautifulSoup
- Data Extraction
- Pandas DataFrames
- CSV File Handling
- Error Handling in Python

---

## 🔮 Future Enhancements

- Scrape multiple pages automatically.
- Export data to Excel.
- Store data in a database.
- Build a GUI for scraping.
- Add filtering and search options.
- Schedule automatic scraping.

---

## 👩‍💻 Author

**Name:** Susmija

**Internship:** SkillCraft Technology

**Repository:** SCT_SE_4

---

## ⭐ Acknowledgement

This project was completed as part of the **SkillCraft Technology Internship Program** to gain practical experience in Python programming and web scraping.
