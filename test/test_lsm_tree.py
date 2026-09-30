```python
import unittest
from src.lsm_tree import LSMTree
from src.types import Key, Value

class TestLSMTree(unittest.TestCase):
    def setUp(self):
        self.lsm_tree = LSMTree(log_dir='./test_log_dir', sstable_dir='./test_sstable_dir')

    def tearDown(self):
        pass

    def test_write_and_read(self):
        key = Key()
        key.value.string_val = 'test_key'
        value = Value()
        value.value.string_val = 'test_value'
        self.lsm_tree.write(key, value)
        self.assertEqual(self.lsm_tree.read(key), value)

if __name__ == '__main__':
    unittest.main()
```
