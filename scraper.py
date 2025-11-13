import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def scrape_helion():
    """Scraper dla Helion.pl"""
    try:
        url = 'https://helion.pl/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.content, 'html.parser')
        
        promotions = []
        
        # Szuka wszystkich kontenerów promocji
        items = soup.find_all('div', class_='promo-book-const')
        
        for i, item in enumerate(items):
            try:
                # Szuka kontenera z informacjami
                book_info = item.find('div', class_='book-of-day-container')
                if not book_info:
                    continue
                
                # Tytuł - szuka linku wewnątrz
                title_elem = book_info.find('a')
                if not title_elem:
                    title_elem = book_info.find('div', class_='book-of-day-cover')
                
                title = title_elem.get_text(strip=True)[:120] if title_elem else 'Brak tytułu'
                
                # Cena
                price_elem = book_info.find('div', class_='book-of-day-price-info')
                price = price_elem.get_text(strip=True) if price_elem else 'Brak ceny'
                
                # Typ promocji
                promo_type = 'Książka Tygodnia' if i == 0 else 'Kurs Tygodnia'
                
                # Pomijaj puste wpisy
                if 'Brak' not in title:
                    promotions.append({
                        'store': 'Helion',
                        'type': promo_type,
                        'title': title,
                        'price': price,
                        'url': 'https://helion.pl/'
                    })
                    
            except Exception as e:
                print(f"Błąd przy przetwarzaniu elementu Helion: {e}")
                continue
        
        print(f"✅ Helion: znaleziono {len(promotions)} promocji")
        return promotions
        
    except Exception as e:
        print(f"❌ Błąd Helion: {e}")
        return []


def scrape_onepress():
    """Scraper dla Onepress.pl"""
    try:
        url = 'https://onepress.pl/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.content, 'html.parser')
        
        promotions = []
        
        # Szuka kontenerów (zakładamy podobną strukturę)
        items = soup.find_all('div', class_='promo-book-const')
        
        if not items:
            # Fallback na inne selektory
            items = soup.find_all('div', class_='book-of-day-container')
        
        for item in items:
            try:
                title_elem = item.find('a')
                if not title_elem:
                    title_elem = item.find('div', class_='book-of-day-cover')
                
                title = title_elem.get_text(strip=True)[:120] if title_elem else None
                
                price_elem = item.find('div', class_='book-of-day-price-info')
                price = price_elem.get_text(strip=True) if price_elem else None
                
                if title and price and 'Brak' not in title:
                    promotions.append({
                        'store': 'Onepress',
                        'type': 'Książka Tygodnia',
                        'title': title,
                        'price': price,
                        'url': 'https://onepress.pl/'
                    })
                    break  # Bierz tylko pierwszą
                    
            except Exception as e:
                print(f"Błąd przy przetwarzaniu elementu Onepress: {e}")
                continue
        
        print(f"✅ Onepress: znaleziono {len(promotions)} promocji")
        return promotions
        
    except Exception as e:
        print(f"❌ Błąd Onepress: {e}")
        return []


def scrape_ebookpoint():
    """Scraper dla Ebookpoint.pl"""
    try:
        url = 'https://ebookpoint.pl/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.content, 'html.parser')
        
        promotions = []
        
        # Szuka kontenerów (zakładamy podobną strukturę)
        items = soup.find_all('div', class_='promo-book-const')
        
        if not items:
            items = soup.find_all('div', class_='book-of-day-container')
        
        types = ['Książka Dnia', 'Audiobook Dnia', 'Kurs Tygodnia']
        count = 0
        
        for i, item in enumerate(items):
            if count >= 3:
                break
                
            try:
                title_elem = item.find('a')
                if not title_elem:
                    title_elem = item.find('div', class_='book-of-day-cover')
                
                title = title_elem.get_text(strip=True)[:120] if title_elem else None
                
                price_elem = item.find('div', class_='book-of-day-price-info')
                price = price_elem.get_text(strip=True) if price_elem else None
                
                if title and price and 'Brak' not in title:
                    promotions.append({
                        'store': 'Ebookpoint',
                        'type': types[count] if count < len(types) else 'Promocja',
                        'title': title,
                        'price': price,
                        'url': 'https://ebookpoint.pl/'
                    })
                    count += 1
                    
            except Exception as e:
                print(f"Błąd przy przetwarzaniu elementu Ebookpoint: {e}")
                continue
        
        print(f"✅ Ebookpoint: znaleziono {len(promotions)} promocji")
        return promotions
        
    except Exception as e:
        print(f"❌ Błąd Ebookpoint: {e}")
        return []


def main():
    print("=" * 50)
    print("🔍 ROZPOCZYNAM SCRAPING PROMOCJI")
    print("=" * 50)
    
    all_promotions = []
    
    # Pobierz z każdego sklepu
    print("\n📚 Helion.pl...")
    all_promotions.extend(scrape_helion())
    
    print("📚 Onepress.pl...")
    all_promotions.extend(scrape_onepress())
    
    print("📚 Ebookpoint.pl...")
    all_promotions.extend(scrape_ebookpoint())
    
    # Przygotuj dane
    data = {
        'updated': datetime.now().isoformat(),
        'promotions': all_promotions
    }
    
    # Zapisz do JSON
    with open('promocje.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("\n" + "=" * 50)
    print(f"✅ GOTOWE! Zapisano {len(all_promotions)} promocji")
    print(f"📅 Czas: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)


if __name__ == '__main__':
    main()
