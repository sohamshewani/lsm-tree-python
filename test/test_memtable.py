```python
import unittest
from src.memtable import MemTable
from src.types import Key, Value

class TestMemTable(unittest.TestCase):
    def setUp(self):
        self.memtable = MemTable()

    def tearDown(self):
        pass

    def test_add(self):
        key = Key()
        key.value.string_val = 'test_key'
        value = Value()
        value.value.string_val = 'test_value'
        self.memtable.add(key, value)
        self.assertEqual(self.memtable.get(key), value)

if __name__ == '__main__':
    unittest.main()
```
