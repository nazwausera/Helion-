import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def scrape_helion():
    try:
        url = 'https://helion.pl/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.content, 'html.parser')
        
        promotions = []
        items = soup.find_all('div', class_='prod-item-sm', limit=2)
        
        for i, item in enumerate(items):
            try:
                title_elem = item.find('a', class_='prod-title')
                price_elem = item.find('span', class_='prod-price-now')
                
                if title_elem and price_elem:
                    title = title_elem.get_text(strip=True)[:100]
                    price = price_elem.get_text(strip=True)
                    promo_type = 'Książka Tygodnia' if i == 0 else 'Kurs Tygodnia'
                    
                    promotions.append({
                        'store': 'Helion',
                        'type': promo_type,
                        'title': title,
                        'price': price,
                        'url': 'https://helion.pl/'
                    })
            except:
                pass
        
        return promotions
    except Exception as e:
        print(f"Błąd Helion: {e}")
        return []

def scrape_onepress():
    try:
        url = 'https://onepress.pl/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.content, 'html.parser')
        
        promotions = []
        items = soup.find_all('div', class_='prod-item-sm', limit=1)
        
        for item in items:
            try:
                title_elem = item.find('a', class_='prod-title')
                price_elem = item.find('span', class_='prod-price-now')
                
                if title_elem and price_elem:
                    title = title_elem.get_text(strip=True)[:100]
                    price = price_elem.get_text(strip=True)
                    
                    promotions.append({
                        'store': 'Onepress',
                        'type': 'Książka Tygodnia',
                        'title': title,
                        'price': price,
                        'url': 'https://onepress.pl/'
                    })
            except:
                pass
        
        return promotions
    except Exception as e:
        print(f"Błąd Onepress: {e}")
        return []

def scrape_ebookpoint():
    try:
        url = 'https://ebookpoint.pl/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.content, 'html.parser')
        
        promotions = []
        items = soup.find_all('div', class_='prod-item-sm', limit=3)
        types = ['Książka Dnia', 'Audiobook Dnia', 'Kurs Tygodnia']
        
        for i, item in enumerate(items):
            try:
                title_elem = item.find('a', class_='prod-title')
                price_elem = item.find('span', class_='prod-price-now')
                
                if title_elem and price_elem:
                    title = title_elem.get_text(strip=True)[:100]
                    price = price_elem.get_text(strip=True)
                    
                    promotions.append({
                        'store': 'Ebookpoint',
                        'type': types[i] if i < len(types) else 'Promocja',
                        'title': title,
                        'price': price,
                        'url': 'https://ebookpoint.pl/'
                    })
            except:
                pass
        
        return promotions
    except Exception as e:
        print(f"Błąd Ebookpoint: {e}")
        return []

def main():
    print("🔍 Rozpoczynanie scrapingu...")
    
    all_promotions = []
    all_promotions.extend(scrape_helion())
    all_promotions.extend(scrape_onepress())
    all_promotions.extend(scrape_ebookpoint())
    
    data = {
        'updated': datetime.now().isoformat(),
        'promotions': all_promotions
    }
    
    with open('promocje.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Zapisano {len(all_promotions)} promocji!")

if __name__ == '__main__':
    main()
