import numpy as np 
import random
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Activation

def create_training_data(x):
    x = np.array(x)    
    x = x[x[:, 1].argsort()]
    for i in range(len(x)):
        if x[i, 1] == 1:
            y = i
            break   
    t = len(x) - y  
    b = x[-(2*t):]                                        
    np.random.shuffle(b)
    return b

x = np.load('training_data3.npy', allow_pickle = True)      
train = create_training_data(x)    
test = np.array(np.load('testing_data3.npy', allow_pickle = True))                      

                             
train_X = train[:, 0, None]
train_y = train[:, 1, None]
test_X = test[:, 0, None]
test_y = test[:, 1, None]

featureset = np.vstack(train_X.squeeze(axis=1))
labels = np.vstack(train_y.squeeze(axis=1))
test_featureset = np.vstack(test_X.squeeze(axis=1))
test_labels = np.vstack(test_y.squeeze(axis=1))

model = Sequential()

model.add(Dense(8, activation = 'relu', input_shape = (4,)))
model.add(Dense(16, activation = 'relu'))
model.add(Dense(32, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))

model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

model.fit(featureset, labels, epochs = 5)
val_loss, val_accuracy = model.evaluate(test_featureset, test_labels)
print(val_loss, val_accuracy)
model.save('flappy_bird_AI3.h5')
    
# print((model.predict(test_featureset) > 0.5).astype(int))