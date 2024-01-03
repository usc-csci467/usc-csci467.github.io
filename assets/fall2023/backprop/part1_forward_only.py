EPSILON = 1e-8

class Node(object):
    """Node in a computation graph.
    
    Must store the following:
        - self.value: Numerical value, computed during forward pass
    """
    pass

class InputNode(Node):
    def __init__(self, value):
        self.value = value

class AddNode(Node):
    """Given child nodes n1 and n2, computes n1 + n2."""
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.value = n1.value + n2.value

class MulNode(Node):
    """Given child nodes n1 and n2, computes n1 * n2."""
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.value = n1.value * n2.value

def my_func(a_val, b_val, c_val):
    a = InputNode(a_val)
    b = InputNode(b_val)
    c = InputNode(c_val)
    d = AddNode(a, b)  # d = a + b
    e = MulNode(c, d)  # e = c * d = c * (a + b)
    return e.value

def numerical_gradient(a_val, b_val, c_val):
    # Evaluate function at (a, b, c)
    orig = my_func(a_val, b_val, c_val)

    # Measure change in output when you change each input by EPSILON
    change_a = my_func(a_val + EPSILON, b_val, c_val) - orig
    change_b = my_func(a_val, b_val + EPSILON, c_val) - orig
    change_c = my_func(a_val, b_val, c_val + EPSILON) - orig

    # Derivative is (change in output) / (change in input)
    a_grad = change_a / EPSILON
    b_grad = change_b / EPSILON
    c_grad = change_c / EPSILON
    return [a_grad, b_grad, c_grad]

def main():
    a = InputNode(7.0)
    b = InputNode(3.0)
    c = InputNode(2.0)
    d = AddNode(a, b)  # d = a + b
    e = MulNode(c, d)  # e = c * d = c * (a + b)
    print(e.value)

    # Numerical gradient
    print('Numerical gradient:', numerical_gradient(7.0, 3.0, 2.0))

if __name__ == '__main__':
    main()
