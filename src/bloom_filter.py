```python
from bitarray import bitarray
from src.utils import serialize_key

class BloomFilter:
    def __init__(self, key_space, filter_size=100000, hash_count=7):
        self.key_space = key_space
        self.filter_size = filter_size
        self.hash_count = hash_count
        self.bit_array = bitarray(filter_size)
        self.bit_array.setall(False)

    def add(self, key):
        key_bytes = serialize_key(key)
        hashes = [hash(key_bytes) % self.filter_size for _ in range(self.hash_count)]
        for i in hashes:
            self.bit_array[i] = True

    def contains(self, key):
        key_bytes = serialize_key(key)
        hashes = [hash(key_bytes) % self.filter_size for _ in range(self.hash_count)]
        return all(self.bit_array[i] for i in hashes)
```
