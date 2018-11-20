import numpy as np


def generateY_0():
    IB = np.kron(np.identity(W + 1), b)
    y_0 = np.matrix([[0 for __ in range((W + 1) * (M + 1))] for _ in range((W + 1) * (M + 1))])
    y_0[0:W + 1, W + 1:(W + 1) * (M + 1)] = IB
    return y_0


def generateY_1():
    E = np.ones(M)
    S_0 = np.dot(-S, E)
    kron_sum = np.kron(D_0, np.identity(M)) + np.kron(np.identity(W + 1), S)
    diag = kron_sum.diagonal()
    R = np.diagflat(np.absolute(diag))
    y_21 = np.dot(np.linalg.inv(R), np.transpose(np.kron(np.identity(W + 1), S_0)))
    tmp = np.dot(np.linalg.inv(R), kron_sum)
    y_22 = tmp + np.identity(tmp.shape[0])

    y_1 = np.matrix([[0 for __ in range((W + 1) * (M + 1))] for _ in range((W + 1) * (M + 1))])
    y_1[W + 1:(W + 1) * (M + 1), 0:W + 1] = y_21  # тут поменять надо
    y_1[W + 1:(W + 1) * (M + 1), W + 1:(W + 1) * (M + 1)] = y_22
    return y_1


def generateY_2():
    y_2 = np.matrix([[0 for __ in range((W + 1) * (M + 1))] for _ in range((W + 1) * (M + 1))])
    kron_sum = np.kron(D_0, np.identity(M)) + np.kron(np.identity(W + 1), S)
    diag = kron_sum.diagonal()
    R = np.diagflat(np.absolute(diag))
    y_22 = np.dot(np.linalg.inv(R), np.kron(D_1, np.identity(M)))
    y_2[W + 1:(W + 1) * (M + 1), W + 1:(W + 1) * (M + 1)] = y_22
    return y_2


def R_operator(matrix):
    diag = matrix.diagonal()
    return np.linalg.inv(np.diagflat(np.absolute(diag)))


if __name__ == '__main__':
    print('Hello! Please, enter W')
    W = int(input())
    D_0 = np.matrix([[0 for __ in range(W + 1)] for _ in range(W + 1)])
    D_1 = np.matrix([[0 for __ in range(W + 1)] for _ in range(W + 1)])

    print('Please, enter matrix elements')
    D_0 = np.matrix([[-8, 1], [1, -11]])
    D_1 = np.matrix([[2, 5], [4, 6]])

    # for i in range(W + 1):
    #     D_0[i] = [float(j) for j in input().split()]
    # for i in range(W + 1):
    #     D_1[i] = [float(j) for j in input().split()]
    print('Please, enter M')
    M = int(input())
    print('Enter b')
    b = np.array([float(i) for i in input().split()])
    print('Enter S')
    S = np.matrix([[0 for _ in range(M + 1)] for __ in range(M + 1)])

    S = np.matrix([[-30., 0.], [30., -30.]])

    # for i in range(M + 1):
    #     S[i] = [float(i) for i in input().split()]
    # e_g, e_f = [float(i) for i in input().split()]

    Y_0 = generateY_0()
    Y_1 = generateY_1()
    Y_2 = generateY_2()
    print(Y_0, Y_1, Y_2)
