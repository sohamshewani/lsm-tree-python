```python
import os
import hashlib
from bitarray import bitarray
from src.types import serialize_value, deserialize_value

def write_to_file(file_path, data):
    with open(file_path, 'a') as file:
        file.write(data)
        file.flush()

def serialize_value(value):
    if value.type == VALUE_TYPE_STRING:
        return value.string_val
    elif value.type == VALUE_TYPE_INTEGER:
        return str(value.integer_val)
    elif value.type == VALUE_TYPE_FLOAT:
        return str(value.float_val)
    elif value.type == VALUE_TYPE_BINARY:
        return value.binary_val

def deserialize_value(serialized_value, value_type):
    if value_type == VALUE_TYPE_STRING:
        return serialized_value
    elif value_type == VALUE_TYPE_INTEGER:
        return int(serialized_value)
    elif value_type == VALUE_TYPE_FLOAT:
        return float(serialized_value)
    elif value_type == VALUE_TYPE_BINARY:
        return serialized_value

def serialize_key(key):
    return key.value.string_val
```
