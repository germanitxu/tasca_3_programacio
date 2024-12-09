import pandas as pd
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import StandardScaler


class PenguinClassificator:
    """
    SC: StandardScaler used
    x_train: Training data standardized
    Y_TRAIN: Train Species
    """
    SC: StandardScaler | None = None
    DV: DictVectorizer | None = None
    X_TRAIN = None
    X_TRAIN_VECTOR = None
    Y_TRAIN = None
    CATEGORICAL = ['sex', 'island']
    NUMERICAL = ['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm',
                 'body_mass_g']
    SPECIES_DICT = {
        "Chinstrap": 0,
        "Adelie": 1,
        "Gentoo": 2
    }
    SPECIES_DICT_REV = {
        0: "Chinstrap",
        1: "Adelie",
        2: "Gentoo"
    }

    def __init__(self, empty=False):
        if not empty:
            self._set_train_test_data()

    @staticmethod
    def _get_data() -> DataFrame:
        """
        Returns a dataframe empty of nulls
        :return: DataFrame
        """
        df = pd.read_csv("src/datasets/penguins.csv").dropna()
        # Penguins in this list have more than 2 genders, which is totally respectable, but it was breaking my DictVectorizer  # noqa
        df = df[df.sex.isin(["MALE", "FEMALE"])]
        return df

    @staticmethod
    def _save_data(data):
        data.to_csv("src/datasets/penguins_test.csv", index=False)

    def _set_train_test_data(self):
        # Retrieve the data
        df = self._get_data()

        # Swap species for numerical value
        df.species = df.species.replace(self.SPECIES_DICT)
        y = df.species.values
        x = df.loc[:, df.columns != 'species']

        # Split test and train data

        # df_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1, stratify=y)
        y_test_names = [self.SPECIES_DICT_REV[val] for val in y_test]
        x_test["species"] = y_test_names
        self._save_data(x_test)
        self.Y_TRAIN = y_train

        # One-hot prediction for training data
        train_dict = x_train[self.CATEGORICAL + self.NUMERICAL].to_dict(orient='records')
        dv_train = DictVectorizer(sparse=False)
        dv_train.fit(train_dict)
        x_train_vector = dv_train.transform(train_dict)
        self.DV = dv_train
        self.X_TRAIN_VECTOR = x_train_vector

        # Standardization
        sc = StandardScaler()
        sc.fit(x_train_vector)
        self.SC = sc
        self.X_TRAIN = sc.transform(x_train_vector)
        # We are also asked to do the standardization of the test data, althought we don't use it here
