#-*- coding: UTF-8 -*-


class Block(object):
    def __init__(self, name):
        self.name = name
        self.children = {}

    @classmethod
    def create_from_config(cls, config):
        """
        >>> conf = { 'block': 'index', 'content': { 'header': {'block': 'header'}, 'body': {'block': 'body'}, }}
        >>> b = Block.create_from_config(conf)
        >>> b.name
        'index'
        >>> isinstance(b.children['header'], Block)
        True
        >>> isinstance(b.children['body'], Block)
        True
        """
        ret = Block(config['block'])
        
        if 'content' in config:
            for child_name, child_config in config['content'].iteritems():
                ret.children[child_name] = cls.create_from_config(child_config)

        return ret

