import pandas as pd

previsores = pd.read_csv('entradas-breast.csv')
classe = pd.read_csv('saidas-breast.csv')

from sklearn.model_selection import train_test_split
previsorestreinamento, previsoresteste, classestreinamento, classeteste = train_test_split(previsores, classe, test_size=0.25)

import keras
from keras.models import Sequential
from keras.layers import Dense

classificador = Sequential()
classificador.add(Dense(units = 16, activation = 'relu',
                        kernel_initializer = 'random_uniform', input_dim = 30))
classificador.add(Dense(units = 16, activation = 'relu',
                        kernel_initializer = 'random_uniform'))
classificador.add(Dense(units = 1, activation = 'sigmoid'))

otimizador = keras.optimizers.Adam(lr = 0.001, decay = 0.0001,
                                    clipvalue = 0.5)
classificador.compile(optimizer = otimizador, loss = 'binary_crossentropy',
                     metrics = ['binary_accuracy'])


#classificador.compile(optimizer = 'adam', loss = 'binary_crossentropy',
#                     metrics = ['binary_accuracy'])

classificador.fit(previsorestreinamento, classestreinamento,
                  batch_size = 10, epochs = 100)

pesos0 = classificador.layers[0].get_weights()
pesos1 = classificador.layers[1].get_weights()
pesos2 = classificador.layers[2].get_weights()

previsoes = classificador.predict(previsoresteste)
previsoes = (previsoes > 0.5)

from sklearn.metrics import confusion_matrix, accuracy_score
precisao = accuracy_score(classeteste, previsoes)
matriz = confusion_matrix(classeteste, previsoes)

resultado = classificador.evaluate(previsoresteste, classeteste)