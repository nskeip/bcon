#-*- coding: UTF-8 -*-
"""

So, we want to have a declaration like this:

('container', 
    ('row', 
        ('span12', {'block': 'header', 'modif': 'index'})), 
    ('row',
        ('span3', {'block': 'sidebar'}
                  {'block': 'adv'}),
        ('span9', {'block': 'content'})),
    ('row',
        ('span12', {'block': 'footer'})))


Let's do some tests...

Yes, a note on typecheck: we do it, because user can be a bad guy.

>>> decl1 = ('container',)
>>> w1 = Wrapper.create_from_decl(decl1)
>>> w1.class_
'container'
>>> w1.blocks
[]

>>> decl2 = ('span12', {'block': 'nav'})
>>> w2 = Wrapper.create_from_decl(decl2)
>>> w2.blocks
[<Block: nav>]

>>> decl3 = ('span12', {'block': 'nav'}, {'block': 'content'})
>>> w3 = Wrapper.create_from_decl(decl3)
>>> w3.blocks
[<Block: nav>, <Block: content>]


Testing invalid declaration:

>>> Wrapper.create_from_decl([{}, {'block': 'some_block'},])
Traceback (most recent call last):
...
TypeError: Invalid class_ type: <type 'dict'> (expected: basestring)


And testing invalid block...

>>> Block({})
Traceback (most recent call last):
...
TypeError: Invalid block name: {} (expected: basestring)

"""

class Block(object): # Block objects are made of dicts :)
    def __init__(self, name):
        if not isinstance(name, basestring):
            raise TypeError('Invalid block name: %s (expected: basestring)' \
                % name)
        self.name = name
        
    def __repr__(self):
        return '<Block: %s>' % self.name
        
    @classmethod
    def create_from_dict(cls, d):
        try:
            return cls(d['block'])
        except KeyError:
            raise TypeError('Invalid block declaration: %s' % d)

class Wrapper(object): # Wrapper objects are made of tuples
    def __init__(self, class_, blocks=None):
        if not isinstance(class_, basestring):
            raise TypeError('Invalid class_ type: %s (expected: basestring)' \
                % type(class_))

        if blocks is not None and not isinstance(blocks, (list, tuple)):
            raise TypeError('Invalid block type: %s' + type(class_) + \
                            '(expected: list or tuple)')

        self.class_ = class_
        self.blocks = blocks or []
        
    @classmethod
    def create_from_decl(cls, iterable):
        head = iterable[0]
        tail = list(iterable[1:])
        return Wrapper(head, blocks=[Block.create_from_dict(d) 
                                     for d in tail])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
