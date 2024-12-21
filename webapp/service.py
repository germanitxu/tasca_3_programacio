import secrets
import os
import json
from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect
from markupsafe import Markup

from src.utils import predict, get_model, get_species_from_prediction
from webapp.forms import PenguinForm
from flask import Flask, jsonify, request, render_template, Response

classes = ["Iris Setosa", "Iris Versicolour", "Iris Virginica"]
template_dir = os.path.abspath("webapp/templates")
images_dir = os.path.abspath("webapp/static")
app = Flask("Penguins", template_folder=template_dir, static_folder=images_dir)
foo = secrets.token_urlsafe(16)
app.secret_key = foo
# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)
# Flask-WTF requires this line
csrf = CSRFProtect(app)


def predict_from_request(model_name, request_json) -> Response:
    dv, sc, model = get_model(name=model_name)
    species, prediction = predict(request_json, model, dv, sc)
    species_name = get_species_from_prediction(species)
    result = {
        "species": species_name,
    }

    return jsonify(result)


@app.route("/predict_lr", methods=["POST"])
def predict_lr():
    return predict_from_request("lr", request.get_json())


@app.route("/predict_dt", methods=["POST"])
def predict_dt():
    return predict_from_request("dt", request.get_json())


@app.route("/predict_svm", methods=["POST"])
def predict_svm():
    return predict_from_request("svm", request.get_json())


@app.route("/predict_knn", methods=["POST"])
def predict_knn():
    return predict_from_request("knn", request.get_json())


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/form", methods=["GET", "POST"])
def form():
    form_object = PenguinForm()
    svg = Markup(open(images_dir + "/images/penguin.svg").read())
    if form_object.validate_on_submit():
        penguin = {
            "island": form_object.island.data,
            "culmen_length_mm": form_object.culmen_length_mm.data,
            "culmen_depth_mm": form_object.culmen_depth_mm.data,
            "flipper_length_mm": form_object.flipper_length_mm.data,
            "body_mass_g": form_object.body_mass_g.data,
            "sex": form_object.sex.data,
        }
        model = form_object.model.data
        species = json.loads(predict_from_request(model, penguin).data)[
            "species"
        ]  # noqa
        return render_template(
            "penguin.html", form=form_object, species=species, penguin=penguin, svg=svg
        )
    return render_template("penguin.html", form=form_object, svg=svg)
