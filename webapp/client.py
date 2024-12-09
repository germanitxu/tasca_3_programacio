import pandas as pd
import requests
import json
import os

base_data = {
    "island": 0,
    "culmen_length_mm": 0,
    "culmen_depth_mm": 0,
    "flipper_length_mm": 0,
    "body_mass_g": 0,
    "sex": "FEMALE",
}
endpoints = ["predict_lr", "predict_svm", "predict_dt", "predict_knn"]
base_url = "http://127.0.0.1:8000/"

df = pd.read_csv("src/datasets/penguins_test.csv")
match = {}
miss = {}

for index, penguin in df.iterrows():
    penguin_species = penguin.to_dict()["species"]
    penguin.drop(labels="species", inplace=True)
    for endpoint in endpoints:
        try:
            url = base_url + endpoint
            response = requests.post(url, json=penguin.to_dict())
            species = json.loads(response.content)["species"]
            if species == penguin_species:
                match[endpoint] = match.get(endpoint, 0) + 1
            else:
                miss[endpoint] = miss.get(endpoint, 0) + 1
        except Exception as e:
            print(e)

print("Total penguins: ", len(df))
print(f"Matched species: {match}")
print(f"Didn't match species: {miss}")

