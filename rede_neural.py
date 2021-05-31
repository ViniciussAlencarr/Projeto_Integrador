""" import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

matriz = np.array([5,31,3,4,43,48,50,58,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31])

meio = np.median(matriz) # o valor do meio do array
media = np.mean(matriz) # media dos valores (soma de todos os valores dividido pela quantidade)
mode = stats.mode(matriz) #o numero que mais aparece
desvio_p = np.std(matriz) #o qunto ele desviou da media 
var = np.var(matriz) #variancia, disperção dos valores
percentual = np.percentile(matriz, 90) #retorna 90% dos mais jovens na lista

v = [5,7,8,7,2,17,2,9,4,11,12,9,6]
t = [99,86,87,88,111,86,103,87,94,78,77,85,86]
d = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
c = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22,23,24,25]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,60,65,58,50,40,30,20,10]

a = np.random.normal(5.0, 0.1, 1000)
b = np.random.normal(10.0, 0.1, 1000)

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept
print(r)
speed = myfunc(2)
print(speed)
mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()   
mymodel = np.poly1d(np.polyfit(x, y, 3))

myline = np.linspace(1, 25, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()
from sklearn import tree

clf = tree.DecisionTreeClassifier()

X = [[0,0,0],[1,0,1],[1,1,1],[0,1,0],[1,0,0],[1,1,0],[0,0,1],[]]

Y = ['Cliente inadimplente', 'Cliente honesto']

clf = clf.fit(X, Y)

prev = clf.predict([[0,0,0]])
print(prev)
from pybrain3.tools.shortcuts import buildNetwork
from pybrain3.datasets import SupervisedDataSet
from pybrain3.supervised.trainers import BackpropTrainer

ds = SupervisedDataSet(2, 1)

ds.addSample((1,1), (1))
ds.addSample((0,0), (-1))
ds.addSample((1,0), (1))

nn = buildNetwork(2, 4, 1, bias=True)

trainer = BackpropTrainer(nn, ds)

for i in range(2000):
    print(trainer.train())

while True:
    dormiu = float(input('Dormiu quanto tempo? '))
    estudou = float(input('Estudou quanto tempo? '))
    z = nn.activate((dormiu, estudou))[0] * 10.0
    print(f'Precisão da nota: {str(z)}')

from pybrain3.structure import FeedForwardNetwork
from pybrain3.structure import LinearLayer, SigmoidLayer, BiasUnit
from pybrain3.structure import FullConnection

rede = FeedForwardNetwork()

camadaEntrada = LinearLayer(2)
camadaOculta = SigmoidLayer(3)
camadaSaida = SigmoidLayer(1)

bias1 = BiasUnit()
bias2 = BiasUnit()

rede.addModule(camadaEntrada)
rede.addModule(camadaOculta)
rede.addModule(camadaSaida)
rede.addModule(bias1)
rede.addModule(bias2)

entradaOculta = FullConnection(camadaEntrada, camadaOculta)
ocultaSaida = FullConnection(camadaOculta, camadaSaida)
biasOculta = FullConnection(bias1, camadaOculta)
biasSaida = FullConnection(bias2, camadaSaida)

rede.sortModules()

print(rede)
print(entradaOculta.params)
print(ocultaSaida.params)
print(biasOculta.params)
print(biasSaida.params)"""


