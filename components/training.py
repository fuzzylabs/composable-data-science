from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

def fit(train_X, train_y):
    rf_model = RandomForestRegressor(random_state=1, n_estimators=10)
    rf_model.fit(train_X, train_y)
    return rf_model

def validate(model, val_X, val_y):
    rf_val_predictions = model.predict(val_X)
    return mean_absolute_error(rf_val_predictions, val_y)
