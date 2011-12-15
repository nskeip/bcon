#-*- coding: UTF-8 -*-


class Block(object):
    def __init__(self, name):
        self.name = name
        self.children = {}

    @classmethod
    def create_from_config(cls, config):
        """
        >>> conf = {
        ...     'block': 'index',
        ...     'content': {
        ...         'header': {
        ...             'block': 'header'
        ...         },
        ...         'body': {
        ...             'block': 'body',
        ...             'content': {
        ...                 'links': {
        ...                     'block': 'links',
        ...                     'content': {
        ...                         'link1': 'Some link',
        ...                         'some_place': {
        ...                             'block': 'some_block'
        ...                         }
        ...                     }
        ...                 }
        ...             }
        ...         }
        ...     }
        ... }
        >>> b = Block.create_from_config(conf)
        >>> b.name
        'index'
        >>> isinstance(b.children['header'], Block)
        True
        >>> b.children['header'].children
        {}
        >>> isinstance(b.children['body'], Block)
        True
        >>> isinstance(b.children['body'].children['links'], Block)
        True
        >>> b.children['body'].children['links'].name
        'links'
        >>> b.children['body'].children['links'].children
        {'link1': 'Some link', 'some_place': <Block 'some_block'>}
        >>> b.children['body'].children
        {'links': <Block 'links'>}
        """
        ret = Block(config['block'])

        if 'content' in config:
            for child_name, child_value in config['content'].iteritems():
                if isinstance(child_value, basestring):
                    ret.children[child_name] = child_value
                elif isinstance(child_value, dict):  # wow! it's a config!
                    child_block = cls.create_from_config(child_value)
                    ret.children[child_name] = child_block

        return ret

    def __repr__(self):
        return '<Block \'%s\'>' % self.name
