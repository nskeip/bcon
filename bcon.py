#-*- coding: UTF-8 -*-


class Bacon(object):

    @classmethod
    def from_config(cls, config):
        """
        >>> conf = [{
        ...     'class': 'container',
        ...     'contents': [ # bacon stripes ;)
        ...         {
        ...             'class': 'row',
        ...             'contents': [
        ...                 {
        ...                     'class': 'span12',
        ...                     'contents': [
        ...                         {'block': 'header'},
        ...                     ],
        ...                 }
        ...             ]
        ...         },
        ...
        ...         {
        ...             'class': 'row',
        ...             'contents': [
        ...                 {
        ...                     'class': 'span4', 
        ...                     'contents': [{'block': 'content'}]
        ...                 },
        ...
        ...                 {
        ...                     'class': 'span8', 
        ...                     'contents': [
        ...                         {'block': 'nav'},
        ...                         {'block': 'adv'},
        ...                     ]
        ...                 },
        ...             ]
        ...         }
        ...     ]
        ... }]

        >>> cls = Bacon
        >>> p = cls.from_config(conf)
        >>> isinstance(p, Bacon)
        True
        """
        ret = cls()
        return ret

if __name__ == '__main__':
    import doctest
    doctest.testmod()
