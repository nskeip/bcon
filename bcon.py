#-*- coding: UTF-8 -*-


class Bacon(object):
    def __init__(self, block_name=None, class_name=None):
        self._container = []

        self.block_name = block_name
        self.class_name = class_name

    def append(self, piece_of_bacon):
        assert isinstance(piece_of_bacon, Bacon)
        self._container.append(piece_of_bacon)

    def __len__(self):
        return len(self._container)

    def __iter__(self):
        return self._container.__iter__()

    def __getitem__(self, item):
        return self._container[item]

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
        ...                         'block': 'header',
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
        >>> p[0].class_name
        'row'
        >>> p[0][0].class_name
        'span12'
        >>> p[1][0].class_name
        'span4'

        >>> for pb in p:
        ...     pb.class_name == 'row'
        True
        True
        """
        ret = cls(block_name=config.get('block'),
                  class_name=config.get('class'))

        if 'contents' in config:
            for c in config['contents']:
                piece_of_beacon = cls.from_config(c)
                ret.append(piece_of_beacon)

        return ret

if __name__ == '__main__':
    import doctest
    doctest.testmod()
