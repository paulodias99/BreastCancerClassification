###############
# IMPORTAÇÕES #
###############
import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score

###############################
#  LEITURA DOS ARQUIVOS .CSV  #
###############################
previsores = pd.read_csv('entradas-breast.csv')
classe = pd.read_csv('saidas-breast.csv')

###############################
#       FUNÇÃO CRIAR REDE     #
###############################
def criarRede():
    classificador = Sequential()
    classificador.add(Dense(units = 16, activation = 'relu', 
                        kernel_initializer = 'uniform', input_dim = 30))
    classificador.add(Dropout(0.2))
    classificador.add(Dense(units = 16, activation = 'relu', 
                        kernel_initializer = 'normal'))
    classificador.add(Dropout(0.2))
    classificador.add(Dense(units = 1, activation = 'sigmoid'))
    otimizador = keras.optimizers.Adam(lr = 0.001, decay = 0.0001, clipvalue = 0.5)
    classificador.compile(optimizer = otimizador, loss = 'binary_crossentropy',
                      metrics = ['binary_accuracy'])
    return classificador

#############################################
#      DEFINIÇÃO DAS ÉPOCAS E BATCH_SIZE    #
#############################################
classificador = KerasClassifier(build_fn = criarRede,
                                epochs = 500,
                                batch_size = 50)
resultados = cross_val_score(estimator = classificador,
                             X = previsores, y = classe,
                             cv = 10, scoring = 'accuracy')

###############################
#  GERAR RESULTADO E DESVIO   #
###############################
media = resultados.mean()
desvio = resultados.std()