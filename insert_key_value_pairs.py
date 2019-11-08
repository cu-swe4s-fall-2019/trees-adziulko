import argparse
import sys
import binary_tree as bt
import avl
sys.path.append('hash-tables-adziulko')
ht = importlib.import_module('hash-tables-adziulko.hash_tables')


def main():
    parser = argparse.ArgumentParser(description='Store key, value pairs in '
                                     'data structures',
                                     prog='insert_key_value_pairs')

    parser.add_argument('--datastructure',
                        type=str,
                        help='Name of data structure (hash, binary tree, or avl tree',
                        required=True)

    parser.add_argument('--dataset',
                        type=str,
                        help='Name of txt file with key/value',
                        required=True)

    parser.add_argument('--numkey',
                        type=int,
                        help='Number of key/value pairs',
                        required=True)

    args = parser.parse_args()

    datastructure = args.datastructure
    filename = args.dataset
    numkey = args.numkey

if __name__ == '__main__':
    main()
