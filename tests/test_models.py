import pandas as pd
import pickle
from src.data import PenguinsData


# Before running the tests, make sure to run once main.py to generate the models

def get_model(name):
    with open(f"../src/saves/{name}.pck", 'rb') as f:
        dv, model = pickle.load(f)
    return dv, model


models = ["lr", "dt", "knn", "svm"]
df = pd.read_csv("datasets/penguins_eval.csv")

def test_single_penguin(penguin):
    print("Testing:")
    print(penguin)
    penguin_species = penguin.species.to_list()[0]
    penguin.drop(columns="species", inplace=True)
    for model_name in models:
        dv, model = get_model(model_name)
        val_dict = penguin[PenguinsData.NUMERICAL + PenguinsData.CATEGORICAL].to_dict(orient='records')
        X_val = dv.transform(val_dict)
        y_pred = model.predict_proba(X_val)
        species = PenguinsData.SPECIES_DICT_REV[list(y_pred[0] >= 0.8).index(True)]
        print(model_name, species == penguin_species)
    print("\n")

for _ in range(0, 10):
    random_penguin = df.sample(n=1)
    test_single_penguin(random_penguin)
