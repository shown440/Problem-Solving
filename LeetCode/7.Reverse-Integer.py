class Solution:
    def reverse(self, x: int) -> int: 
        mystr = str(x)
        if mystr[0] == "-":
            op_str = "-" + mystr[:0:-1]
            if int(op_str) < -2147483648:
                return 0
            return int(op_str)
        # print(mystr)
        op_str = mystr[::-1]
        if int(op_str) > 2147483647:
            return 0
        return int(op_str)
        