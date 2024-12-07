import pickle

from sklearn.feature_extraction import DictVectorizer


def save_model(model, name, dv):
    """
    Saves the model and DictVectorizer into a file
    :param model: Model to save
    :param name: Name of the file
    :param dv: DictVectorizer
    :return:
    """
    with open(f"src/saves/{name}.pck", 'wb') as f:
        pickle.dump((dv, model), f)


def get_model(name):
    """
    Loads model and DictVectorizer
    :param name: Name of the model file to load
    :return: Tuple(DictVectorizer, model)
    """
    with open(f"src/saves/{name}.pck", 'rb') as f:
        dv, model = pickle.load(f)
    return dv, model


def predict(specimen, model, dv: DictVectorizer, percent=0.8):
    """
    Predict the result of specimen
    :param specimen: The specimen we are trying to get y_pred
    :param model: Model used for prediction
    :param dv: used when training data
    :param percent: from 0 to 1 both included, float at which a species is approved
    :return:
    """
    x = dv.transform(specimen)
    y_pred = model.predict_proba(x)
    return y_pred[0] >= percent, y_pred[0]


def get_species_from_prediction(prediction, percent: float = 0.8):
    """
    Since the species is predicted as a 0 to 2 value number, we have to transform it to its name.
    :param prediction: Prediction from model
    :param percent: Percentatge at
    :return:
    """
    from src.data import PenguinsData
    return PenguinsData.SPECIES_DICT_REV[list(prediction).index(True)]
