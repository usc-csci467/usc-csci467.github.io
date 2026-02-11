EPSILON = 1e-8

class Node(object):
    """Node in a computation graph.

    Must store the following:
        - self.value: Numerical value, computed during forward pass
        - self.grad: Gradient of output with respect to self, i.e. d(output)/d(self)
        - self.topo_order: Pointer to topological ordering of all nodes in graph
    """
    def backward(self):
        """Does backward pass.
        
        Assumption: self.grad has been set by parent nodes already.
        Propagates this gradient to all child nodes.
        """
        raise NotImplementedError

    def compute_grad(self):
        # This function only gets called on the output node.
        self.grad = 1   # Gradient of output w.r.t itself is 1
        for node in self.topo_order[::-1]:  # Reverse the list
            # Call backward() in reverse topological order
            node.backward()


class InputNode(Node):
    def __init__(self, value, topo_order):
        self.value = value
        self.grad = 0
        self.topo_order = topo_order
        topo_order.append(self)

    def backward(self):
        pass  # Nothing to do, as there are no child nodes

class AddNode(Node):
    """Given child nodes n1 and n2, computes n1 + n2."""
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.value = n1.value + n2.value
        self.grad = 0
        self.topo_order = n1.topo_order
        self.topo_order.append(self)

    def backward(self):
        # Chain rule: d(output)/d(child) = d(output)/d(self) * d(self)/d(child)
        # For addition, d(self)/d(child) = 1, since self = child1 + child2
        self.n1.grad += self.grad
        self.n2.grad += self.grad

class MulNode(Node):
    """Given child nodes n1 and n2, computes n1 * n2."""
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.value = n1.value * n2.value
        self.grad = 0
        self.topo_order = n1.topo_order
        self.topo_order.append(self)

    def backward(self):
        # Chain rule: d(output)/d(child) = d(output)/d(self) * d(self)/d(child)
        # For multiplication, d(self)/d(child1) = child2, since self = child1 * child2
        self.n1.grad += self.grad * self.n2.value
        self.n2.grad += self.grad * self.n1.value

class PowerNode(Node):
    """Given child node n and power p, computes n^p."""
    def __init__(self, n, power):
        # n is a Node, power is just a float/integer
        self.n = n
        self.power = power
        self.value = n.value**power
        self.grad = 0
        self.topo_order = n.topo_order
        self.topo_order.append(self)

    def backward(self):
        # Chain rule: d(output)/d(child) = d(output)/d(self) * d(self)/d(child)
        # For power, d(self)/d(child) = p * child^(p-1)
        self.n.grad += self.power * self.n.value**(self.power-1) * self.grad

class ReluNode(Node):
    """Given child node n, computes Relu(n)."""
    def __init__(self, n):
        self.n = n
        self.grad = 0
        self.value = max(n.value, 0)
        self.topo_order = n.topo_order
        self.topo_order.append(self)

    def backward(self):
        if self.value > 0:
            self.n.grad += self.grad
        else:
            self.n.grad += 0.0

def my_func(a_val, b_val):
    topo_order = []
    a = InputNode(a_val, topo_order)
    b = InputNode(b_val, topo_order)
    c = AddNode(a, b)  # c = a+b
    d = PowerNode(b, 3)  # d = b^3
    e = MulNode(c, d)  # e = c * d = (a+b) * b^3
    return e

def numerical_gradient(a_val, b_val):
    # Evaluate function at (a, b)
    orig = my_func(a_val, b_val).value

    # Measure change in output when you change each input by EPSILON
    change_a = my_func(a_val + EPSILON, b_val).value - orig
    change_b = my_func(a_val, b_val + EPSILON).value - orig

    # Derivative is (change in output) / (change in input)
    a_grad = change_a / EPSILON
    b_grad = change_b / EPSILON
    return [a_grad, b_grad]

def main():
    # Numerical gradient
    print('Numerical gradient:', numerical_gradient(7.0, 3.0))

    # Compare with backpropagation
    # Function: f(a, b) = (a + b) * b^3
    # Evaluate at a=7, b=3
    topo_order = []
    a = InputNode(7.0, topo_order)
    b = InputNode(3.0, topo_order)
    c = AddNode(a, b)  # c = a+b
    d = PowerNode(b, 3)  # d = b^3
    e = MulNode(c, d)  # e = c * d = (a+b) * b^3
    e.compute_grad()
    print('Backprop:', [a.grad, b.grad])

if __name__ == '__main__':
    main()
