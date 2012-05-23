#-*- coding: UTF-8 -*-

"""
[
    [ # row began
        { # span bagan
            'class': 'span6',
            'content': 'some_block',
        },
        {
            'class': 'span6',
        },
    ]
]
"""

class Page(object):

    @classmethod
    def from_config(cls):
        """
        >>> conf = [
        ...     'container',
        ...     [
        ...         'row',
        ...         {'class': 'span12', 'block': ['header']}
        ...     ],
        ...
        ...     [
        ...         'row',
        ...         {'class': 'span4', 'block': ['content']},
        ...         {'class': 'span8', 'block': ['nav']},
        ...     ]
        ... ]
        """

if __name__ == '__main__':
    import doctest
    doctest.testmod()
