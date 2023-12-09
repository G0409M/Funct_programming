import requests
import pandas as pd
import tabulate
from Functions import result, creating_dataframe
# Część odpowiadająca za pobieranie danych
dframe=creating_dataframe()
print("Pobrane dane: ")
print(dframe.to_markdown(index=False))
# Część funkcyjna
result(dframe)
# Część graficzna