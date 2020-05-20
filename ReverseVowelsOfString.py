class Solution:
    """
    @param s: a string
    @return: reverse only the vowels of a string
    """
    def reverseVowels(self, s):
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowel_set = set(vowels)
        
        s_arr = list(s)
        
        left = 0
        right = len(s_arr) - 1
        
        while left <= right:
            while left < right and s_arr[left] not in vowel_set:
                left += 1
            
            while left <= right and s_arr[right] not in vowel_set:
                right -= 1
            
            if left <= right:
                s_arr[left], s_arr[right] = s_arr[right], s_arr[left]
                left += 1
                right -= 1
            
        return ''.join(s_arr)
