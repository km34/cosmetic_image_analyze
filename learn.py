import numpy as np
import pandas as pd
from pathlib import Path
from tqdm import tqdm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

path = f'./img/features.csv'
with open(path, 'r') as f:
    data = pd.read_csv(f)

# label以外
X = data.iloc[:, 1:].values

# labelのとこ
y = data.iloc[:, 0].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=1, stratify=y)

param_grid = {
    "criterion": ["gini", "entropy"],
    'n_estimators': [25, 50, 100, 500, 1000]
}
gs = GridSearchCV(
    estimator=RandomForestClassifier(random_state=1),
    param_grid=param_grid,
    scoring='accuracy',
    cv=10,
    n_jobs=-1
)
gs.fit(X_train, y_train)
print('グリッドサーチの最適なスコア')
print('最適なパラメータ', gs.best_params_)
clf = gs.best_estimator_

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print('feature')
print(accuracy_score(y_true=y_test, y_pred=y_pred))
