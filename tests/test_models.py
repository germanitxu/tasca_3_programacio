import pandas as pd
import pickle
from src.utils import predict

# Before running the tests, make sure to run once main.py to generate the models


def get_model(name):
    with open(f"../src/saves/{name}.pck", "rb") as f:
        dv, sc, model = pickle.load(f)
    return dv, sc, model


models = ["lr", "dt", "knn", "svm"]
df = pd.read_csv("datasets/penguins_eval.csv")


def test_single_penguin(penguin):
    penguin.drop(columns="species", inplace=True)
    for model_name in models:
        dv, sc, model = get_model(model_name)
        penguin_dict = penguin.to_dict(orient="records")[0]
        species, prediction = predict(penguin_dict, model, dv, sc)
        assert (
            True in species
        ), "No species found for specimen."  # At least one species found


for _ in range(0, 10):
    random_penguin = df.sample(n=1)
    test_single_penguin(random_penguin)
