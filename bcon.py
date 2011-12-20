#-*- coding: UTF-8 -*-
import os
import sys
import argparse
import json
from xml.dom.minidom import parse


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
        ret = cls(config['block'])

        if 'content' in config:
            for child_name, child_value in config['content'].iteritems():
                if isinstance(child_value, basestring):
                    ret.children[child_name] = child_value
                elif isinstance(child_value, dict):  # wow! it's a config!
                    child_block = cls.create_from_config(child_value)
                    ret.children[child_name] = child_block

        return ret
        
    @staticmethod
    def load_block_document(name):
        fp = os.path.abspath(os.path.join(name, 'source.html'))
        return parse(fp)

    def __repr__(self):
        return '<Block \'%s\'>' % self.name


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='Bacon. Yet another b-e-ms pattern implementation.')

    arg_parser.add_argument('config',
                            help='a js-config file describing the layout')

    arg_parser.add_argument('output_dir',
                            help='output directory where compiled files will be stored')

    arg_parser.add_argument('--static-dir', '-sD',
                            default='./static',
                            dest='static_dir',
                            help='where static is stored on your drive')

    arg_parser.add_argument('--static-prefix', '-sP',
                            default='/static',
                            dest='static_prefix',
                            help='static directory prefix on your pages')

    args = arg_parser.parse_args(sys.argv[1:])

    try:
        os.makedirs(args.output_dir)
    except OSError:
        print 'file exists or something. we do not wanna any overwrites'
        sys.exit(1)

    try:
        js_config = json.loads(open(args.config).read())
    except IOError:
        print 'the config aint found (or some other io-shit happened)'
        sys.exit(2)
    except ValueError:
        print 'failed to parse config'
        sys.exit(3)

    main_block = Block.create_from_config(js_config)