import tensorflow as tf
xData = [1,2,3,4,5,6,7] #하루 노동시간
yData = [25000,55000,75000,110000,128000,155000,180000] # 하루 매출량
# 가설 기울기
W = tf.Variable(tf.random_uniform([1],-100,100))    # w = 가중치(weight)
b = tf.Variable(tf.random_uniform([1],-100,100))    #b = bias(편항) 
x = tf.placeholder(tf.float32)
t = tf.placeholder(tf.float32) 
# 위에서 틀 만들어서
# 밑에서 가설 만듬
H = W * x + b
# 비용함수
cost =tf.reduce_mean(tf.square(H-Y)) # (예측값 - 실제값)을 제곱, reduce_mean -> 평균값
# 얼만큼 점프하는 지 템포
a = tf.Variable(0.01)
optimizer = tf.train.GrandientDescentOptimizer(a)  #GrandientDescentOptimizer -> 경사하강 라이브러리
train = optimizer.minimize(cost)

init = tf.global_variables_initializer() # 변수 초기화
sess = tf.Session()
sess.run(init)


# 학습 진행
for i in range(5001):
    sess.run(train, feed_dict = {X: xData, Y:yData})
    if i % 500 == 0:
        print(i,sess.run(cost, feed_dict = {X:xData, Y:yData}), sess.run(W), sess.run(b))
# 입력결과 출력
print(sess.run(H, feed_dict = {X :8}))

    
