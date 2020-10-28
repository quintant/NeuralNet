import random
import nodes

inLayer = nodes.inLayer(2)

hiddenLayer = nodes.Layer(420, inLayer)

hiddenLayer2 = nodes.Layer(69, hiddenLayer)

outLayer = nodes.Layer(10, hiddenLayer2)


for i in range(1,3):
    print(f"::-> {i}")
    inp = random.uniform(-6.9, 6.9)
    inLayer.newVal([inp, random.uniform(-9.6, 6.9)])
    hiddenLayer.calcL()
    outLayer.calcL()
    hiddenLayer2.calcL()
    print(inLayer.listValues())
    #print(hiddenLayer.listValues())
    #print(hiddenLayer2.listValues())
    print(outLayer.listValues())
