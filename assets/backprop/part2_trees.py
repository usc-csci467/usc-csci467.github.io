EPSILON = 1e-8

class Node(object):
    """Node in a computation graph.

    Must store the following:
        - self.value: Numerical value, computed during forward pass
        - self.grad: Gradient of output with respect to self, i.e. d(output)/d(self)
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
        self.backward()  # Recursively do the actual backward pass


class InputNode(Node):
    def __init__(self, value):
        self.value = value
        self.grad = 0

    def backward(self):
        pass  # Nothing to do, as there are no child nodes

class AddNode(Node):
    """Given child nodes n1 and n2, computes n1 + n2."""
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.value = n1.value + n2.value
        self.grad = 0

    def backward(self):
        # Chain rule: d(output)/d(child) = d(output)/d(self) * d(self)/d(child)
        # For addition, d(self)/d(child) = 1, since self = child1 + child2
        self.n1.grad = self.grad
        self.n2.grad = self.grad

        # Recursively backprop through the child nodes
        self.n1.backward()
        self.n2.backward()

class MulNode(Node):
    """Given child nodes n1 and n2, computes n1 * n2."""
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.value = n1.value * n2.value
        self.grad = 0

    def backward(self):
        # Chain rule: d(output)/d(child) = d(output)/d(self) * d(self)/d(child)
        # For multiplication, d(self)/d(child1) = child2, since self = child1 * child2
        self.n1.grad = self.grad * self.n2.value
        self.n2.grad = self.grad * self.n1.value

        # Recursively backprop through the child nodes
        self.n1.backward()
        self.n2.backward()

class PowerNode(Node):
    """Given child node n and power p, computes n^p."""
    def __init__(self, n, power):
        # n is a Node, power is just a float/integer
        self.n = n
        self.power = power
        self.value = n.value**power
        self.grad = 0

    def backward(self):
        # Chain rule: d(output)/d(child) = d(output)/d(self) * d(self)/d(child)
        # For power, d(self)/d(child) = p * child^(p-1)
        self.n.grad = self.power * self.n.value**(self.power-1) * self.grad

        # Recurse on child node
        self.n.backward()

class ReluNode(Node):
    """Given child node n, computes Relu(n)."""
    def __init__(self, n):
        self.n = n
        self.grad = 0
        self.value = max(n.value, 0)

    def backward(self):
        # Chain rule: d(output)/d(child) = d(output)/d(self) * d(self)/d(child)
        # For Relu, d(self)/d(child) = 1 if child > 0, 0 otherwise
        if self.value > 0:
            self.n.grad = self.grad
        else:
            self.n.grad = 0.0

        # Recurse on child node
        self.n.backward()

def my_func(a_val, b_val, c_val):
    a = InputNode(a_val)
    b = InputNode(b_val)
    c = InputNode(c_val)
    d = PowerNode(b, 3)  # d = b^3
    e = AddNode(a, d)  # e = a + d
    f = MulNode(c, e)  # e = c * e = c * (a + b^3)
    return f

def numerical_gradient(a_val, b_val, c_val):
    # Evaluate function at (a, b, c)
    orig = my_func(a_val, b_val, c_val).value

    # Measure change in output when you change each input by EPSILON
    change_a = my_func(a_val + EPSILON, b_val, c_val).value - orig
    change_b = my_func(a_val, b_val + EPSILON, c_val).value - orig
    change_c = my_func(a_val, b_val, c_val + EPSILON).value - orig

    # Derivative is (change in output) / (change in input)
    a_grad = change_a / EPSILON
    b_grad = change_b / EPSILON
    c_grad = change_c / EPSILON
    return [a_grad, b_grad, c_grad]

def main():
    # Numerical gradient
    print('Numerical gradient:', numerical_gradient(7.0, 3.0, 2.0))

    # Compare with backpropagation
    # Function: f(a, b, c) = (a + b^3) * c
    # Evaluate at a=7, b=3, c=2
    a = InputNode(7.0)
    b = InputNode(3.0)
    c = InputNode(2.0)
    d = PowerNode(b, 3)  # d = b^3
    e = AddNode(a, d)  # d = a + e
    f = MulNode(c, e)  # f = d * e
    f.compute_grad()
    print('Backprop:', [a.grad, b.grad, c.grad])

if __name__ == '__main__':
    main()
