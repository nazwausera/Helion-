żądania importu
z bs4 import BeautifulSoup
importuj json
z importu datetime datetime

def scrape_helion():
    próbować:
        url = 'https://helion.pl/'
        nagłówki = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        odpowiedź = żądania.get(url, nagłówki=nagłówki, limit czasu=10)
        response.encoding = 'utf-8'
        zupa = PięknaZupa(zawartośćodpowiedzi, 'html.parser')
        
        promocje = []
        elementy = soup.find_all('div', class_='prod-item-sm', limit=2)
        
        dla i, element w enumerate(elementy):
            próbować:
                title_elem = item.find('a', class_='prod-title')
                price_elem = item.find('span', class_='prod-price-now')
                
                jeśli title_elem i price_elem:
                    title = title_elem.get_text(strip=True)[:100]
                    cena = price_elem.get_text(strip=True)
                    promo_type = 'Książka Tygodnia' if i == 0 else 'Kurs Tygodnia'
                    
                    promocje.append({
                        'sklep': 'Helion',
                        'type': typ_promocji,
                        'tytuł': tytuł,
                        'cena': cena,
                        'url': 'https://helion.pl/'
                    })
            z wyjątkiem:
                przechodzić
        
        promocje zwrotne
    z wyjątkiem wyjątku jako e:
        print(f"Błąd Helion: {e}")
        powrót []

def scrape_onepress():
    próbować:
        url = 'https://onepress.pl/'
        nagłówki = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        odpowiedź = żądania.get(url, nagłówki=nagłówki, limit czasu=10)
        response.encoding = 'utf-8'
        zupa = PięknaZupa(zawartośćodpowiedzi, 'html.parser')
        
        promocje = []
        elementy = soup.find_all('div', class_='prod-item-sm', limit=1)
        
        dla pozycji w pozycjach:
            próbować:
                title_elem = item.find('a', class_='prod-title')
                price_elem = item.find('span', class_='prod-price-now')
                
                jeśli title_elem i price_elem:
                    title = title_elem.get_text(strip=True)[:100]
                    cena = price_elem.get_text(strip=True)
                    
                    promocje.append({
                        'sklep': 'Onepress',
                        „typ”: „Książka Tygodnia”,
                        'tytuł': tytuł,
                        'cena': cena,
                        'url': 'https://onepress.pl/'
                    })
            z wyjątkiem:
                przechodzić
        
        promocje zwrotne
    z wyjątkiem wyjątku jako e:
        print(f"Bład Onepress: {e}")
        powrót []

def scrape_ebookpoint():
    próbować:
        url = 'https://ebookpoint.pl/'
        nagłówki = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        odpowiedź = żądania.get(url, nagłówki=nagłówki, limit czasu=10)
        response.encoding = 'utf-8'
        zupa = PięknaZupa(zawartośćodpowiedzi, 'html.parser')
        
        promocje = []
        elementy = soup.find_all('div', class_='prod-item-sm', limit=3)
        typy = ['Książka Dnia', 'Audiobook Dnia', 'Kurs Tygodnia']
        
        dla i, element w enumerate(elementy):
            próbować:
                title_elem = item.find('a', class_='prod-title')
                price_elem = item.find('span', class_='prod-price-now')
                
                jeśli title_elem i price_elem:
                    title = title_elem.get_text(strip=True)[:100]
                    cena = price_elem.get_text(strip=True)
                    
                    promocje.append({
                        'sklep': 'Ebookpoint',
                        'type': types[i] jeśli i < len(types) w przeciwnym razie 'Promocja',
                        'tytuł': tytuł,
                        'cena': cena,
                        'url': 'https://ebookpoint.pl/'
                    })
            z wyjątkiem:
                przechodzić
        
        promocje zwrotne
    z wyjątkiem wyjątku jako e:
        print(f"Bład Ebookpoint: {e}")
        powrót []

def main():
    print("đŸ” Rozpoczynanie skrobania...)
    
    wszystkie_promocje = []
    all_promotions.extend(scrape_helion())
    all_promotions.extend(scrape_onepress())
    all_promotions.extend(scrape_ebookpoint())
    
    dane = {
        'zaktualizowano': datetime.now().isoformat(),
        'promocje': wszystkie_promocje
    }
    
    z otwartym('promocje.json', 'w', kodowanie='utf-8') jako f:
        json.dump(dane, f, Ensure_ascii=False, indent=2)
    
    print(f"âœ… Zapisano {len(all_promotions)} promocja!")

jeśli __name__ == '__main__':
    główny()
