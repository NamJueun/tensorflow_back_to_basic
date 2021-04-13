#!/usr/bin/env python
# coding: utf-8

# In[4]:


# 필요 모듈을 임포트합니다.
import tensorflow as tf
import numpy as np

@tf.function 
def square_pos(x):
    if x > 0:
        x  = x * x
    else:
        x = x * -1
    return x

print(square_pos(tf.constant(2)))


# In[ ]:




