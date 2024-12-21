import pickle
from pathlib import Path

from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import StandardScaler


def save_model(model, name, dv, sc):
    """
    Saves the model and DictVectorizer into a file
    :param model: Model to save
    :param name: Name of the file
    :param dv: DictVectorizer
    :param sc: StandardScaler
    :return:
    """
    Path("src/saves").mkdir(parents=True, exist_ok=True)
    with open(f"src/saves/{name}.pck", "wb") as f:
        pickle.dump((dv, sc, model), f)


def get_model(name):
    """
    Loads model and DictVectorizer
    :param name: Name of the model file to load
    :return: Tuple(DictVectorizer, model)
    """
    with open(f"src/saves/{name}.pck", "rb") as f:
        dv, sc, model = pickle.load(f)
    return dv, sc, model


def predict(
    specimen: dict, model, dv: DictVectorizer, sc: StandardScaler, percent=0.5
) -> (list[bool], list[float]):
    """
    Predict the result of specimen
    :param specimen: The specimen we are trying to get y_pred
    :param model: Model used for prediction
    :param dv: DictVectorizer used when training data
    :param sc: StandardScaler used when training data
    :param percent: from 0 to 1 both included, float at which a species is approved
    :return: 2 list of species found as boolean and as float between 0 and 1
    """

    x_dv = dv.transform(specimen)
    x = sc.transform(x_dv)
    y_pred = model.predict_proba(x)
    return y_pred[0] >= percent, y_pred[0]


def get_species_from_prediction(prediction) -> str:
    """
    Since the species is predicted as a 0 to 2 value number, we have to transform it to its name.
    :param prediction: Prediction from model
    :return: Name of the species
    """
    from src.classificator import PenguinClassificator

    return PenguinClassificator.SPECIES_DICT_REV[list(prediction).index(True)]
