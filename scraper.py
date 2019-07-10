import requests
from bs4 import BeautifulSoup

URL = "https://www.skroutz.gr/search?keyphrase="

search = raw_input("Search: ")

URL = URL + search

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")
try:
    title = soup.find("div", attrs={"class": "details"}).find("h2").get_text()

    price = soup.find("div", attrs={"class": "price react-component"}).get_text().split()
    
    price = price[1].replace(".", "").replace(",", ".")
    
    fprice = float(price)

    print(title)

    print fprice, "EUR"
except AttributeError:
    try:
        title = soup.find("h1", attrs={"class": "page-title"}).get_text().strip()

        price = soup.find("div", attrs={"class": "price"}).get_text().split()

        price = price[0].replace(".", "").replace(",", ".")

        fprice = float(price)

        print(title)

        print fprice, "EUR"
    except AttributeError:
        print("Error")
    except UnicodeEncodeError:
        print("Error")
    

