import requests
import pandas as pd
import tabulate
from functools import reduce
def creating_dataframe():
    country_codes = ['PL', 'US', 'CA', 'DE', 'FR', 'GB', 'IT', 'JP', 'AU', 'BR', 'IN', 'CN', 'RU', 'ZA', 'KR', 'MX',
                     'ES', 'ID', 'NG', 'EG', 'SA', 'AR', 'TR', 'IR', 'TH', 'IT', 'VN', 'PH', 'GB', 'FR',
                     'EG', 'GR', 'NL', 'PT', 'BE', 'SE', 'CH', 'AT', 'NO', 'DK', 'FI', 'IE', 'CL', 'CO', 'VE', 'PE',
                     'MY', 'SG', 'NZ']
    all_countries_data = []
    for country_code in country_codes:
        country_data = get_country_data(country_code)
        all_countries_data.append(country_data)
    country_info_list = []
    for country_data in all_countries_data:
        country_name = country_data[0]['name']['common']
        country_population = country_data[0]['population'] if 'population' in country_data[0] else ''
        country_region = country_data[0]['region'] if 'region' in country_data[0] else ''
        country_subregion = country_data[0]['subregion'] if 'subregion' in country_data[0] else ''
        country_area = country_data[0]['area'] if 'area' in country_data[0] else ''
        country_capital = country_data[0]['capital'][0] if 'capital' in country_data[0] and country_data[0][
            'capital'] else ''
        country_gini = country_data[0]['gini']['2018'] if 'gini' in country_data[0] and '2018' in country_data[0][
            'gini'] else ''
        country_info_list.append(
            [country_name, country_population, country_region, country_subregion, country_area, country_capital,
             country_gini])
    columns = ['Country', 'Population', 'Region', 'Subregion', 'Area', 'Capital', 'Gini']
    dframe = pd.DataFrame(country_info_list, columns=columns)
    return dframe

def get_country_data(country_code):
    url = f'https://restcountries.com/v3/alpha/{country_code}'
    response = requests.get(url)
    data = response.json()
    return data
def result(df):
    composed_function = compose(sort_dataframe_by_population,group_dataframe_by_subregion,filter_dataframe_by_subregion,filter_dataframe_by_region, filter_dataframe_by_letter_a)

    result_df = composed_function(df)

    print(result_df.to_markdown(index=False))

def compose(*funcs):
    return lambda initial: reduce(lambda acc, f: f(acc), reversed(funcs), initial)

def filter_dataframe_by_region(dframe):
    print("wybieranie tylko regionu EUROPE")
    filtered_df = dframe[(dframe['Region'] == 'Europe') |(dframe['Region'] == 'Americas') ]
    '''print(dframe.to_markdown(index=False))'''
    return filtered_df

def filter_dataframe_by_letter_a(dframe):
    print("wybieranie tylko państw które zawierają literę a")
    filtered_df = dframe[dframe['Country'].str.lower().str.contains('a')]
    '''print(dframe.to_markdown(index=False))'''
    return filtered_df
def filter_dataframe_by_subregion(dframe):
    print("wybieranie tylko państw które leżą w wschodniej lub środkowej europie lub połudiowej Ameryce")
    filtered_df = dframe[(dframe['Subregion'] == 'Western Europe') | (dframe['Subregion'] == 'Central Europe') | (dframe['Subregion'] == 'South America') ]
    '''print(dframe.to_markdown(index=False))'''
    return filtered_df
def sort_dataframe_by_population(dframe):
    print("Sortowanie danych po populacji")
    sorted_df = dframe.sort_values(by='Population', ascending=False)
    return sorted_df
def group_dataframe_by_subregion(dframe):
    print("Grouping DataFrame by Subregion")
    grouped_df = dframe.groupby('Subregion').agg({
        'Country': 'count',
        'Population': 'sum',
        'Area': 'sum'
    }).reset_index()
    return grouped_df