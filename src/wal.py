```python
import os
from datetime import datetime
from src.utils import write_to_file

class WAL:
    def __init__(self, log_dir):
        self.log_dir = log_dir
        self.open_files = {}
        self.current_file = None
        self.current_file_name = None
        self.open_new_file()

    def open_new_file(self):
        current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.current_file_name = os.path.join(self.log_dir, f'wal_{current_time}.log')
        self.current_file = open(self.current_file_name, 'a')
        self.open_files[self.current_file_name] = self.current_file

    def log_operation(self, operation, key, value, merge_op=None):
        entry = f'{datetime.now()}|{operation.name}|{key}|{value}
'
        if merge_op:
            entry += f'MERGE_OP: {merge_op.name}
'
        self.current_file.write(entry)
        self.current_file.flush()

    def close(self):
        for file in self.open_files.values():
            file.close()
        self.open_files.clear()
```
