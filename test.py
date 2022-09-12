# Test task for VK


#testing tuple 
example_tuple = ('V', 20)

def test_tuple_1():
    assert tuple == type(example_tuple)


def test_tuple_2():
    s=('K', 22)
    assert ('V', 20, 'K', 22) == example_tuple+s   


def test_tuple_3():                         # negative test
    example_tuple[0] = 'b'
    assert example_tuple[0] == 'b'



#testing float
example_number= 77.7


def test_float_1():
    float_to_int = int(example_number)
    assert 77 == float_to_int
    
def test_float_2():
    round_example_number = round(example_number)
    assert 78 == round_example_number

def test_float_3():                           # negative test   
    assert example_number/0 == 0 