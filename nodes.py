class inNode():
    def __init__(self, value: float) -> None:
        self.value = value

    def Value(self):
        return self.value

    def updateValue(self, val:float):
        self.value = val

class Node():
    """
    Node, should:
    > have a wheight
    > have a list of all inbound nodes
    """
    import random
    def __init__(self, inboundNodes: list) -> None:
        self.inboundNodes = inboundNodes
        self.inboundNodesWeight = [Node.random.uniform(-1, 1) for x in inboundNodes]
        self.value = 0.0


    def updateNodeWheight(self, val: float, index: int):
        self.inboundNodesWeight[index] = float

    
    def calc(self):
        """
        calculates the node value from inNode + wheight
        """
        self.value = 0.0
        for node, wheight in zip(self.inboundNodes, self.inboundNodesWeight):
            self.value += node.value *wheight



class Layer():
    """
    > hold a list of all nodes in layer
    """
    def __init__(self, count: int, prevLayer: "Layer") -> None:
        self.NodeList = []
        for _ in range(count):
            node = Node(prevLayer.listNodes())
            self.NodeList.append(node)
    
    def calcL(self):
        for node in self.NodeList:
            node.calc()


    
    def listNodes(self) -> Node:
        """
        returns a list with all the node is the layer
        """
        return self.NodeList

    def listValues(self):
        return [node.value for node in self.NodeList]

class inLayer():
    """
    > hold a list of all nodes in layer
    """
    def __init__(self, count: int) -> None:
        self.NodeList = []
        for _ in range(count):
            node = inNode(1.0)
            self.NodeList.append(node)
    
    def calcL(self):
        for node in self.NodeList:
            node.calc()

    def newVal(self, values: list):
        for node, nval in zip(self.NodeList, values):
            node.updateValue(nval)
    
    def listNodes(self) -> Node:
        """
        returns a list with all the node is the layer
        """
        return self.NodeList

    def listValues(self):
        return [node.Value() for node in self.NodeList]