import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, AdaBoostClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score, precision_score, recall_score,f1_score, confusion_matrix

from sklearn.metrics import accuracy_score

from sklearn.ensemble import VotingClassifier


border = "_"*65
#-------------------------------------------------------------
# Step 1 : Load the data set
#-------------------------------------------------------------

print(border)
print("Step 1 : Load the data set")
df = pd.read_csv("Fraudulent_Transaction_Detection.csv")
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

X = df.drop("Fraud", axis=1)
Y = df["Fraud"]
print(border)
print("X shape", X.shape)
print("Y shape", Y.shape)
print(border)


#-------------------------------------------------------------
# Step 4 : split dataset
#-------------------------------------------------------------

print(border)
print("Step 4 : spilit dataset")
print(border)
X_train , X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
print(border)
"""
#-------------------------------------------------------------
# Step 5 : scale the dataset
#-------------------------------------------------------------
Scaler = StandardScaler()
X_train = Scaler.fit_transform(X_train)
X_test = Scaler.fit_transform(X_train)

"""
#-------------------------------------------------------------
# Step 5 : model DecisionTreeClassifier
#-------------------------------------------------------------
print(border)

model_DT = DecisionTreeClassifier(random_state=42)
model_DT = model_DT.fit(X_train,Y_train)

Y_pred_DT = model_DT.predict(X_test)

print(Y_pred_DT)


Accuracy_DT = accuracy_score(Y_test,Y_pred_DT)
print(f" Accuracy of DecisionTreeClassifier model is : {Accuracy_DT}")
print(border)

Precision_DT = precision_score(Y_test,Y_pred_DT)
print(f" precision score of DecisionTreeClassifier model is : {Precision_DT}")
print(border)

Recall_DT = recall_score(Y_test,Y_pred_DT)
print(f" recall score of DecisionTreeClassifier model is : {Recall_DT}")
print(border)

F1_score_DT = f1_score(Y_test,Y_pred_DT)
print(f" F1 score of DecisionTreeClassifier model is : {F1_score_DT}")
print(border)

ConfussionMatrix_DT = confusion_matrix(Y_test,Y_pred_DT)
print(f" ConfussionMatrix of DecisionTreeClassifier model is : {ConfussionMatrix_DT}")

print(border)

print("MSE :",mean_squared_error(Y_test, Y_pred_DT))
print("R2: ",r2_score(Y_test, Y_pred_DT))

print(border)

#-------------------------------------------------------------
# Step 6 : model BaggingClassifier
#-------------------------------------------------------------
model_bagg = BaggingClassifier(
    estimator= model_DT,
    n_estimators=10,
    random_state=42
)

model_bagg = model_bagg.fit(X_train,Y_train)

Y_pred_bagg = model_bagg.predict(X_test)

Accuracy_bagg = accuracy_score(Y_test,Y_pred_DT)
print(f" Accuracy of BaggingClassifier model is : {Accuracy_bagg}")
print(border)

Precision_bagg = precision_score(Y_test,Y_pred_bagg)
print(f" precision score of BaggingClassifier model is : {Precision_bagg}")
print(border)

Recall_bagg = recall_score(Y_test,Y_pred_bagg)
print(f" Recall score of BaggingClassifier model is : {Recall_bagg}")
print(border)

F1_score_bagg = f1_score(Y_test,Y_pred_bagg)
print(f" F1_score of BaggingClassifier model is : {F1_score_bagg}")
print(border)

ConfussionMatrix_bagg = confusion_matrix(Y_test,Y_pred_bagg)
print(f" ConfussionMatrix of BaggingClassifier model is : {ConfussionMatrix_bagg}")

print("MSE :",mean_squared_error(Y_test, Y_pred_bagg))
print("R2: ",r2_score(Y_test, Y_pred_bagg))

print(border)

#-------------------------------------------------------------
# Step 7 : model Boosting Classifier
#-------------------------------------------------------------
model_boost = AdaBoostClassifier(
    n_estimators=50,
    learning_rate=1,
    random_state=42
)

model_boost = model_boost.fit(X_train,Y_train)

Y_pred_boost = model_boost.predict(X_test)

Accuracy_boost = accuracy_score(Y_test,Y_pred_boost)
print(f" Accuracy of AdaBoostClassifier model is : {Accuracy_boost}")
print(border)

Precision_boost = precision_score(Y_test,Y_pred_boost)
print(f" precision score of AdaBoostClassifier model is : {Precision_boost}")
print(border)

