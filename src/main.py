from lsm_tree_python import LSMTree

if __name__ == '__main__':
    lsm_tree = LSMTree()
    lsm_tree.put(b'key1', b'value1')
    lsm_tree.put(b'key2', b'value2')
    print(lsm_tree.get(b'key1'))
    print(lsm_tree.get(b'key2'))
    lsm_tree.delete(b'key1')
    print(lsm_tree.get(b'key1'))