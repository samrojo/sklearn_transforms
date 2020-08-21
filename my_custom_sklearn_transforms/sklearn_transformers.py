from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        
        data["BACKEND_AVGxBEGGINER"] = data['AVG_SCORE_BACKEND']*data['NUM_COURSES_BEGINNER_BACKEND']
        data["FRONTEND_AVGxBEGGINER"] = data['AVG_SCORE_FRONTEND']*data['NUM_COURSES_BEGINNER_FRONTEND']
        #---
        data["AVGBxDHOURS"] = data['AVG_SCORE_BACKEND']*data['HOURS_DATASCIENCE']
        data["AVGBxDBEGGINER"] = data['AVG_SCORE_BACKEND']*data['NUM_COURSES_BEGINNER_DATASCIENCE']
        data["AVGBxDADVANCED"] = data['AVG_SCORE_BACKEND']*data['NUM_COURSES_ADVANCED_DATASCIENCE']
        
        data["AVGBxFHOURS"] = data['AVG_SCORE_BACKEND']*data['HOURS_FRONTEND']
        data["AVGBxFADVANCED"] = data['AVG_SCORE_BACKEND']*data['NUM_COURSES_ADVANCED_FRONTEND']
        
        data["AVGFxDHOURS"] = data['AVG_SCORE_BACKEND']*data['HOURS_DATASCIENCE']
        
        data["AVGFxBHOURS"] = data['AVG_SCORE_FRONTEND']*data['HOURS_BACKEND']
        data["AVGFxBADVANCED"] = data['AVG_SCORE_FRONTEND']*data['NUM_COURSES_ADVANCED_BACKEND']
        #---
        
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
