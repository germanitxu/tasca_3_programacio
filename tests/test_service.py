import requests

base_data = {
    "island": 0,
    "culmen_length_mm": 0,
    "culmen_depth_mm": 0,
    "flipper_length_mm": 0,
    "body_mass_g": 0,
    "sex": "FEMALE",
}
endpoints = ["predict_lr", "predict_svm", "predict_dt", "predict_knn"]
base_url = "http://127.0.0.1:8000/"

for endpoint in endpoints:
    print(f"Using {endpoint}")
    url = base_url + endpoint
    response = requests.post(url, json=base_data)
    assert response is not None
