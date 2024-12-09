from src.utils import predict, get_model, get_species_from_prediction
from flask import Flask, jsonify, request

classes = ['Iris Setosa', 'Iris Versicolour', 'Iris Virginica']

app = Flask('Penguins')


def predict_from_request(model_name, request_json):
    dv, sc, model = get_model(name=model_name)
    species, prediction = predict(request_json, model, dv, sc)
    species_name = get_species_from_prediction(species)
    result = {
        'species': species_name,
    }

    return jsonify(result)


@app.route('/predict_lr', methods=['POST'])
def predict_lr():
    return predict_from_request("lr", request.get_json())


@app.route('/predict_dt', methods=['POST'])
def predict_dt():
    return predict_from_request("dt", request.get_json())


@app.route('/predict_svm', methods=['POST'])
def predict_svm():
    return predict_from_request("svm", request.get_json())


@app.route('/predict_knn', methods=['POST'])
def predict_knn():
    return predict_from_request("knn", request.get_json())
