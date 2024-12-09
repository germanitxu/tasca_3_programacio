from src.classificator import PenguinClassificator
from src.models import Models
from webapp.service import app

# Retrieve the data
data = PenguinClassificator()
models = Models(data)
models.save_models()

app.run(debug=True, port=8000)