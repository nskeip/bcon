#-*- coding: UTF-8 -*-
"""

('container', 
    ('row', 
        ('span12', {'block': 'header', 'modif': 'index'})), 
    ('row',
        ('span3', {'block': 'sidebar'}
                  {'block': 'adv'}),
        ('span9', {'block': 'content'})),
    ('row',
        ('span12', {'block': 'footer'})))

>>> decl1 = ('container',)
>>> w1 = Wrapper.create_from_decl(decl1)
>>> w1.class_
'container'
>>> w1.blocks
[]

>>> decl2 = ('span12', {'block': 'nav'})
>>> w2 = Wrapper.create_from_decl(decl2)
>>> w2.blocks
[{'block': 'nav'}]

>>> decl3 = ('span12', {'block': 'nav'}, {'block': 'content'})
>>> w3 = Wrapper.create_from_decl(decl3)
>>> w3.blocks
[{'block': 'nav'}, {'block': 'content'}]


Testing invalid declaration:

>>> Wrapper.create_from_decl([{}, {'block': 'some_block'},])
Traceback (most recent call last):
...
TypeError: Invalid class_ type: <type 'dict'> (expected: basestring)

"""

class Block(object): # Block objects are made of dicts :)
    def __init__(self, name=None):
        self.name = name

class Wrapper(object): # Wrapper objects are made of tuples
    def __init__(self, class_, blocks=None):    
        if not isinstance(class_, basestring):
            raise TypeError('Invalid class_ type: %s (expected: basestring)' % type(class_))

        if blocks is not None and not isinstance(blocks, (list, tuple)):
            raise TypeError('Invalid blocks type: %s (expected: list or tuple)' % type(class_))

        self.class_ = class_
        self.blocks = blocks or []
        
    @classmethod
    def create_from_decl(cls, iterable):
        head = iterable[0]
        tail = list(iterable[1:])
        return Wrapper(head, blocks=tail)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
