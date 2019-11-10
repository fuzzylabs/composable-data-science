from sklearn.model_selection import train_test_split

def select_features(training_data):
    y = training_data.SalePrice
    features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

    X = training_data[features]
    return train_test_split(X, y, random_state=1)
