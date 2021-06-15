from os import listxattr
from pybrain3.tools.shortcuts import buildNetwork
from pybrain3.structure import TanhLayer
from pybrain3.datasets import SupervisedDataSet
from pybrain3.supervised.trainers import BackpropTrainer

# Create a network with two inputs, three hidden, and one output
nn = buildNetwork(10, 30, 1, bias=True, hiddenclass=TanhLayer)

# Create a dataset that matches network input and output sizes:
norgate = SupervisedDataSet(10, 1)

# Create a dataset to be used for testing.

# Add input and target values to dataset
# Values for NOR truth table
norgate.addSample((0,1,0,1,0,1,0,1,0,1), (1,))
norgate.addSample((1,0,1,0,1,0,1,0,1,0), (1,))
norgate.addSample((0,1,0,1,0,0,1,0,0,0), (0,))
norgate.addSample((0,0,1,0,0,0,0,0,1,1), (0,))
norgate.addSample((1,0,0,0,1,1,0,0,1,1), (1,))
norgate.addSample((0,0,1,1,1,0,0,0,0,0), (0,))

# Add input and target values to dataset
# Values for NOR truth table

#Training the network with dataset norgate.
trainer = BackpropTrainer(nn, norgate)

""" lista = [
  x1,
  x2,
  x3,
  x4,
  x5,
  x6,
  x7,  
  x8,
  x9,
  x10
] """
lista = [
  1,
  1,
  1,
  1,
  1,
  1,
  1,
  1,
  1,
  1
]
fatoresPositivo = lista.count(1)
fatoresNegativo = lista.count(0)

status = 'Em análise...'
# will run the loop 1000 times to train it.
def iniciarAnalise(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10):
  print('Iniciando...')
  for i in range(1, 3000):
    status = 'Em análise'
    erro = trainer.train()
    if i % 1000 == 0:
      print("Erro: %s" % erro)
      resultado = nn.activate([
        x1,
        x2,
        x3,
        x4,
        x5,
        x6,
        x7,  
        x8,
        x9,
        x10
      ])
  if resultado >= 1.00000000:
    print("Crédito aprovado")
    status = 'Pronta para análise'
    return status
  else:
    print("Crédito recusado")  
    status = 'Recusado'
    return status

