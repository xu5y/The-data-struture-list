from numpy import *


class Perception:
    def __init__(self, alpha=0.01, n_iter=60):  # 学习率和迭代次数
        self.alpha = alpha
        self.n_iter = n_iter

    def train(self, data, label):  # x为输入的训练数据，Y为标签
        m, n = shape(data)  # 得到训练样本的数量和特征的数量
        self.b=0
        self.w = mat(ones((n, 1)))
        # 训练
        for i in range(self.n_iter):
            for x, y in zip(data, label):  # 得到i个（x,y)的元组
                f = float(self.w * x) + self.b

                if f * y < 0:
                    self.b += self.alpha * y
                    self.w += x.T * self.alpha * y

            # 提早停止标准

            if self.loss(data, label) == 0:
                return i

    def loss(self, X, Y):
        sum_loss = 0
        for x, y in zip(X, Y):
            f = float(self.w * x) + self.b
            sum_loss += -(f * y)
        return sum_loss