""" base.addSample((0,0), (0,))
base.addSample((0,1), (1,))
base.addSample((1,0), (1,))
base.addSample((1,1), (0,))

treinamento = BackpropTrainer(rede, dataset=base, learningrate=0.01,momentum=0.06)

for i in range(1, 10000):
  erro = treinamento.train()
  if i % 1000 == 0:
    print("Erro: %s" % erro)

print(rede.activate([0,0]))
print(rede.activate([1,0]))
print(rede.activate([0,1]))
print(rede.activate([1,1]))
 """"""
import pandas as pd
import numpy as np
import random

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

import seaborn as sns
import matplotlib.pyplot as plt

janela = 60
horizonte = 10
num_samples = 200

sample_size = janela+horizonte
xtime = np.arange(0, sample_size)

X = [np.sin(i * xtime) for i in np.linspace(0.05, 0.2, num_samples)]

plt.figure(figsize=(16,4))
for i in [0, num_samples//2, -1]:
  x = X[i]
  x = x - min(x) / max(x) - min(x)

  plt.plot(x)

plt.show() 

X = np.array(X)
data = X[:, :janela]
label = X[:, janela:]

idx = np.random.permutation(len(data))

data_train = data[idx[:int(0.8 * len(data))]]
label_train = label[idx[:int(0.8 * len(data))]]

data_test =  data[idx[int(0.8 * len(data)):]]
label_test = label[idx[int(0.8 * len(data)):]]

for i in range(3):
  k = np.random.choice(np.arange(len(data_test)))
  plt.figure()
  plt.plot(range(janela), data_test[k], label='Entrada')
  plt.plot(range(janela, janela+horizonte), label_test[k], label='Saida')
 plt.legend()
  plt.show() 

regress = LinearRegression()

regress.fit(data_train, label_train)

ypred = regress.predict(data_test)
import pandas as pd
import numpy as np

data = pd.read_excel('default of credit card clients.xls', header=1, index_col='ID')
data[['PAY_0', 'PAY_2','PAY_3','PAY_4','PAY_5','PAY_6']] += 2

X = data.drop('default payment next month', axis=1)
y = data['default payment next month'].copy()

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, KFold, train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2)

#parece que o random_state do LogisticRegression não está funcionando, 
#então este modelo pode dar resultados diferentes cada vez que for rodado
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
kf = KFold(n_splits=5, random_state=0, shuffle=True)

categs = [1,2,3,5,6,7,8,9,10]
ohe = onehotencorder = ColumnTransformer(transformers=[("OneHot", OneHotEncoder(), [1,3,5,6,7,8,9,13])],remainder='passthrough')
model = make_pipeline(ohe, LogisticRegression(C=0.5, random_state=1, class_weight='balanced'))
cross_val_score(model, X_train, y_train, n_jobs=-1, cv=kf, scoring='roc_auc').mean()

from sklearn.ensemble import RandomForestClassifier
kf = KFold(n_splits=5, random_state=0, shuffle=True)

model = RandomForestClassifier(n_jobs=-1, n_estimators=500, max_features=6, min_samples_leaf=20, random_state=0, class_weight='balanced')
cross_val_score(model, X_train, y_train, n_jobs=1, cv=kf, scoring='roc_auc').mean()



import xgboost as xgb

kf = KFold(n_splits=5, random_state=0, shuffle=True)

model = xgb.XGBClassifier(learning_rate=0.009, max_depth=6, min_child_weight=3,
                     subsample=0.15, colsample_bylevel=0.85, n_estimators=500)
cross_val_score(model, X_train, y_train, n_jobs=1, cv=kf, scoring='roc_auc').mean()

from sklearn.metrics import roc_auc_score

model = xgb.XGBClassifier(learning_rate=0.009, max_depth=6, min_child_weight=3,
                     subsample=0.15, colsample_bylevel=0.85, n_estimators=500)
model.fit(X_train, y_train)
p = model.predict_proba(X_test)
roc_auc_score(y_test, p[:, 1])
"""
from pybrain3.tools.shortcuts import buildNetwork
from pybrain3.structure import TanhLayer
from pybrain3.datasets import SupervisedDataSet
from pybrain3.supervised.trainers import BackpropTrainer
import server

# Create a network with two inputs, three hidden, and one output
nn = buildNetwork(10, 30, 1, bias=True, hiddenclass=TanhLayer)

# Create a dataset that matches network input and output sizes:
norgate = SupervisedDataSet(10, 1)

# Create a dataset to be used for testing.

# Add input and target values to dataset
# Values for NOR truth table
norgate.addSample((0,1,0,1,0,1,0,1,0,1), (1,)) # 1 == aprovado
norgate.addSample((1,0,1,0,1,0,1,0,1,0), (1,)) # 0 == recusado
norgate.addSample((0,1,0,1,0,0,1,0,0,0), (0,))
norgate.addSample((0,0,1,0,0,0,0,0,1,1), (0,))
norgate.addSample((1,0,0,0,1,1,0,0,1,1), (1,))
norgate.addSample((0,0,1,1,1,0,0,0,0,0), (0,))

# Add input and target values to dataset
# Values for NOR truth table


#Training the network with dataset norgate.
trainer = BackpropTrainer(nn, norgate)

# will run the loop 1000 times to train it.
for i in range(1, 50000):
  erro = trainer.train()
  if i % 1000 == 0:
    print("Erro: %s" % erro)
resultado = nn.activate([server.x1,
server.x2,
server.x3,
server.x4,
server.x5,
server.x6,
server.x7,
server.x8,
server.x9,
server.x10])

credit_result = ''
if resultado >= 1.00000000:
  credit_result = 'Credito aprovado'
  print("Crédito aprovado")
  print(resultado)
else:
  credit_result = 'Credito recusado'
  print("Crédito recusado")  
  print(resultado)
