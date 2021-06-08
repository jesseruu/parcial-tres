from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score 
from sklearn.naive_bayes import GaussianNB
import pandas as pd

def importar_dataset():
    universalBank = pd.read_csv('dataset/UniversalBank.csv')
    X = universalBank.drop(['Personal Loan'], axis=1)
    y = universalBank['Personal Loan']

    return X, y

def naive_bayes():

    X, y = importar_dataset()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    naive_bayesM = GaussianNB()
    naive_bayesM.fit(X_train, y_train)

    y_pred = naive_bayesM.predict(X_test)

    precision = accuracy_score(y_test, y_pred)
    print("La precision del modelo es:", precision)

if __name__ == "__main__":
    naive_bayes()