import requests
import json
import os
from bs4 import BeautifulSoup
from datetime import datetime

# Pobierz API Key ze zmiennej środowiskowej (GitHub Actions)
API_KEY = os.getenv("SCRAPINGBEE_API_KEY")
print("SCRAPINGBEE_API_KEY:", API_KEY)



def fetch_with_scrapingbee(url):
    api_url = f"https://app.scrapingbee.com/api/v1/?api_key={API_KEY}&url={url}&render_js=true"
    response = requests.get(api_url, timeout=30)
    response.raise_for_status()
    return response.text

def get_promotions_helion():
    html = fetch_with_scrapingbee("https://helion.pl/")
    soup = BeautifulSoup(html, "html.parser")
    results = []
    # Przykład: szuka promocji w bloku 'promo-book-const'
    items = soup.find_all("div", class_="promo-book-const")
    for i, item in enumerate(items[:2]):  # Książka tygodnia i kurs tygodnia
        book_info = item.find("div", class_="book-of-day-container")
        if not book_info:
            continue
        title_elem = book_info.find("a")
        price_elem = book_info.find("div", class_="book-of-day-price-info")
        title = title_elem.get_text(strip=True) if title_elem else "Brak tytułu"
        price = price_elem.get_text(strip=True) if price_elem else "Brak ceny"
        promo_type = "Książka Tygodnia" if i == 0 else "Kurs Tygodnia"
        results.append({
            "store": "Helion",
            "type": promo_type,
            "title": title,
            "price": price,
            "url": "https://helion.pl/"
        })
    return results

def get_promotions_onepress():
    html = fetch_with_scrapingbee("https://onepress.pl/")
    soup = BeautifulSoup(html, "html.parser")
    results = []
    items = soup.find_all("div", class_="promo-book-const")
    for item in items[:1]:  # Książka tygodnia
        book_info = item.find("div", class_="book-of-day-container")
        if not book_info:
            continue
        title_elem = book_info.find("a")
        price_elem = book_info.find("div", class_="book-of-day-price-info")
        title = title_elem.get_text(strip=True) if title_elem else "Brak tytułu"
        price = price_elem.get_text(strip=True) if price_elem else "Brak ceny"
        results.append({
            "store": "Onepress",
            "type": "Książka Tygodnia",
            "title": title,
            "price": price,
            "url": "https://onepress.pl/"
        })
    return results

def get_promotions_ebookpoint():
    html = fetch_with_scrapingbee("https://ebookpoint.pl/")
    soup = BeautifulSoup(html, "html.parser")
    results = []
    items = soup.find_all("div", class_="promo-book-const")
    types = ["Książka Dnia", "Audiobook Dnia", "Kurs Tygodnia"]
    for i, item in enumerate(items[:3]):  # Trzy promocje dzienne
        book_info = item.find("div", class_="book-of-day-container")
        if not book_info:
            continue
        title_elem = book_info.find("a")
        price_elem = book_info.find("div", class_="book-of-day-price-info")
        title = title_elem.get_text(strip=True) if title_elem else "Brak tytułu"
        price = price_elem.get_text(strip=True) if price_elem else "Brak ceny"
        results.append({
            "store": "Ebookpoint",
            "type": types[i] if i < len(types) else "Promocja",
            "title": title,
            "price": price,
            "url": "https://ebookpoint.pl/"
        })
    return results

def main():
    promotions = []
    promotions.extend(get_promotions_helion())
    promotions.extend(get_promotions_onepress())
    promotions.extend(get_promotions_ebookpoint())
    out = {"updated": datetime.now().isoformat(), "promotions": promotions}
    with open("promocje.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
