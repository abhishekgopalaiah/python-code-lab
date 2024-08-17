class HashTable:
    def __init__(self, size=10):
        self.size = size  # initialize the hash table with a given size
        self.table = [[] for _ in range(size)]  # Create a list of empty lists

    def _hash(self, key):
        return hash(key) % self.size  # compute index of a key using hash function

    def __setitem__(self, key, value):
        index = self._hash(key)
        table = self.table[index]
        # update the value if key already exists
        for idx, kv in enumerate(table):
            # print(idx, kv)
            if kv[0] == key:
                table[idx] = (key, value)
                return

                # Otherwise, add a new key-value pair
        self.table[index].append((key, value))

    def __getitem__(self, key):
        # Retrieve a value by key
        index = self._hash(key)
        table = self.table[index]
        for kv in table:
            if kv[0] == key:
                return kv[1]
        # Key not found
        raise KeyError(f"Key '{key}' not found.")

    def __delitem__(self, key):
        # Delete a key-value pair by key
        index = self._hash(key)
        bucket = self.table[index]

        for i, kv in enumerate(bucket):
            if kv[0] == key:
                del bucket[i]
                return

    def __repr__(self):
        # Representation of the hash table for debugging
        return str(self.table)


if __name__ == "__main__":
    dictionary = HashTable()
    dictionary['name'] = 'Abhishek'
    dictionary['city'] = 'Bengaluru'
    print(f"name: {dictionary['name']}")
    print(f"city: {dictionary['city']}")

    dictionary['name'] = 'Abhishek G'
    print(f"updated name: {dictionary['name']}")
    print(f"city: {dictionary['city']}")

    # Try to retrieve the deleted key

    del dictionary['city']
    try:
        print(dictionary['city'])
    except KeyError as e:
        print(e)

    print(dictionary)
