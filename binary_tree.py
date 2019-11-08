import csv

class Node:
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

def add(root, key, value=None):
    if root == None:
        root = Node(key, value=value)
        return root
    else:
        if key < root.key:
            if root.left == None:
                root.left = Node(key, value=value)
            else:
                add(root.left, key, value=value)
        else:
            if root.right == None:
                root.right = Node(key, value=value)
            else:
                add(root.right, key, value=value)
        return root

def search(root, key):
    if key == root.key:
        return root.value
    elif key < root.key:
        if root.left is None:
            return 'No value attributed to key'
        return search(root.left, key)
    elif key > root.key:
        if root.right is None:
            return str(key)+ 'No value attributed to key'
        return search(root.right, key)
    else:
        print(str(root.key) + ' is found')

if __name__ == '__main__':

    file = 'tree_test_csv.csv'

    first_line = True
    for line in open(file, 'r'):
        file_data = line.rstrip().split(',')
        if first_line is True:
            data_tree = Node(file_data[0], file_data[1])
            first_line = False
        else:
            add(data_tree, file_data[0], file_data[1])

    find_key = '10'
    tree_traverse = search(data_tree, find_key)
    print('key = ' + find_key + '\n' + 'value = ' + str(tree_traverse))






#    root = None

#    root = add(root, 9, 8)
#    root = add(root, 6)
#    root = add(root, 8)
#    root = add(root, 15)
#    root = add(root, 13)
#    root = add(root, 21)
#
#    root = add(root, 6)
#    root = add(root, 14)
#    root = add(root, 3)


#    print(root.key, root.value)
#    print(root.left.key, root.left.value)
#    print(root.right.left.key, root.right.left.value)
#    print(root.left.right.key)
