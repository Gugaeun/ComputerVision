import numpy as np
import tensorflow as tf
import keras.datasets as ds

from keras.models import Sequential
# 99% 달성을 위한 증강, 리셰이프 레이어들을 추가로 임포트합니다.
from keras.layers import Dense, Dropout, Reshape, Flatten, RandomRotation, RandomTranslation
from keras.optimizers import SGD
from keras.callbacks import LearningRateScheduler

# 1. 데이터 로드 및 전처리
(x_train, y_train), (x_test, y_test) = ds.mnist.load_data()
x_train = x_train.reshape(60000, 784).astype(np.float32) / 255.0
x_test = x_test.reshape(10000, 784).astype(np.float32) / 255.0
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

# 2. 모델 구축 (데이터 증강 레이어 포함)
mlp = Sequential()

# [핵심 트릭] 784 픽셀을 증강 레이어가 인식할 수 있게 28x28x1 이미지 형태로 잠시 바꿉니다.
mlp.add(Reshape((28, 28, 1), input_shape=(784,)))

# 이제 안전하게 무작위 회전과 이동 증강을 적용합니다. (학습할 때만 작동하고 검증할 때는 자동으로 꺼집니다!)
mlp.add(RandomRotation(factor=0.05))       # 약 18도 이내 무작위 회전
mlp.add(RandomTranslation(height_factor=0.05, width_factor=0.05)) # 상하좌우 5% 이내 무작위 이동

# 증강이 끝났으니 다시 원래대로 일렬(784)로 펼쳐서 Dense 층에 넘겨줍니다.
mlp.add(Flatten())

# 기존 Dense 레이어 구조 연결
mlp.add(Dense(units=512, activation='relu'))
mlp.add(Dropout(0.2))
mlp.add(Dense(units=256, activation='relu'))
mlp.add(Dropout(0.2))
mlp.add(Dense(units=10, activation='softmax'))

# 3. 컴파일
opt = SGD(learning_rate=0.1, momentum=0.9, nesterov=True)
mlp.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

# 4. 학습률 스케줄러 정의 및 콜백
def scheduler(epoch, lr):
    if epoch < 20:
        return lr
    else:
        return lr * 0.1

lr_callback = LearningRateScheduler(scheduler)

# 5. 모델 학습 (데이터 증강이 들어가므로 기존보다 조금 더 여유 있게 50 에포크를 돌립니다)
mlp.fit(
    x_train, y_train, 
    batch_size=128, 
    epochs=50, 
    validation_data=(x_test, y_test), 
    callbacks=[lr_callback], 
    verbose=2
)

# 6. 결과 출력
res = mlp.evaluate(x_test, y_test, verbose=0)
print('\n★ 증강 적용 최종 테스트 정확률 =', res[1] * 100, '%')




