from pybrain3.tools.shortcuts import buildNetwork
from pybrain3.structure import TanhLayer
from pybrain3.datasets import SupervisedDataSet
from pybrain3.supervised.trainers import BackpropTrainer
import server

# Create a network with two inputs, three hidden, and one output
nn = buildNetwork(10, 3, 1, bias=True, hiddenclass=TanhLayer)

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

if resultado >= 1.00000000:
  print("Crédito aprovado")
  print(resultado)
else:
  print("Crédito recusado")  
  print(resultado) 