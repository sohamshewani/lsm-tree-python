```python
import unittest
from src.sstable import SSTable
from src.types import Key, Value

class TestSSTable(unittest.TestCase):
    def setUp(self):
        self.sstable = SSTable(file_path='./test_sstable')

    def tearDown(self):
        pass

    def test_write(self):
        key = Key()
        key.value.string_val = 'test_key'
        value = Value()
        value.value.string_val = 'test_value'
        self.sstable.write(key, value)
        self.assertEqual(self.sstable.read(key), value)

if __name__ == '__main__':
    unittest.main()
```
