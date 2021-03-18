class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        i_o = 0
        for i in range(0, len(s)):
            if i==0:
                i_o += int(roman_int_dict[s[i]])
            elif(s[i]=="V" and s[i-1]=="I"):
                i_o += int(roman_int_dict[s[i]])-2
            elif(s[i]=="X" and s[i-1]=="I"):
                i_o += int(roman_int_dict[s[i]])-2
                
            elif(s[i]=="L" and s[i-1]=="X"):
                i_o += int(roman_int_dict[s[i]])-20
            elif(s[i]=="C" and s[i-1]=="X"):
                i_o += int(roman_int_dict[s[i]])-20
                
            elif(s[i]=="D" and s[i-1]=="C"):
                i_o += int(roman_int_dict[s[i]])-200
            elif(s[i]=="M" and s[i-1]=="C"):
                i_o += int(roman_int_dict[s[i]])-200
            else:
                i_o += int(roman_int_dict[s[i]])
        return i_o
    
    
    