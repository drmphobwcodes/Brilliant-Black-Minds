'''
what is HashMap?- A HashMap is a data structure that implements an associative array. It creates a mapping of keys to values.
What is an associative array?- An associative array is an abstract data type that stores a collection of unique keys and a 
collection of values, where each key is associated with one value.'''

class MyHashMap:
    # Constructor to initialize the hashmap
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]
    # Function to put the key and value in the hashmap
    def put(self, key, value):
        hash_key = key % self.size
        # If the key is already present in the hashmap, update the value
        bucket = self.buckets[hash_key]
        #Iterating through the bucket to check if the key is already present in the hashmap or not: if it is 
        #present, update the value
        for i, kv in enumerate(bucket):
            if kv[0] == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
    # Function to get the value of the key from the hashmap
    def get(self, key):
        hash_key = key % self.size
        bucket = self.buckets[hash_key]
        #Iterating through the bucket to check if the key is present in the hashmap or not: if it is present, 
        #return the value
        for i, kv in enumerate(bucket):
            if kv[0] == key:
                return kv[1]
        return -1
    # Function to remove the key from the hashmap
    def remove(self, key):
        hash_key = key % self.size
        bucket = self.buckets[hash_key]
        #Iterating through the bucket to check if the key is present in the hashmap or not: if it is present,
        #remove the key
        for i, kv in enumerate(bucket):
            if kv[0] == key:
                del bucket[i]
                return