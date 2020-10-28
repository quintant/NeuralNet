import random
import nodes

inLayer = nodes.inLayer(2)

hiddenLayer = nodes.Layer(7, inLayer)

hiddenLayer2 = nodes.Layer(5, hiddenLayer)

outLayer = nodes.Layer(10, hiddenLayer2)



inp = random.uniform(-6.9, 6.9)
inLayer.newVal([inp, random.uniform(-9.6, 6.9)])
hiddenLayer.calcL()
hiddenLayer2.calcL()
outLayer.calcL()
print(inLayer.listValues())
print(hiddenLayer.listValues())
print(hiddenLayer2.listValues())
print(outLayer.listValues())
