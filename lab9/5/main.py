import numpy as np
from scipy.linalg import inv, det
from scipy.stats import multivariate_normal


def logpdf_custom(X, m, C):
    N, D = X.shape

    C_inv = inv(C)
    log_det_C = np.log(det(C))

    logpdf_values = []
    for i in range(N):
        x = X[i]
        diff = x - m
        logpdf = -0.5 * (log_det_C + np.dot(diff.T, np.dot(C_inv, diff)) + D * np.log(2 * np.pi))
        logpdf_values.append(logpdf)
    
    return np.array(logpdf_values)


N, D = 1000, 5
np.random.seed(0)
X = np.random.randn(N, D)
m = np.zeros(D)
C = np.eye(D)

logpdf_custom_values = logpdf_custom(X, m, C)

logpdf_scipy_values = multivariate_normal(m, C).logpdf(X)


print("Максимальное отклонение: ", np.max(np.abs(logpdf_custom_values - logpdf_scipy_values)))


import time

start_time = time.time()
logpdf_custom(X, m, C)
custom_duration = time.time() - start_time

start_time = time.time()
multivariate_normal(m, C).logpdf(X)
scipy_duration = time.time() - start_time

print(f"Время работы (custom): {custom_duration:.6f} секунд")
print(f"Время работы (scipy): {scipy_duration:.6f} секунд")
