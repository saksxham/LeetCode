class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s

        idx,d=0,1  
        #1--downward direction
        #2--upward direction
        #idx--index of 2d array in which it should be updated
        twod=[[] for x in range(len(s))]

        for i in s:
            twod[idx].append(i)
            if idx==0:
                d=1
            elif idx==numRows-1:
                d=-1
            
            idx=idx+d
        s=''
        for i in twod:
            for x in i:
                s=s+x
        return s