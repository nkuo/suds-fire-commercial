{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf470
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 ##Other models\
\
samples = np.array([0.1 if i == 0 else 1.2 for i in y_train])\
\
model = RandomForestClassifier(n_estimators=500)\
model.fit(X_train, y_train)\
pred = model.predict(X_test)\
real = y_test\
cm = confusion_matrix(real, pred)\
print confusion_matrix(real, pred)\
\
from sklearn.metrics import cohen_kappa_score\
kappa = cohen_kappa_score(real, pred)\
\
fpr, tpr, thresholds = metrics.roc_curve(y_test, pred, pos_label=1)\
\
print 'Accuracy = ', float(cm[0][0] + cm[1][1])/len(real)\
print 'kappa score = ', kappa\
print 'AUC Score = ', metrics.auc(fpr, tpr)\
print 'recall = ',tpr[1]\
print 'precision = ',float(cm[1][1])/(cm[1][1]+cm[0][1])\
\
\
model = linear_model.LogisticRegression(C=1e5)\
model.fit(X_train, y_train,sample_weight = samples)\
pred = model.predict(X_test)\
real = y_test\
cm = confusion_matrix(real, pred)\
print confusion_matrix(real, pred)\
\
from sklearn.metrics import cohen_kappa_score\
kappa = cohen_kappa_score(real, pred)\
\
fpr, tpr, thresholds = metrics.roc_curve(y_test, pred, pos_label=1)\
\
print 'Accuracy = ', float(cm[0][0] + cm[1][1])/len(real)\
print 'kappa score = ', kappa\
print 'AUC Score = ', metrics.auc(fpr, tpr)\
print 'recall = ',tpr[1]\
print 'precision = ',float(cm[1][1])/(cm[1][1]+cm[0][1])\
\
from sklearn.ensemble import AdaBoostClassifier\
from sklearn.tree import DecisionTreeClassifier\
\
model = AdaBoostClassifier(\
        DecisionTreeClassifier(max_depth=2),\
        n_estimators=600,\
        learning_rate=1.5,\
        algorithm="SAMME")\
model.fit(X_train, y_train)\
pred = model.predict(X_test)\
real = y_test\
cm = confusion_matrix(real, pred)\
print confusion_matrix(real, pred)\
\
from sklearn.metrics import cohen_kappa_score\
kappa = cohen_kappa_score(real, pred)\
\
fpr, tpr, thresholds = metrics.roc_curve(y_test, pred, pos_label=1)\
\
print 'Accuracy = ', float(cm[0][0] + cm[1][1])/len(real)\
print 'kappa score = ', kappa\
print 'AUC Score = ', metrics.auc(fpr, tpr)\
print 'recall = ',tpr[1]\
print 'precision = ',float(cm[1][1])/(cm[1][1]+cm[0][1])\
\
from sklearn import svm\
\
model = svm.SVC(kernel='linear', C = 1.0)\
\
model.fit(X_train, y_train)\
pred = model.predict(X_test)\
real = y_test\
cm = confusion_matrix(real, pred)\
print confusion_matrix(real, pred)\
\
from sklearn.metrics import cohen_kappa_score\
kappa = cohen_kappa_score(real, pred)\
\
fpr, tpr, thresholds = metrics.roc_curve(y_test, pred, pos_label=1)\
\
print 'Accuracy = ', float(cm[0][0] + cm[1][1])/len(real)\
print 'kappa score = ', kappa\
print 'AUC Score = ', metrics.auc(fpr, tpr)\
print 'recall = ',tpr[1]\
print 'precision = ',float(cm[1][1])/(cm[1][1]+cm[0][1])}