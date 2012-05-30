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

"""

class Block(object): # Block objects are made of dicts :)
    def __init__(self, name=None):
        self.name = name

class Wrapper(object): # Wrapper objects are made of tuples
    def __init__(self, class_):
        self.class_ = class_
        
    @classmethod
    def create_from_decl(cls, iterable):
        head = iterable[0]
        tail = iterable[1:]
        return Wrapper(head)



if __name__ == '__main__':
    import doctest
    doctest.testmod()
