class Node():
    """
    Node, should:
    > have a wheight
    > have a list of all inbound nodes
    """
    def __init__(self, wheight: float, inboundNodes: list) -> None:
        self.wheight = wheight
        self.inboundNodes = inboundNodes


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