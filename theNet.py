import random
import nodes

inLayer = nodes.inLayer(1)
## 1


## 2
#node = nodes.inNode(random.Random())
#inLayer.addNode(node)

## 3
#node = nodes.inNode(random.Random())
#inLayer.addNode(node)


hiddenLayer = nodes.Layer(3, inLayer)


outLayer = nodes.Layer(1, hiddenLayer)


for i in range(1,3):
    print(f"::-> {i}")
    inp = float(i)
    inLayer.newVal([inp])
    hiddenLayer.calcL()
    outLayer.calcL()
    print(inLayer.listValues())
    print(hiddenLayer.listValues())
    print(outLayer.listValues())