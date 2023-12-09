import requests
import pandas as pd
import tabulate
from Functions import result, creating_dataframe, write_to_excel
# Część odpowiadająca za pobieranie danych
dframe = creating_dataframe()
print("Pobrane dane: ")
print(dframe.to_markdown(index=False))
write_to_excel(dframe, "input.xlsx")
# Część funkcyjna
r_dframe = result(dframe)
print(r_dframe.to_markdown(index=False))
#Zapisywanie wyników w excelu
write_to_excel(r_dframe, "result.xlsx")
# Część graficzna