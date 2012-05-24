#-*- coding: UTF-8 -*-


class Bacon(object):
    def __init__(self):
        self._container = []
        self._class_name = None


    def append(self, piece_of_bacon):
        assert isinstance(piece_of_bacon, Bacon)
        self._container.append(piece_of_bacon)


    def __len__(self):
        return len(self._container)

    
    @classmethod
    def from_config(cls, config):
        """
        >>> conf = {
        ...     'class': 'container',
        ...     'contents': [
        ...              {
        ...                 'class': 'row',
        ...                 'contents': [
        ...                     {
        ...                         'class': 'span12',
        ...                         'contents': [
        ...                             {'block': 'header'},
        ...                         ],
        ...                     }
        ...                 ]
        ...             },
        ...    
        ...             {
        ...                 'class': 'row',
        ...                 'contents': [
        ...                     {
        ...                         'class': 'span4', 
        ...                         'contents': [{'block': 'content'}]
        ...                     },
        ...    
        ...                     {
        ...                         'class': 'span8', 
        ...                         'contents': [
        ...                             {'block': 'nav'},
        ...                             {'block': 'adv'},
        ...                         ]
        ...                     },
        ...                 ]
        ...             }
        ...         ]
        ...     }

        >>> p = Bacon.from_config(conf)
        >>> isinstance(p, Bacon)
        True
        >>> len(p)
        2
        """
        ret = cls()

        # TODO: block

        if 'class' in config:
            ret._class_name = config['class']

        if 'contents' in config:
            for c in config['contents']:
                piece_of_beacon = cls.from_config(c)
                ret.append(piece_of_beacon)

        return ret

if __name__ == '__main__':
    import doctest
    doctest.testmod()
