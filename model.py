""" Models.py - main module"""
import pickle
from dataclasses import dataclass
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV,\
    cross_val_score, cross_val_predict, KFold
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



plt.style.use('seaborn')


@dataclass
class Model:
    """ class Model - Random Forest Classifier Model """

    filename: str = "krisha_data.xlsx"
    model_filename = "model.pkl"
    param_forest = {'clf__n_estimators': [10, 20, 50],
                    'clf__max_features': [None, 1, 2],
                    'clf__max_depth': [1, 2, 5]}

    def train_model(self):
        """ train_model - method to train and save model """
        pipe_forest = Pipeline([('clf', RandomForestRegressor())])
        x, y = self.preprocessing(self.get_dataframe())
        x_train, x_test, y_train, y_test = train_test_split(x,
                                                            y,
                                                            test_size=0.33,
                                                            random_state=0)
        model = self.get_model(pipe_forest, self.param_forest, x_train, y_train)
        with open(self.model_filename, 'wb') as file:
            pickle.dump(model, file)

    def get_dataframe(self) -> pd.DataFrame:
        """ get_dataframe - method to fetch dataframe """
        file = pd.read_excel(self.filename)
        dataframe = pd.DataFrame(file)
        return dataframe

    @staticmethod
    def preprocessing(data) -> tuple:
        """ preprocessing - method to preprocess dataframe """
        # clean redundant values
        data = data.replace('\n', ' ', regex=True)
        data = data.replace('  ', ' ', regex=True)
        data = data.replace('  ', ' ', regex=True)
        data = data.replace('  ', ' ', regex=True)
        data = data.replace('  ', ' ', regex=True)

        # make price column numeric
        data[['Price']] = data[['Price']].apply(pd.to_numeric)

        # get standard deviation of a data price
        data = data[np.abs(data["Price"]-data["Price"].mean()) <= (3*data["Price"].std())]

        #
        numeric_data = data[['Price', 'Rooms', 'Square', 'Latitude', 'Longitude']]
        categorical_data_names = ['isMortgaged', 'Building', 'Floor', 'FloorType', 'PrivDormitory',
                                  'Renovation', 'TelephoneType', 'InternetType', 'BathroomType',
                                  'Balcony', 'BalconyGlazed', 'DoorType', 'Parking', 'Furniture',
                                  'Country', 'City', 'HasChange', 'District', 'Street', 'HouseNum',
                                  'FloorType', 'CeilingHeight', 'Security', 'MapComplex']

        new_df = pd.DataFrame()
        for categorical_data_name in categorical_data_names:
            new_df = pd.concat([new_df,
                                pd.get_dummies(data[categorical_data_name])],
                               axis='columns')

        renew_df = pd.concat([new_df, numeric_data], axis='columns')
        renew_df.dropna(inplace=True)
        y = renew_df.Price
        x = renew_df
        return x, y

    @staticmethod
    def get_model(pipeline, parameters, x_train, y_train):
        """ get_model - method to fit and get model """
        grid_obj = GridSearchCV(estimator=pipeline,
                                param_grid=parameters,
                                cv=3,
                                scoring='r2',
                                verbose=2,
                                n_jobs=1,
                                refit=True)
        grid_obj.fit(x_train, y_train)
        return grid_obj

    @staticmethod
    def plot(grid_obj, x, y):
        """ plot - method to plot model features """
        results = pd.DataFrame(pd.DataFrame(grid_obj.cv_results_))
        results_sorted = results.sort_values(by=['mean_test_score'], ascending=False)
        print(results_sorted)
        estimator = grid_obj.best_estimator_

        shuffle = KFold(n_splits=5,
                        shuffle=True,
                        random_state=0)
        cv_scores = cross_val_score(estimator,
                                    x,
                                    y.values.ravel(),
                                    cv=shuffle,
                                    scoring='r2')

        y_pred = cross_val_predict(estimator, x, y, cv=shuffle)

        plt.scatter(y, y_pred)
        xmin, xmax = plt.xlim()
        ymin, ymax = plt.ylim()
        plt.plot([xmin, xmax], [ymin, ymax], "g--", lw=1, alpha=0.4)
        plt.xlabel("True prices")
        plt.ylabel("Predicted prices")
        plt.annotate(f' R-squared CV = {round(float(cv_scores.mean()), 3)}',
                     size=9,
                     xy=(xmin, ymax),
                     xytext=(10, -15),
                     textcoords='offset points')
        plt.annotate(grid_obj.best_params_,
                     size=9,
                     xy=(xmin, ymax),
                     xytext=(10, -35),
                     textcoords='offset points',
                     wrap=True)
        plt.title('Predicted prices (EUR) vs. True prices (EUR)')
        plt.show()

    def load_model(self):
        """ load_model - method to load pickle model """
        with open(self.model_filename, "rb") as file:
            model = pickle.load(file)
            return model

    @staticmethod
    def predict(model, prediction_parameters):
        """ predict - method to predict input parameters """
        return model.predict(prediction_parameters)

    def predict_parameters(self, prediction_parameters):
        """ predict_parameters - predict parameters """
        model = self.load_model()
        prediction_result = self.predict(model, prediction_parameters=prediction_parameters)
        return prediction_result
