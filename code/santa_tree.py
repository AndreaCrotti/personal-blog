"""
Solve the santa problem using a generated tree, thus avoiding to
generate all the solutions that are clearly wrong.
"""
__metaclass__ = type

import unittest


class GiverGraph:
    def __init__(self, elems):
        self.santa = dict((x, None) for x in elems)

    def __setitem__(self, item, value):
        self.santa[item] = value

    def valid(self):
        # check that
        # - there are no circles
        # - the entries are compatible
        for et in self.santa:
            pass


class Sequence:
    def __init__(self, elems, sequence):
        """Pass the list of all the elements and the current sequence
        """
        self.elemns = elemns
        self.sequence = sequence

    def done(self):
        pass

    def invalid(self):
        pass

    def next(self):
        """Create new Sequence objects and return them
        """


class TestSantaTree(unittest.TestCase):
    SIMPLE_INPUT = [
        "first last", "second snd", "third third"
    ]
    # list all the possibilities
    OUTPUT = []

    def test_giver_graph(self):
        giv = GiverGraph()
        giv['a'] = 'b'
        giv['b'] = 'c'
        giv['c'] = 'a'
        self.assertTrue(giv.valid())


if __name__ == '__main__':
    unittest.main()
