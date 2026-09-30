```python
import os
from src.utils import deserialize_value
from src.types import Key, Value

class SSTable:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = {}  # Map of keys to values

    def write(self, key, value):
        self.data[key] = value
        with open(self.file_path, 'a') as file:
            file.write(f'{key.value.string_val}|{serialize_value(value)}
')

    def read(self, key):
        if key in self.data:
            return self.data[key]
        else:
            with open(self.file_path, 'r') as file:
                for line in file:
                    k, v = line.split('|')
                    if k == key.value.string_val:
                        return deserialize_value(v)
        return None
```
