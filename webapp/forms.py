from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length, NumberRange


class PenguinForm(FlaskForm):
    island_choices = [
        ("Biscoe", "Biscoe"),
        ("Dream", "Dream"),
        ("Torgersen", "Torgersen"),
    ]
    sex_choices = [("FEMALE", "Femella"), ("MALE", "Mascle")]
    model_choices = [
        ("lr", "Regressió Logística"),
        ("svm", "Màquina de Suport Vectorial"),
        ("dt", "Arbre de Decisió"),
        ("knn", "k-Nearest Neighbours"),
    ]
    model = SelectField(
        "Triau un model de predicció",
        validators=[DataRequired(), Length(min=1, max=50)],
        choices=model_choices,
    )
    island = SelectField(
        "Illa",
        validators=[DataRequired(), Length(min=1, max=50)],
        choices=island_choices,
    )
    culmen_length_mm = FloatField(
        "Longitud del bec  (mm)", validators=[DataRequired(), NumberRange(min=0)]
    )
    culmen_depth_mm = FloatField(
        "Profunditat del bec (mm)", validators=[DataRequired(), NumberRange(min=0)]
    )
    flipper_length_mm = IntegerField(
        "Longitud de l'aleta (mm)", validators=[DataRequired(), NumberRange(min=0)]
    )
    body_mass_g = IntegerField(
        "Massa corporal (g)", validators=[DataRequired(), NumberRange(min=0)]
    )
    sex = SelectField("Sexe", validators=[DataRequired()], choices=sex_choices)

    submit = SubmitField("Enviar")
