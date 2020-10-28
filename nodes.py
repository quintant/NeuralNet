class Node():
    """
    Node, should:
    > have a wheight
    > have a list of all inbound nodes
    """
    import random
    def __init__(self, inboundNodes: list) -> None:
        self.inboundNodes = inboundNodes
        self.inboundNodesWeight = [Node.random.Random() for x in inboundNodes]
        self.value = 0.0

    def wheight(self):
        """
        returns the node whight
        """
        return self.wheight
    
    def calc(self):
        """
        calculates the node value from inNode + wheight
        """
        self.value = 0.0
        for node, wheight in zip(self.inboundNodes, self.inboundNodesWeight):
            self.value += node*wheight


class Layer():
    """
    > hold a list of all nodes in layer
    """
    def __init__(self) -> None:
        self.NodeList = []
    
    def addNode(self, node: Node):
        """
        add node to list
        """
        self.NodeList.append(node)
    
    def listNodes(self):
        """
        returns a list with all the node is the layer
        """
        return self.NodeList