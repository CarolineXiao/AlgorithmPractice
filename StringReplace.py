class Solution:
    """
    @param a: The A array
    @param b: The B array
    @param s: The S string
    @return: The answer
    """
    def stringReplace(self, a, b, s):
        if s == "":
            return ""
        
        # key -> index in s, value->index in B
        length = set()
        a_dict = {}
        len_list = []
        
        for i in range(len(a)):
            a_dict[a[i]] = i
            length.add(len(a[i]))
        
        for l in length:
            len_list.append(l)
            
        len_list.sort(reverse=True)
            
        result = ""
        start = 0
        while start < len(s):
            found = False
            for length in len_list:
                end = start + length
                if end > len(s):
                    continue

                str = s[start:end]
                if str in a_dict:
                    found = True
                    result += b[a_dict[str]]
                    start = end
                    break
            if not found:
                result += s[start]
                start += 1
        
        return result
            
