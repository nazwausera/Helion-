import requests
import json
import os
from bs4 import BeautifulSoup
from datetime import datetime

API_KEY = os.getenv("SCRAPINGBEE_API_KEY")

def fetch_with_scrapingbee(url):
    api_url = (
        f"https://app.scrapingbee.com/api/v1/"
        f"?api_key={API_KEY}"
        f"&url={url}"
        f"&render_js=true"
        f"&wait=3000"
        f"&block_resources=false"
    )
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
        "Safari/537.36"
    }
    response = requests.get(api_url, headers=headers, timeout=30)
    response.raise_for_status()
    print(f"\nSCRAPINGBEE_API_KEY: {API_KEY}\n")
    print(f"\n=== HTML zawartość {url} (pierwsze 3000 znaków) ===\n")
    print(response.text[:3000])
    print(f"\n=== KONIEC HTML {url} ===\n")
    return response.text

def get_promotions_helion():
    html = fetch_with_scrapingbee("https://helion.pl/")
    soup = BeautifulSoup(html, "html.parser")
    results = []
    items = soup.find_all("div", class_="promo-book-const")
    print("Znaleziono kontenerów Helion:", len(items))
    for i, item in enumerate(items[:2]):
        book_info = item.find("div", class_="book-of-day-container")
        title_elem = book_info.find("a") if book_info else None
        price_elem = book_info.find("div", class_="book-of-day-price-info") if book_info else None
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
    print("Znaleziono kontenerów Onepress:", len(items))
    for item in items[:1]:
        book_info = item.find("div", class_="book-of-day-container")
        title_elem = book_info.find("a") if book_info else None
        price_elem = book_info.find("div", class_="book-of-day-price-info") if book_info else None
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
    print("Znaleziono kontenerów Ebookpoint:", len(items))
    types = ["Książka Dnia", "Audiobook Dnia", "Kurs Tygodnia"]
    for i, item in enumerate(items[:3]):
        book_info = item.find("div", class_="book-of-day-container")
        title_elem = book_info.find("a") if book_info else None
        price_elem = book_info.find("div", class_="book-of-day-price-info") if book_info else None
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
    print(f"\nZapisano {len(promotions)} promocji do promocje.json\n")

if __name__ == "__main__":
    main()
