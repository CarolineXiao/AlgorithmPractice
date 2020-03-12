class Solution:
    """
    @param s: a string
    @return bool: whether you can make s a palindrome by deleting at most one character
    """
    def validPalindrome(self, s):
        # Write your code here
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                leftString = s[:left] + s[left+1:]
                rightString = s[:right] + s[right+1:]
                deleteLeft = self.isPalindrome(leftString)
                deleteRight = self.isPalindrome(rightString)
                return deleteLeft or deleteRight
            
            left += 1
            right -= 1
        return True
        
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
