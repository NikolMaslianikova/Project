import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Функція для візуалізації результатів регресії
def plot_regression_results(y_test, y_pred):
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_pred, color='blue')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], linestyle='--', color='red')
    plt.xlabel('Y тестові')
    plt.ylabel('Y передбачені')
    plt.title('Результати лінійної регресії')
    # plt.show()

# Функція для обчислення MSE
def calculate_mse(X, a, y):
    y_pred = X.dot(a)
    return np.sum((y - y_pred) ** 2) / len(y_pred)

# Функція для реалізації градієнтного спуску
def gradient_descent(X, a, y, lambda_val=None, regularization=None):
    y_pred = X.dot(a)
    grad = 2/len(X) * X.T.dot(y_pred - y)
    if regularization == 'L1':
        l1_grad = lambda_val * np.sign(a)
        grad += l1_grad
    elif regularization == 'L2':
        l2_grad = 2 * lambda_val * a
        grad += l2_grad
    return grad

# Функція для тестування моделі
def test_model(X_test, y_test, n_iterations, feature_names, lambda_val=None, regularization=None):
    a = np.zeros(X_test.shape[1])
    beta = 0.01
    eps = 1e-6
    mse = 0
    iterations = 0
    start_time = time.time()

    for i in range(n_iterations):
        grad = gradient_descent(X_test, a, y_test, lambda_val, regularization)
        new_a = a - beta * grad
        mse = calculate_mse(X_test, new_a, y_test)

        if np.linalg.norm(new_a - a, ord=2) < eps:
            print('Збіжність досягнута після', i + 1, 'ітерацій.')
            print('---------------------------------------')
            break
        a = new_a
        iterations += 1

    y_pred = X_test.dot(a)
    end_time = time.time()
    execution_time = end_time - start_time

    rmse = np.sqrt(mse)
    r_squared = 1 - (np.sum((y_test - y_pred) ** 2) / np.sum((y_test - np.mean(y_test)) ** 2))

    print('Коефіцієнти лінійної регресії:')
    for j, col in enumerate(feature_names):
        print(f"{col} = {a[j]}")
    print('---------------------------------------')
    print('MSE:', mse)
    print('R^2:', r_squared)
    print("Час виконання (секунди):", execution_time)
    print("Кількість ітерацій:", iterations)
    plot_regression_results(y_test, y_pred)
    print("\n\n\n")

# Завантаження даних
data_path = "/Users/nikmas/Desktop/Advertising Budget and Sales.csv"
data = pd.read_csv(data_path)
data.columns = ['Unnamed: 0', 'TV Ad Budget ($)', 'Radio Ad Budget ($)', 'Newspaper Ad Budget ($)', 'Sales ($)']

# Розподіл даних на тренувальну і тестову вибірки

train_data, test_data = train_test_split(data, test_size=0.4, random_state=42)

X_train = train_data[['TV Ad Budget ($)', 'Radio Ad Budget ($)', 'Newspaper Ad Budget ($)']]
y_train = train_data['Sales ($)']

X_test = test_data[['TV Ad Budget ($)', 'Radio Ad Budget ($)', 'Newspaper Ad Budget ($)']]
y_test = test_data['Sales ($)']

# Зберігання назв стовпців перед масштабуванням
feature_names = X_train.columns

# Стандартизація даних
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Додавання стовпця одиниць для вільного члена
X_train_scaled = np.c_[np.ones(X_train_scaled.shape[0]), X_train_scaled]
X_test_scaled = np.c_[np.ones(X_test_scaled.shape[0]), X_test_scaled]

# Додавання назви для вільного члена
feature_names = ['Intercept'] + list(feature_names)

n_iterations = 10000
lambda_val = 0.1

# Без регуляризації
print("Без регуляризації:")
test_model(X_test_scaled, y_test, n_iterations, feature_names)

# L1 регуляризація
print("L1 регуляризація:")
test_model(X_test_scaled, y_test, n_iterations, feature_names, lambda_val, regularization='L1')

# L2 регуляризація
print("L2 регуляризація:")
test_model(X_test_scaled, y_test, n_iterations, feature_names, lambda_val, regularization='L2')


