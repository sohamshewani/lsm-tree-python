```python
import unittest
from src.wal import WAL

class TestWAL(unittest.TestCase):
    def setUp(self):
        self.wal = WAL(log_dir='./test_log_dir')

    def tearDown(self):
        self.wal.close()

    def test_log_operation(self):
        self.wal.log_operation(WAL.WRITE, 'test_key', 'test_value')
        self.assertTrue(os.path.exists('./test_log_dir/wal_*.log'))

if __name__ == '__main__':
    unittest.main()
```
