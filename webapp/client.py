import pandas as pd
import requests
import json
from pprint import pprint
base_data = {
    "island": 0,
    "culmen_length_mm": 0,
    "culmen_depth_mm": 0,
    "flipper_length_mm": 0,
    "body_mass_g": 0,
    "sex": "FEMALE",
}
endpoints = {
    "Logistic Regression": "predict_lr",
    "Support Vector Machine": "predict_svm",
    "Decision Tree": "predict_dt",
    "k-Nearest Neighbours": "predict_knn"
}
base_url = "http://127.0.0.1:8000/"

df = pd.read_csv("src/datasets/penguins_test.csv", index_col=False)
penguins = df.sample(n=3)
match = {}
miss = {}
for index, penguin in penguins.iterrows():
    penguin_species = penguin.to_dict()["species"]
    penguin.drop(labels="species", inplace=True)
    print("Pingüí:")
    pprint(penguin.to_dict(), width=1)
    for model_name, endpoint in endpoints.items():
        try:
            url = base_url + endpoint
            response = requests.post(url, json=penguin.to_dict())
            species = json.loads(response.content)["species"]
            if species == penguin_species:
                match[model_name] = match.get(model_name, 0) + 1
            else:
                miss[model_name] = miss.get(model_name, 0) + 1
        except Exception as e:
            print(e)

print("Total penguins: ", len(penguins))
print("Matched species: ")
pprint(match, width=2)
print("Didn't match species:")
pprint(miss, width=2)
