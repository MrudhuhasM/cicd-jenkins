import pandas as pd
from sklearn.model_selection import train_test_split

from sales_prediction.config.config import DATA_PATH

def load_data():
    data = pd.read_csv(DATA_PATH / "data.csv")
    data.dropna(inplace=True)
    data.drop(['Influencer'],axis=1,inplace=True)
    return data

def split_data(data):
    X = data.drop('Sales', axis=1)
    y = data['Sales']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

