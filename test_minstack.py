import minstack

def test_minstack():
    stack = minstack.MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    assert stack.getMin() == -3
    stack.pop()
    assert stack.top() == 0
    assert stack.getMin() == -2
def test_minstack_empty():
    stack = minstack.MinStack()
    assert stack.top() == None
    assert stack.getMin() == None
def test_minstack_single_element():
    stack = minstack.MinStack()
    stack.push(5)
    assert stack.top() == 5
    assert stack.getMin() == 5
    stack.pop()
    assert stack.top() == None
    assert stack.getMin() == None
def test_minstack_all_same():
    stack = minstack.MinStack()
    stack.push(2)
    stack.push(2)
    stack.push(2)
    assert stack.getMin() == 2
    stack.pop()
    assert stack.getMin() == 2
    stack.pop()
    assert stack.getMin() == 2
    stack.pop()                    
    assert stack.getMin() == None
