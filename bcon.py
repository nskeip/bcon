#-*- coding: UTF-8 -*-
"""

So, we want to have a declaration like this:

('container', 
    ('row', 
        ('span12', {'block': 'header', 'modif': 'index'})), 
    ('row',
        ('span3', {'block': 'sidebar'}
                  {'block': 'adv'}),
        ('span9', {'block': 'content', 'context': {'foo': 'bar'}})),
    ('row',
        ('span12', {'block': 'footer'})))

"""

class Block(object): # Block objects are made of dicts :)
    def __init__(self, name, context=None):
        if not isinstance(name, basestring):
            raise TypeError('Invalid block name: %s (expected: basestring)' \
                % name)

        self.name = name
        self.context = context or {}
        
    def __repr__(self):
        return '<Block: %s>' % self.name
        
    @classmethod
    def create_from_dict(cls, d):
        try:
            return cls(d['block'],
                       context=d.get('context'))
        except KeyError:
            raise TypeError('Invalid block declaration: %s' % d)

class GridWrapper(object): # GridWrapper objects are made of tuples
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
        return GridWrapper(head, blocks=[Block.create_from_dict(d)
                                     for d in tail])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