Recall_boost = recall_score(Y_test,Y_pred_boost)
print(f" Recall score of AdaBoostClassifier model is : {Recall_boost}")
print(border)

F1_score_boost = f1_score(Y_test,Y_pred_boost)
print(f" F1_score of AdaBoostClassifier model is : {F1_score_boost}")
print(border)

ConfussionMatrix_boost = confusion_matrix(Y_test,Y_pred_boost)
print(f" ConfussionMatrix of AdaBoostClassifier model is : {ConfussionMatrix_boost}")


print("MSE :",mean_squared_error(Y_test, Y_pred_boost))
print("R2: ",r2_score(Y_test, Y_pred_boost))

print(border)
#-------------------------------------------------------------
# Step 8 : RandomForestClassifier
#-------------------------------------------------------------
model_RFC = RandomForestClassifier(
    n_estimators=10,
    random_state=42
)
model_RFC = model_RFC.fit(X_train,Y_train)

Y_pred_RFC = model_RFC.predict(X_test)

Accuracy_RFC = accuracy_score(Y_test,Y_pred_RFC)
print(f" Accuracy of RandomForestClassifier model is : {Accuracy_RFC}")
print(border)

Precision_RFC = precision_score(Y_test,Y_pred_RFC)
print(f" precision score of RandomForestClassifier model is : {Precision_RFC}")
print(border)

Recall_RFC = recall_score(Y_test,Y_pred_RFC)
print(f" Recall score of RandomForestClassifier model is : {Recall_RFC}")
print(border)

F1_score_RFC = f1_score(Y_test,Y_pred_RFC)
print(f" F1_score of RandomForestClassifier model is : {F1_score_RFC}")
print(border)

ConfussionMatrix_RFC = confusion_matrix(Y_test,Y_pred_RFC)
print(f" ConfussionMatrix of RandomForestClassifier model is : {ConfussionMatrix_RFC}")

print("MSE :",mean_squared_error(Y_test, Y_pred_RFC))
print("R2: ",r2_score(Y_test, Y_pred_RFC))



model_softVoting = VotingClassifier(
    estimators=[
    ("RandomForest" ,model_RFC),
    ("Decision Tree",model_DT ),
    ("Bagging model",model_bagg ),
    ("Boosting model",model_boost)
    ],
    voting="soft"
    )

print("Train soft Voting Model ")
model_softdVoting = model_softVoting.fit(X_train, Y_train)
print("soft Voting Model trained Sucessfully")

print("Test softdVoting model")
Y_pred_SV = model_softVoting.predict(X_test)
print("softdVoting model tested successfully")

print(border)
print("Check Accuracy of soft Voting Model")
accuracy_SV = accuracy_score(Y_test, Y_pred_SV)
print(f"Accuracy of soft Voting model is: {accuracy_SV}")
print(border)


Precision_SV = precision_score(Y_test,Y_pred_SV)
print(f" precision score of soft votting model is : {Precision_SV}")
print(border)

Recall_SV = recall_score(Y_test,Y_pred_SV)
print(f" Recall score of soft votting model is : {Recall_SV}")
print(border)

F1_score_SV = f1_score(Y_test,Y_pred_SV)
print(f" F1_score of soft votting model is : {F1_score_SV}")
print(border)

ConfussionMatrix_SV = confusion_matrix(Y_test,Y_pred_SV)
print(f" ConfussionMatrix of soft votting model is : {ConfussionMatrix_SV}")

print("MSE :",mean_squared_error(Y_test, Y_pred_SV))
print("R2: ",r2_score(Y_test, Y_pred_SV))

print("Algoritham          Accuracy           Precision           Recall           F1Score")
print(f"Decision Tree      {Accuracy_DT} |    {Precision_DT} |    {Recall_DT} |    {F1_score_DT}")
print(f"Bagging            {Accuracy_bagg} |  {Precision_bagg} |  {Recall_bagg} |  {F1_score_bagg}")
print(f"AdaBoost           {Accuracy_boost} | {Precision_boost} | {Recall_boost} | {F1_score_boost}")
print(f"Random Forect      {Accuracy_RFC} |   {Precision_RFC} |   {Recall_RFC} |   {F1_score_RFC}")
print(f"voting             {accuracy_SV} |    {Precision_SV} |    {Recall_SV} |    {F1_score_SV}")


print(border)
print("------End of Programm-------")
print(border)
