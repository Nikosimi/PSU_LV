import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, precision_score, recall_score, accuracy_score, classification_report

df = pd.read_csv('occupancy_processed.csv')

feature_names = ['S3_Temp', 'S5_CO2']
target_name = 'Room_Occupancy_Count'
class_names = ['Slobodna', 'Zauzeta']

X = df[feature_names].to_numpy()
y = df[target_name].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

y_pred = knn.predict(X_test_scaled)

cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["0", "1"])
disp.plot(cmap=plt.cm.Blues)
plt.title('Confusion Matrix KNN')
plt.show()

accuracy = accuracy_score(y_test, y_pred)
print("Točnost: ", accuracy)

print("Preciznost i odziv po klasama:\n",classification_report(y_test, y_pred))

for k in [1, 2, 3, 4, 10, 15, 20, 25]:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train_scaled, y_train)
    y_pred_k = model.predict(X_test_scaled)
    print("k: ", k)
    print(classification_report(y_test, y_pred_k))

knn_not_scaled = KNeighborsClassifier(n_neighbors=5)
knn_not_scaled.fit(X_train, y_train)
y_pred_not_scaled = knn_not_scaled.predict(X_test)
print("Bez skaliranja\n",classification_report(y_test, y_pred_not_scaled))


