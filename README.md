# Tasca 3 Programació d'intel·ligència artificial

## Requeriments

python>=3.12
poetry>=1.8.4

## Instal·lació
Clona el repositori
```shell
git clone git@github.com:germanitxu/tasca_3_programacio.git
```
```shell
cd tasca_3_programacio
```
Usa poetry per instalar les llibreries

```shell
poetry install
```

## Com utilitzar

Pren l'aplicació llançant amb python el script `main.py`

```shell
poetry run python main.py
```


A `main.py` s'entrenen els models, es guardan als fitxers y levanta el servidor flask.

Sense desconectar aques fil, pots probar els tests y el client, explicats a continuació.

### Tests
A la carpeta `test` n'hi ha dos scripts per testear el models y la aplicació de flask, usant una troç de dades dels pinguins guardada a `tests/datasets`.

### Proves del client

Dins la carpeta `webapp`, el fitxer `client.py` usa els datasets de tests [penguins_test.csv]([https://github.com/germanitxu/tasca_3_programacio/blob/master/src/datasets/penguins_test.csv]) per fer cridades cadascuns dels endpoints del server de flask.
```shell
poetry run python webapp/client.py
```
Per fer cridades usant curl o un client de petitions, pots usar aquest eixample:

```shell
curl --request POST "http://127.0.0.1:8000/predict_lr" --header "Content-Type: application/json" --data-raw "{
    \"island\": \"Torgersen\",
    \"culmen_length_mm\": 35.7,
    \"culmen_depth_mm\": 17,
    \"flipper_length_mm\": 189,
    \"body_mass_g\": 3350,
    \"sex\": \"FEMALE\"
}"
```
