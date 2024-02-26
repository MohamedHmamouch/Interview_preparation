


def decorator_to_str(func)->str:

    def to_string_converter(*args,**kwargs):

        result=func(*args,**kwargs)

        return str(result)
        
    return to_string_converter
@decorator_to_str
def add(a, b):
    return a + b


@decorator_to_str
def get_info(d):
    return d['info']


def test_to_str():
    try:
        assert add(5, 30) == '35'
        assert get_info({'info': [1, 2, 3]}) == '[1, 2, 3]'
        return "All tests passed successfully!"
    except AssertionError as e:
        return f"Test failed: {e}"

if __name__=='__main__':

    print(test_to_str())