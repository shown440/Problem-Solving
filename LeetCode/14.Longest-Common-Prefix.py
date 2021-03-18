class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        print(len(strs))
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        prefix = ""
        j=0
        flg=None
        while j != len(strs[0]):
            for i in range(1,len(strs)):
                # print(1)
                # print(strs[i][j])
                try:
                    if strs[0][j] == strs[i][j]:
                        flg=True
                    else:
                        flg = False
                        break
                except:
                    flg = False
                    break
            if flg == True:
                prefix=prefix+strs[0][j]
            if flg == False:
                # break
                return prefix       
            j=j+1
        return prefix
            
                    
