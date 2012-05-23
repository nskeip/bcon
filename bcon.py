#-*- coding: UTF-8 -*-


class Page(object):

    @classmethod
    def from_config(cls, config):
        """
        >>> conf = {
        ...     'class': 'container',
        ...     'contents': [
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
        ... }
        """
        pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
