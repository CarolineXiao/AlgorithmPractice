class Solution:
    """
    @param str: A String
    @param left: a left offset
    @param right: a right offset
    @return: return a rotate string
    """
    def RotateString2(self, str, left, right):
        if str == "":
            return ""
        offset = (left - right) % len(str)
        if offset == 0:
            return str
        
        if offset > 0:
            prefix = str[:offset]
            rest = str[offset:]
            return rest + prefix
        else:
            postfix = str[offset:]
            rest = str[:offset]
            return postfix + rest
