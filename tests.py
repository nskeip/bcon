import unittest2
from bcon import Block, GridWrapper

class BlockTestCase(unittest2.TestCase):
    def test_expects_basestring_as_name(self):
        self.assertRaises(TypeError, lambda: Block({}))


class GridWrapperTestCase(unittest2.TestCase):
    def test_expects_basestring_as_name(self):
        self.assertRaises(TypeError, lambda: GridWrapper({}))

    def test_minimum_structure(self):
        decl = ('container',)
        g = GridWrapper.create_from_decl(decl)
        self.assertEqual(g.class_, 'container')

    def test_nested_blocks_created(self):
        decl = ('span12', {'block': 'nav', 'context': {'foo': 'bar'}},
                          {'block': 'body'})
        g = GridWrapper.create_from_decl(decl)
        self.assertTrue(isinstance(g.blocks, list))

        self.assertEqual(2, len(g.blocks))

        b_nav = g.blocks[0]
        self.assertTrue(isinstance(b_nav, Block))
        self.assertEqual(b_nav.context, {'foo': 'bar'})

        b_body = g.blocks[1]
        self.assertTrue(isinstance(b_body, Block))