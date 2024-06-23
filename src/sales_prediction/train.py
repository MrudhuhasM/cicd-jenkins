from sales_prediction.data_handling import load_data, split_data

from sklearn.linear_model import LinearRegression
import joblib
from sales_prediction.config.config import MODEL_PATH

def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


def main():
    print("Loading data...")
    data = load_data()
    X_train, X_test, y_train, y_test = split_data(data)
    print("Training model...")
    model = train_model(X_train, y_train)
    print("Model trained. Saving model...")
    MODEL_PATH.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH / "model.pkl")
    print("Model saved. in ", MODEL_PATH / "model.pkl")

if __name__ == "__main__":
    main()


