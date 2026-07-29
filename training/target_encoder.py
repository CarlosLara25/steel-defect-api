from sklearn.preprocessing import LabelEncoder


def fit_label_encoder(y):
    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)

    return encoder, y_encoded