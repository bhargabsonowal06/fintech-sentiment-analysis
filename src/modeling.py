from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report


def train_svm(X_train, y_train):
    model = LinearSVC(class_weight="balanced")
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions)

    return accuracy, report