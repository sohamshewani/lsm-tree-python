```python
from src.utils import serialize_value
from src.types import Key, Value, merge_operation_t

class MemTable:
    def __init__(self, max_size=1024):
        self.max_size = max_size
        self.entries = []
        self.size = 0

    def add(self, key, value, merge_op=None):
        if self.size + len(serialize_value(value)) > self.max_size:
            self.flush()
        self.entries.append((key, value, merge_op))
        self.size += len(serialize_value(value))

    def flush(self):
        if self.entries:
            # Logic to flush to SSTables
            pass

    def get(self, key):
        for entry in self.entries:
            if entry[0] == key:
                return entry[1]
        return None
```
