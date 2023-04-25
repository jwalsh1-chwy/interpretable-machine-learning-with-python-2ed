#!/usr/bin/env python

"""
This script demonstrates various properties such as Fidelity, Accuracy, Comprehensibility, Degree of Importance, 
and more using the SHAP (SHapley Additive exPlanations) method to explain predictions of an Support Vector Machine 
(SVM) model trained on the Breast Cancer dataset. 

The script also demonstrates the use of the waterfall plot to visualize the SHAP values for a specific instance.
"""

import shap
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


def load_data():
    """Loads Breast Cancer dataset and return the feature matrix and target labels."""
    data = load_breast_cancer()
    X, y = data.data, data.target
    return X, y


def split_data(X, y):
    """Split data into training and test sets."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    return X_train, X_test, y_train, y_test


def train_model(X_train, y_train):
    """Train an SVM classifier on the training data."""
    clf = SVC(kernel="linear", probability=True, random_state=42)
    clf.fit(X_train, y_train)
    return clf


def predict(clf, X_test):
    """Predict on test set."""
    y_pred = clf.predict(X_test)
    y_pred_proba = clf.predict_proba(X_test)
    return y_pred, y_pred_proba


def evaluate(y_test, y_pred):
    """Evaluate the accuracy of the model"""
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy


def explain_predictions(clf, X_train, X_test):
    """Use SHAP method to explain predictions of an SVM model."""
    explainer = shap.Explainer(clf, X_train)
    shap_values = explainer(X_test)
    return shap_values


if __name__ == "__main__":
    X, y = load_data()
    X_train, X_test, y_train, y_test = split_data(X, y)
    clf = train_model(X_train, y_train)
    y_pred, y_pred_proba = predict(clf, X_test)
    accuracy = evaluate(y_test, y_pred)
    print("Accuracy of the SVM model:", accuracy)
    shap_values = explain_predictions(clf, X_train, X_test)
    shap.plots.waterfall(shap_values[0])
