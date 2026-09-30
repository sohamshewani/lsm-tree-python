```python
from src.utils import serialize_key
from src.sstable import SSTable
from src.types import Key, Value

class LSMTree:
    def __init__(self, log_dir, sstable_dir):
        self.log_dir = log_dir
        self.sstable_dir = sstable_dir
        self.memtable = MemTable()
        self.sstables = []
        self.create_sstables()

    def create_sstables(self):
        # Initialize SSTables
        pass

    def write(self, key, value):
        self.memtable.add(serialize_key(key), value)
        self.memtable.flush()
        self.log_operation(WRITE, key, value)

    def read(self, key):
        # First, check MemTable
        value = self.memtable.get(serialize_key(key))
        if value:
            return value

        # Then, check SSTables
        for sstable in self.sstables:
            value = sstable.read(key)
            if value:
                return value

        return None

    def log_operation(self, operation, key, value):
        wal = WAL(self.log_dir)
        wal.log_operation(operation, key, value)
        wal.close()
```
