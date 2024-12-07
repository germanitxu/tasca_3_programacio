from src.data import PenguinsData
from src.models import Models
from webapp.service import app

# Retrieve the data
data = PenguinsData()
models = Models(data)
models.save_models()

app.run(debug=True, port=8000)