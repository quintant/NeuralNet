import random
import nodes

inLayer = nodes.inLayer(2)

hiddenLayer = nodes.Layer(4, inLayer)

hiddenLayer2 = nodes.Layer(5, hiddenLayer)

outLayer = nodes.Layer(10, hiddenLayer2)


for i in range(1,3):
    print(f"::-> {i}")
    inp = float(i)
    inLayer.newVal([inp, inp/36])
    hiddenLayer.calcL()
    outLayer.calcL()
    hiddenLayer2.calcL()
    print(inLayer.listValues())
    print(hiddenLayer.listValues())
    print(hiddenLayer2.listValues())
    print(outLayer.listValues())