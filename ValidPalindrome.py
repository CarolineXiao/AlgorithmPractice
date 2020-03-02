class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        if s == '':
            return True
        
        for char in s:
            if not (char.isalpha() or char.isnumeric()):
                s = s.replace(char, '')
        
        s = s.lower()
        head = 0;
        tail = len(s) - 1;
        while head < tail:
            if s[head] != s[tail]:
                return False
            head = head + 1
            tail = tail - 1
        
            
        return True
