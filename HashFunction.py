class Solution:
    """
    @param key: A string you should hash
    @param HASH_SIZE: An integer
    @return: An integer
    """
    def hashCode(self, key, HASH_SIZE):
        ans = 0
        for i in range(len(key)):
            ans = (ans * 33 + ord(key[i])) % HASH_SIZE
        return ans
