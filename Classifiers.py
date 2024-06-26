pip install dataprep
import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import OrdinalEncoder
from dataprep.eda import create_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score

df=pd.read_csv("/content/diabetes_prediction_dataset.csv")
df.head()

encode=OrdinalEncoder()
df.gender=encode.fit_transform(df[["gender"]])

encode1=OrdinalEncoder()
df.smoking_history=encode1.fit_transform(df[["smoking_history"]])

x=df.drop("diabetes",axis=1)
y=df["diabetes"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25)

def classifiers(x_train,y_train):

  #Decision Tree Classifier
  from sklearn.tree import DecisionTreeClassifier
  model=DecisionTreeClassifier().fit(x_train,y_train)
  y_pred=model.predict(x_test)
  accuracy = accuracy_score(y_test,y_pred)
  print(f"Decision Tree Classifier accuracy score: {accuracy}\n")

  #Random Forest Classifier
  from sklearn.ensemble import RandomForestClassifier
  model1=RandomForestClassifier().fit(x_train,y_train)
  y_pred1=model1.predict(x_test)
  accuracy1 = accuracy_score(y_test,y_pred1)
  print(f"Random Forest Classifier accuracy score: {accuracy1}\n")

  #AdaBoost Classifier
  from sklearn.ensemble import AdaBoostClassifier
  model2=AdaBoostClassifier().fit(x_train,y_train)
  y_pred2=model2.predict(x_test)
  accuracy2 = accuracy_score(y_test,y_pred2)
  print(f"AdaBoost Classifier accuracy score: {accuracy2}\n")

  #SGD Classifier
  from sklearn.linear_model import SGDClassifier
  model3=SGDClassifier().fit(x_train,y_train)
  y_pred3=model3.predict(x_test)
  accuracy3 = accuracy_score(y_test,y_pred3)
  print(f"SGD Classifier accuracy score: {accuracy3}\n")

  #Support Vector Machines
  from sklearn import svm
  model4=svm.SVC().fit(x_train,y_train)
  y_pred4=model4.predict(x_test)
  accuracy4 = accuracy_score(y_test,y_pred4)
  print(f"Support Vector Machines accuracy score: {accuracy4}\n")

  #Nearest Neighbors
  from sklearn.neighbors import NearestCentroid
  model5=NearestCentroid().fit(x_train,y_train)
  y_pred5=model5.predict(x_test)
  accuracy5 = accuracy_score(y_test,y_pred5)
  print(f"Nearest Neighbors accuracy score: {accuracy5}\n")

  #KNeighbors Classifier
  from sklearn.neighbors import KNeighborsClassifier
  model6=KNeighborsClassifier().fit(x_train,y_train)
  y_pred6=model6.predict(x_test)
  accuracy6 = accuracy_score(y_test,y_pred6)
  print(f"KNeighbors Classifier accuracy score: {accuracy6}\n")

  #Neural network models
  from sklearn.neural_network import MLPClassifier
  model7=MLPClassifier().fit(x_train,y_train)
  y_pred7=model7.predict(x_test)
  accuracy7 = accuracy_score(y_test,y_pred7)
  print(f"Neural network models accuracy score: {accuracy7}\n")

  #Gradient Boosting Classifier
  from sklearn.ensemble import GradientBoostingClassifier
  model8=GradientBoostingClassifier().fit(x_train,y_train)
  y_pred8=model8.predict(x_test)
  accuracy8 = accuracy_score(y_test,y_pred8)
  print(f"Gradient Boosting Classifier accuracy score: {accuracy8}\n")

  #Naive Bayes
  from sklearn.naive_bayes import GaussianNB
  model9=GaussianNB().fit(x_train,y_train)
  y_pred9=model9.predict(x_test)
  accuracy9 = accuracy_score(y_test,y_pred9)
  print(f"Naive Bayes accuracy score: {accuracy9}\n")

