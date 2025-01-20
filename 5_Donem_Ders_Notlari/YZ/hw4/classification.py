from numpy import *
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, accuracy_score
import scipy.io

# Veri yükleme ve görselleştirme
data = scipy.io.loadmat('C:/Users/Murat Berk/Documents/GitHub/SchoolNotes/5_Donem_Ders_Notlari/YZ/hw4/data_classification.mat')
features = np.asarray(data['features'])
labels = np.asarray(data['classes']).ravel()

# Veri görselleştirme
data_zeros = features[labels == 0]
data_ones = features[labels == 1]
plt.scatter(data_zeros[:, 0], data_zeros[:, 1], color='magenta', label='Sınıf 0')
plt.scatter(data_ones[:, 0], data_ones[:, 1], color='green', label='Sınıf 1')
plt.xlabel('Özellik 1')
plt.ylabel('Özellik 2')
plt.legend()
plt.show()

# Çapraz doğrulama ve düzenli eğim azalışı ile lojistik regresyon
kf = KFold(n_splits=5, random_state=42, shuffle=True)

# PCA ve LDA uygulama fonksiyonları
def apply_pca(data, n_components):
    pca = PCA(n_components=n_components)
    return pca.fit_transform(data)

def apply_lda(data, labels, n_components):
    lda = LDA(n_components=n_components)
    return lda.fit_transform(data, labels)

# Model eğitimi ve değerlendirme
def train_and_evaluate(X, y, kf):
    f1_scores = []
    accuracies = []
    
    for train_index, test_index in kf.split(X):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        model = LogisticRegression(penalty='l2', solver='lbfgs', max_iter=1000)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        f1_scores.append(f1_score(y_test, y_pred))
        accuracies.append(accuracy_score(y_test, y_pred))

    return np.mean(f1_scores), np.mean(accuracies)

# Deneyler
datasets = {
    'Original': features,
    'PCA': apply_pca(features, n_components=1),
    'LDA': apply_lda(features, labels, n_components=1)
}

results = {}
for name, dataset in datasets.items():
    f1, acc = train_and_evaluate(dataset, labels, kf)
    results[name] = {'F1 Score': f1, 'Accuracy': acc}

# Sonuçları yazdırma
for name, metrics in results.items():
    print(f"{name} Dataset:")
    print(f"  F1 Score: {metrics['F1 Score']:.4f}")
    print(f"  Accuracy: {metrics['Accuracy']:.4f}\n")
