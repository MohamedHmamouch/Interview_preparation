#Write the generator random_gen that generates random numbers (use random module) between 10 and 20 and stops once it has generated the number 15.

import random
import pytest
def random_gen():
    while True:
        n = random.randint(10, 20)
        yield n
        if n == 15:
            break



if __name__=="__main__":

    def test_generator():
        g = random_gen()
        assert isinstance(g, type((x for x in [])))
        a = next(g)
        while a != 15:
            assert 10 <= a <= 20
            a = next(g)
        with pytest.raises(StopIteration):
            next(g)