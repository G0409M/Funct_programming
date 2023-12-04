import requests
import pandas as pd

# Funkcja do pobierania danych o kraju z API
def get_country_data(country_code):
    url = f'https://restcountries.com/v3/alpha/{country_code}'
    response = requests.get(url)
    data = response.json()
    return data

# Lista kodów krajów (możesz dostosować listę według własnych potrzeb)
country_codes = ['PL', 'US', 'CA', 'DE', 'FR', 'GB', 'IT', 'JP', 'AU', 'BR', 'IN', 'CN', 'RU', 'ZA', 'KR', 'MX', 'ES', 'ID', 'NG', 'EG']

# Inicjalizacja pustej listy do przechowywania danych krajów
all_countries_data = []

# Pętla pobierająca dane dla każdego kraju
for country_code in country_codes:
    country_data = get_country_data(country_code)
    all_countries_data.append(country_data)
# Wyodrębnij potrzebne informacje
country_info_list = []
for country_data in all_countries_data:
    country_name = country_data[0]['name']['common']
    country_population = country_data[0]['population'] if 'population' in country_data[0] else ''
    country_region = country_data[0]['region'] if 'region' in country_data[0] else ''
    country_subregion = country_data[0]['subregion'] if 'subregion' in country_data[0] else ''
    country_area = country_data[0]['area'] if 'area' in country_data[0] else ''
    country_capital = country_data[0]['capital'][0] if 'capital' in country_data[0] and country_data[0]['capital'] else ''
    country_gini = country_data[0]['gini']['2018'] if 'gini' in country_data[0] and '2018' in country_data[0]['gini'] else ''

    country_info_list.append([country_name, country_population, country_region, country_subregion, country_area, country_capital, country_gini])

# Utwórz DataFrame
columns = ['Country', 'Population', 'Region', 'Subregion', 'Area', 'Capital', 'Gini']
df = pd.DataFrame(country_info_list, columns=columns)


# Wyświetl DataFrame jako Markdown tabelę
print(df.to_markdown(index=False))

# Funkcja do sprawdzania przynależności kraju do regionu
def region_membership( country_name, region_name):
    country_row = df[df['Country'] == country_name]
    if not country_row.empty:
        country_region = country_row['Region'].values[0]
        return country_region == region_name
    else:
        return False
def check_region_membership(country_name, region_name):
    result = region_membership(country_name, region_name)
    if result:
        print(f"{country_name} belongs to {region_name}.")
    else:
        print(f"{country_name} does not belong to {region_name}.")

# Przykład użycia funkcji check_region_membership
check_region_membership('Poland', 'Europe')
check_region_membership('Egypt', 'Africa')
check_region_membership('Egypt', 'Asia')