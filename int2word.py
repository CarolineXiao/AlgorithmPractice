class Solution:
    """
    @param num: a non-negative integer
    @return: english words representation
    """
    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        word_dict = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eightteen",
            19: "Ninteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"}
            
        result = ""
        thousand = 0
        million = 0
        billion = 0
        
        if num // 1000 > 0:
            thousand = num // 1000
        
        if num // 1000000 > 0:
            million = num // 1000000
            thousand = num % 1000000 // 1000
        
        if num // 1000000000 > 0:
            billion = num // 1000000000
            million = num % 1000000000 // 1000000
            thousand = num % 1000000 // 1000
        
        
        if billion > 0:
            result += self.convert(billion, word_dict) + " Billion "
        if million > 0:
            result += self.convert(million, word_dict) + " Million "
        if thousand > 0:
            result += self.convert(thousand, word_dict) + " Thousand "
        result += self.convert(num % 1000, word_dict)
        
        return result
        
            
    def convert(self, num, word_dict):
        word = ""
        if num // 100 > 0:
            word += word_dict[num // 100] + " Hundred "
        if num % 100 < 20 and num % 100 > 0:
            word += word_dict[num % 100]
        elif num % 100 > 20:
            if num % 10 == 0:
                word += word_dict[num % 100]
            else:
                word += word_dict[num % 100 - num % 10] + " " + word_dict[num % 10]
                
        return word
            
