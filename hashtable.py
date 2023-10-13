#Source / Reference: WGU ZyBooks Course Material - Hashing / Chaining 7.2.1
class HashMap:
    def __init__(self, initial_capacity=20):
        # Initialize the hash map with a specified initial capacity
        self.buckets = [[] for _ in range(initial_capacity)]

    def insert(self, key, item):
        # Get the hash value of the key and calculate the bucket index
        bucket = hash(key) % len(self.buckets)
        # Get the list of key-value pairs in the bucket
        bucket_list = self.buckets[bucket]

        for i, kv in enumerate(bucket_list):
            # Check if the key already exists in the bucket
            if kv[0] == key:
                # If the key exists, update the corresponding value
                kv[1] = item
                return True

        # If the key doesn't exist, append a new key-value pair to the bucket
        bucket_list.append([key, item])
        return True

    def lookup(self, key):
        # Get the hash value of the key and calculate the bucket index
        bucket = hash(key) % len(self.buckets)
        # Get the list of key-value pairs in the bucket
        bucket_list = self.buckets[bucket]

        for pair in bucket_list:
            # Search for the key in the bucket
            if pair[0] == key:
                # If the key is found, return the corresponding value
                return pair[1]

        return None

    def remove(self, key):
        # Get the hash value of the key and calculate the bucket index
        bucket = hash(key) % len(self.buckets)
        # Get the list of key-value pairs in the bucket
        bucket_list = self.buckets[bucket]

        for i, pair in enumerate(bucket_list):
            # Search for the key in the bucket
            if pair[0] == key:
                # If the key is found, remove the key-value pair from the bucket
                del bucket_list[i]
                return True

        # If the key is not found, return False
        return False

    def values(self):
        # Retrieve all values from the hash map
        values = []
        for bucket in self.buckets:
            for pair in bucket:
                values.append(pair[1])
        return values
