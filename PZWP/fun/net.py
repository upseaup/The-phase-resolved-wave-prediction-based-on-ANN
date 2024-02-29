import tensorflow as tf
from tensorflow import keras as ks
import abc


def activation_fun(act_fun):
    if act_fun == 'relu':
        function = tf.nn.relu
    elif act_fun == "elu":
        function = tf.nn.elu

    else:
        print('the activate fun is wrong')
        print('act_fun')
        function = 0
    return function


class Mlp(ks.Model):
    # Initialize MLP (ANN) structure with mlp_list
    def __init__(self, mlp_list, act_fun='relu', name='mlp', w_init=tf.random_normal_initializer,
                 b_init=tf.zeros_initializer()):
        super(Mlp, self).__init__()
        self.mlp_list = mlp_list
        self.net_len = len(mlp_list)

        self.name_ = name
        self.w_dict = dict()
        self.b_dict = dict()

        # select activation
        self.act_fun = activation_fun(act_fun)

        # net_len = int(len(mlp_list))
        for i in range(self.net_len - 1):
            self.w_dict[self.name_ + '_w_%d' % (i + 1)] = tf.Variable(
                initial_value=w_init(seed=i)(shape=(self.mlp_list[i], self.mlp_list[i + 1]),
                                             dtype='float32', ),
                trainable=True,
                name=self.name_ + '_w_%d' % (i + 1))
            self.b_dict[self.name_ + '_b_%d' % (i + 1)] = tf.Variable(
                initial_value=b_init(shape=[self.mlp_list[i + 1], ],
                                     dtype='float32'),
                trainable=True,
                name=self.name_ + '_b_%d' % (i + 1))
        # print(mlp_list)

    def call(self, inputs):
        x = inputs

        for i in range(self.net_len - 2):  # 处理最后一层不用relu
            x = self.act_fun(
                tf.matmul(x, self.w_dict[self.name_ + '_w_%d' % (i + 1)]) + self.b_dict[self.name_ + '_b_%d' % (i + 1)])

        y = tf.matmul(x, self.w_dict[self.name_ + '_w_%d' % (self.net_len - 1)]) + self.b_dict[
            self.name_ + '_b_%d' % (self.net_len - 1)]
        return y
