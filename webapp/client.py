import pandas as pd
import requests
import json

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

df = pd.read_csv("../tests/datasets/penguins_eval.csv")
for index, penguin in df.iterrows():
    print(">>>")
    print(penguin)
    print(">>>")
    penguin_species = penguin.to_dict()["species"]
    penguin.drop(labels="species", inplace=True)
    for endpoint in endpoints:
        print(f"Using {endpoint}")
        url = base_url + endpoint
        response = requests.post(url, json=penguin.to_dict())
        species = json.loads(response.content)["species"]
        print(species == penguin_species)
