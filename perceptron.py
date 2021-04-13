#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tensorflow as tf
tf.random.set_seed(777) #시드를 설정합니다.

import numpy as np 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.lossess import mse

# 데이터 준비하기
x = np.array([[0,0],[1,0],[0,1],[1,1]])
y = np.array([[0],[1],[1],[1]])

# 모델 구성하기
model = Sequential()

# 단층 퍼셉트론을 구성합니다.
model.add(Dense(1,input_shape = (2, ), activation = 'linear'))

