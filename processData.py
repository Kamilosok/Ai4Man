import pyodbc
import random
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

counter = 0
X_train = []
X_test = []
Y_train = []
logreg = LogisticRegression(solver = 'liblinear')
file = open("F:\Git\Ai4Man\Database\Y_train.txt")
#As this is not a professional project I will train the model on 200 of the first messages

if __name__ == "__main__":
    conn = pyodbc.connect(
        r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=F:\Git\Ai4Man\Database\Logs.accdb;')
    cursor = conn.cursor()
    fetched_data = cursor.execute('select Author, Message from Messages')

    datay = [list(rows) for rows in fetched_data]

    for row in datay:
        if(counter<=200):
            X_train.append(datay[counter][1])
            Y_train.append(int(file.readline()))
        else:
            X_test.append(datay[counter][1])
        counter+=1


    data = pd.DataFrame(X_train)
    db = pd.get_dummies(data)
    data2 = pd.DataFrame(X_test)
    db2 = pd.get_dummies(data2)
    Xjoker = logreg.fit(db, Y_train)
    not_existing_cols = [c for c in X_test if c not in db]
    Xjoker = Xjoker.reindex(Xjoker.columns.tolist() + not_existing_cols, axis=1)
    y_pred = logreg.predict(db2)
    #Does not work, ValueError: X has 36925 features, but LogisticRegression is expecting 161 features as input.
    #Idk how to fix it and still do it in a way that I understand

    for i in range(len(X_train)):
        print(X_train[0])
        print(y_pred[0])
        print("###########################")



