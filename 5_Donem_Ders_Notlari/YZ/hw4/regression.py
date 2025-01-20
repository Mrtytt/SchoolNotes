from numpy import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import KFold

# Standart Eğik Azalması
def gradient_descent(X, y, alpha=0.01, iterations=1000):
    m, n = X.shape
    theta = np.zeros(n)
    for _ in range(iterations):
        gradient = (1/m) * X.T @ (X @ theta - y)
        theta -= alpha * gradient
    return theta

# Düzenlileştirilmiş Eğik Azalması
def regularized_gradient_descent(X, y, alpha=0.01, iterations=1000, lambda_=0.1):
    m, n = X.shape
    theta = np.zeros(n)
    for _ in range(iterations):
        gradient = (1/m) * X.T @ (X @ theta - y) + (lambda_/m) * theta
        theta -= alpha * gradient
    return theta

# Normal Denklem Yöntemi
def normal_equation(X, y, lambda_=0.1):
    m, n = X.shape
    I = np.eye(n)
    I[0, 0] = 0  # Bias terimi düzenlenmez
    theta = np.linalg.inv(X.T @ X + lambda_ * I) @ X.T @ y
    return theta

# Hatayı Hesaplama
def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred)**2)

# Çapraz Doğrulama ve Model Eğitimi
def regression_experiments(points):
    points = np.asarray(points, dtype="object")
    X = np.array([x[0] for x in points])
    y = np.array([x[1] for x in points])
    X = np.c_[np.ones(X.shape[0]), X]  # Bias terimi için birler sütunu ekleyin

    kf = KFold(n_splits=5, random_state=42, shuffle=True)
    results = []

    for fold, (train_index, test_index) in enumerate(kf.split(X)):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        # Standart eğim azalması
        theta_gd = gradient_descent(X_train, y_train)
        y_pred_gd = X_test @ theta_gd
        mse_gd = mean_squared_error(y_test, y_pred_gd)

        # Düzenlileştirilmiş eğim azalması
        theta_rgd = regularized_gradient_descent(X_train, y_train)
        y_pred_rgd = X_test @ theta_rgd
        mse_rgd = mean_squared_error(y_test, y_pred_rgd)

        # Normal denklem
        theta_ne = normal_equation(X_train, y_train)
        y_pred_ne = X_test @ theta_ne
        mse_ne = mean_squared_error(y_test, y_pred_ne)

        results.append({
            "Fold": fold + 1,
            "Gradient Descent MSE": mse_gd,
            "Regularized Gradient Descent MSE": mse_rgd,
            "Normal Equation MSE": mse_ne
        })

        print(f"Fold {fold + 1} Results:")
        print(f"  Gradient Descent MSE: {mse_gd}")
        print(f"  Regularized Gradient Descent MSE: {mse_rgd}")
        print(f"  Normal Equation MSE: {mse_ne}")

    return results

# Veri Yükleme ve Görselleştirme
data = pd.read_csv('C:/Users/Murat Berk/Documents/GitHub/SchoolNotes/5_Donem_Ders_Notlari/YZ/hw4/data_regression.txt')
f1 = data['MAKINA'].values
target = data['KAR_ZARAR'].values

fig = plt.figure()
plt.plot(f1, target, 'rx')
plt.xlabel('Makina')
plt.ylabel('Kar/Zarar')
plt.title('Makina ve Kar/Zarar Dağılımı')
plt.show()

# Veri kümesini düzenle
points = [(f1[i], target[i]) for i in range(len(f1))]

# Modelleri eğit ve sonuçları al
results = regression_experiments(points)

# Sonuçları göster
results_df = pd.DataFrame(results)
print("\nToplam Sonuçlar:")
print(results_df)
