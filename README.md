# Rede neural desenvolvida em python aplicada no diagnóstico do câncer de mama. 
###### Descrição: Rede neural desenvolvida em python aplicada no diagnóstico do câncer de mama.

## Introdução
Esta é uma implementação de um modelo usado para diagnóstico de câncer de mama. A implementação permite que os usuários obtenham previsões
do diagnóstico do câncer de mama através de uma rede neural que recebe os dados de arquivos <b><i>.csv</i></b>.
### Atenção
* São três arquivos <b>.py</b>, mas somente o arquivo que deve ter a taxa de precisão considerada é o de <b>validação cruzada</b>.
### Pré requesitos
* Pandas 0.25.1
* Python 3.7
* Keras 2.3.1
* TensorFlow 1.14.0

## Execução
> entradas-breast.csv & saidas-breast.csv

Os arquivos .csv que contém os dados de entrada da rede neural foram extraídos originalmente 
<a href="https://archive.ics.uci.edu/ml/datasets/Breast+Cancer">daqui</a>.

> breast_cancer_simples.py

Primeiramente foi criado este arquivo. Seu objetivo era a criação da rede neural com 16 neurônios nas camadas ocultas (30 parâmetros de entrada + 1 de saída / 2 ≅ 16), com um modelo sequencial e utilizando camadas densas (um neurônio conectado aos outros da camada subsequente).

> breast_cancer_tuning.py

Tendo em vista os próximos parâmetros que deveriam ser adotados, foi criado este arquivo com o objetivo de ajustar aos parâmetros à nossa base de dados, isto é, qual melhor conjunto de parâmetros. Por exemplo: qual função de ativação deveremos utilizar.

Após a execução, esse foi o resultado obtido:

<img src="https://github.com/paulodias99/BreastCancerClassification/blob/master/img/resultadotuning.PNG"/>

##### Observação:
A utilização de 8 neurônios na câmada oculta foi escolhida para um teste de 100 épocas. No arquivo breast_cancer_cruzada.py, foi realizado testes em 500 épocas e a taxa de precisão foi mais alta com 16 neurônios.

> breast_cancer_cruzada.py

Neste arquivo utlizamos os parâmetros segundo o resultado gerado pelo arquivo <i>tuning.py</i>. Foi adicionada a técnica de Dropout, com a finalidade de zerar alguns valores da camada de entrada. Utlizamos uma taxa de 20% no Dropout. Outra mudança foi o teste com 500 épocas e um batch_size de 50, isto é, será calculado o erro para 50 registros e depois será feito o ajuste dos pesos.

Foi utilizada a técnica de validação cruzada, ou K-fold Cross Validation, isto é, a base de dados de treinamento será dividida em um número <i>K</i>, após feita a divisão será feito o treinamento com o restante dos registros e será realizado o teste na parte que foi separada. Após esse processo, outra parte dentro da base de dados será separada e o restante será utilizado para treinamento. Desta forma serão realizados fases de treinamento e teste em toda a base de dados. A imagem a seguir exemplifica este processo.

<img src="https://miro.medium.com/max/1368/0*P--gozwUfJ0TKtEp.png" width="600" height="300"/>

#### Execução

<img src="https://media.giphy.com/media/LPmFDTeNIB0rcJoYPC/giphy.gif"/>

#### Resultados obtidos

* K-fold Cross Validation

<img src="https://github.com/paulodias99/BreastCancerClassification/blob/master/img/resultadok10.PNG"/>

* Resultados Gerais

<img src="https://github.com/paulodias99/BreastCancerClassification/blob/master/img/resultadogeral.PNG"/>

# Taxa de precisão: 90.51%

#### Especificações da Máquina
O teste foi realizada em uma máquia:
* SO: Windows 10, x64
* Ambiente de Desenvolvimento: Spyder
* Utilização de memória durante a execução: 68%.
* RAM: 8gb.
* Processador: I5

