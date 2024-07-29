class Solution(object):
    def myAtoi(self, s):
        rev=0
        neg=1
        a=0
        for i in s:
            if i=='.': break
            if i==' ' :
                if a==1: break
                continue
            if i=='+':
                if a==1: break
                if a==0: a=1
                continue
            if i=='-':
                if a==1: break
                a=1
                neg=-1
            if i.isalpha(): break
            if i.isdigit():
                a=1
                rev = rev*10 + int(i)
        rev = rev*neg

        if rev > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if rev < -2 ** 31:
            return -2 ** 31
        return rev
       
        