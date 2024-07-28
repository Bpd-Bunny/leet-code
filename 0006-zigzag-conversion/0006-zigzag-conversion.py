class Solution(object):
    def convert(self, s, numRows):
        if numRows==1:
            return s
        str2=''
        n=(numRows-1)*2
        for r in range(0,numRows):
            for i in range(r, len(s), n):
                str2+=s[i]
                if r>0 and r<numRows-1 and i+n-2*r < len(s):
                    str2+=s[i+n-2*r]
        return str2
        