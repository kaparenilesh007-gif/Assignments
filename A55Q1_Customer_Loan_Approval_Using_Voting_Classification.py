import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import accuracy_score

from sklearn.ensemble import VotingClassifier


border = "_"*65
#-------------------------------------------------------------
# Step 1 : Load the data set
#-------------------------------------------------------------

print(border)
print("Step 1 : Load the data set")
df = pd.read_csv("Customer_Loan_Approval.csv")
print(border)

print("First 5 Smaples from dataset")
print(df.head())
print(border)



#-------------------------------------------------------------
# Step 2 : Check for missing values
#-------------------------------------------------------------

print(border)
print("Step 2 : Check for missing values")
print(border)

print("Missing values per column: ")
print(df.isnull().sum())

print(border)


#-------------------------------------------------------------
# Step 3 : Seperate dataset into features and label
#-------------------------------------------------------------
print(border)
print("Step 3 : Seperate dataset into features and label")
print(border)

X = df.drop("LoanApproved", axis=1)
Y = df["LoanApproved"]
print(border)
print("X shape", X.shape)
print("Y shape", Y.shape)
print(border)


#-------------------------------------------------------------
# Step 4 : spilit dataset
#-------------------------------------------------------------

print(border)
print("Step 4 : spilit dataset")
print(border)
X_train , X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
print(border)


#-------------------------------------------------------------
# Step  : scale the data
#-------------------------------------------------------------
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)
#Y_train = scaler.fit_transform(Y_train)
#Y_test = scaler.fit_transform(Y_test)

#-------------------------------------------------------------
# Step 5 : Train Each model indivisualy
#-------------------------------------------------------------
print(border)
print("Step 5 : Train Each model indivisual")
print(border)

print(border)
print("Train LogisticRegression model")
model_Log = LogisticRegression(max_iter=1000)
model_Log = model_Log.fit(X_train,Y_train)
print("LogisticRegression model trained sucessfully")
print(border)

print("Test the LogisticRegression model")
Y_pred_Log = model_Log.predict(X_test)
print("LogisticRegression model tested sucessfully")
print(border)

print(border)
print("Check Accuracy of LogisticRegression model")
accuracy_Log = accuracy_score(Y_test, Y_pred_Log)
print(f"Accuracy of LogisticRegression model {accuracy_Log}")
print(border)

print(border)
print("Train DecisionTreeClassifier model")
model_DT = DecisionTreeClassifier(random_state=42)
model_DT = model_DT.fit(X_train,Y_train)
print("DecisionTreeClassifier model trained Sucessfully")

print(border)
print("Test DecisionTreeClassifier model")
Y_pred_DT = model_Log.predict(X_test)
print("DecisionTreeClassifier model tested succesfully")

print(border)
print("Check Accuracy of DecisionTreeClassifier model")
accuracy_DT = accuracy_score(Y_test, Y_pred_DT)
print(f"Accuracy of DecisionTreeClassifier model is: {accuracy_DT}")

print(border)
print("Train KNeighborsClassifier model")
model_KNN = KNeighborsClassifier(n_neighbors=5)
model_KNN = model_KNN.fit(X_train,Y_train)
print("KNeighborsClassifier model trained Sucessfully")


print(border)
print("Test KNeighborsClassifier model")
Y_pred_KNN = model_KNN.predict(X_test)
print("KNeighborsClassifier model tested succesfully")

print(border)
print("Check Accuracy of KNeighborsClassifier model")
accuracy_KNN = accuracy_score(Y_test, Y_pred_KNN)
print(f"Accuracy of KNeighborsClassifier model is: {accuracy_KNN}")

#-------------------------------------------------------------
# Step 6  : create Hard voting model
#-------------------------------------------------------------

print(border)
print(" Step 6  : create Hard voting model")
print(border)

model_HardVoting = VotingClassifier(
    estimators=[
    ("Logisti" ,model_Log),
    ("Decision Tree", model_DT),
    ("KNN", model_KNN)
    ],
    voting="hard"
    )

print("Hard Voting Model created  Sucessfully")

print("Train Hard Voting Model ")
model_HardVoting = model_HardVoting.fit(X_train, Y_train)
print("Hard Voting Model trained Sucessfully")

print(border)
print("Test Hard voting model")
Y_pred_HV = model_HardVoting.predict(X_test)
print("Hrd Voting Model tested Sucessfully")

print(border)
print("Check Accuracy of Hard Voting Model")
accuracy_HV = accuracy_score(Y_test, Y_pred_HV)
print(f"Accuracy of Hard Veoting model is: {accuracy_HV}")

#-------------------------------------------------------------
# Step 7  : create soft voting model
#-------------------------------------------------------------

print(border)
print(" Step 7  : create soft voting model")
print(border)

model_softVoting = VotingClassifier(
    estimators=[
    ("Logisti" ,model_Log),
    ("Decision Tree", model_DT),
    ("KNN", model_KNN)
    ],
    voting="soft"
    )
print("soft Voting Model created  Sucessfully")

print("Train soft Voting Model ")
model_softdVoting = model_softVoting.fit(X_train, Y_train)
print("soft Voting Model trained Sucessfully")

print("Test softdVoting model")
Y_pred_SV = model_softVoting.predict(X_test)
print("softdVoting model tested successfully")

print(border)
print("Check Accuracy of soft Voting Model")
accuracy_SV = accuracy_score(Y_test, Y_pred_SV)
print(f"Accuracy of soft Veoting model is: {accuracy_SV}")
print(border)

print(border)
print("Both Accuracy here ")
print(f"Accuracy of LogisticRegression model is:     {accuracy_Log}")
print(f"Accuracy of DecisionTreeClassifier model is: {accuracy_DT}")
print(f"Accuracy of KNeighborsClassifier model is:   {accuracy_KNN}")
print(f"Accuracy of Hard Veoting model is:           {accuracy_HV}")
print(f"Accuracy of soft Veoting model is:           {accuracy_SV}")
print(border)

print(border)
print("------End of Programm-------")
print(border)
