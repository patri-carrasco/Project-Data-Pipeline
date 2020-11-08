def update_price_nan(reference):
    parametros = reference
    response = requests.get(f'https://www.amazon.es/s?k=lego+{parametros}')
    if response.status_code != 200:
        print(f'Error {response.status_code}')
    else:
        try:
            response.json()
        except Exception:
            print(f"The content is not JSONeable")
        
    soup = BeautifulSoup(response.content)
    possible_price = soup.find_all("span", class_="a-offscreen")
    
    string_price = possible_price[0].text
    result = string_price.strip()
    result = result.replace(',','.')
    
    price = float(result[:-2])
    return price