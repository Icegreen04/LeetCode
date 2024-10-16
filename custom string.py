import re
class CustomString:
    def __init__(self, s:str):
        self.s=s
    
    def capitalise(self):
        if not self.s:
            return self.s
        self.s=self.removeWhiteSpace()
        return self.caps(self.s[0]) + self.small(self.s[1:])
    
    def caps(self,char):
        new_char=''
        for i in char:
            if 'a' <= i <='z':
                new_char+= chr(ord(i)-32)
            else:
                new_char+= i
        return new_char
    
    def exchange(self,old,new):
        new_char=''
        for i in self.s:
            if i != old:
                new_char+=i
            else:
                new_char+=new
        return new_char            
    
    def isPalindrome(self):
        temp=self.removeWhiteSpace()
        temp=re.sub(r"[^0-9a-zA-Z]",'',self.s)
        temp=CustomString(temp)
        temp=temp.low()
        return temp==temp[::-1]
    
    def length(self):
        count=0
        if not self.s:
            return count
        for i in self.s:
            count+=1
        return count  
    
    def low(self):
        return self.small(self.s)      
    
    def removeWhiteSpace(self):
        left=0
        while left<self.length() and self.s[left]==' ':
            left+=1
        right=self.length()-1
        while right>=0 and self.s[right]==' ':
            right-=1
        self.s=self.s[left:right+1]
        return self.s
    
    def reverse(self):
        self.s=self.removeWhiteSpace()
        new_char=''
        for i in self.s[::-1]:
            new_char+=i
        return new_char
    
    def small(self,char):
        new_char=''
        for i in char:
            if 'A' <= i <= 'Z':
                new_char+= chr(ord(i)+32)
            else:
                new_char+= i
        return new_char
    
    def splitUp(self):
        str_arr=[]
        self.s=self.removeWhiteSpace()
        n=self.length()
        left=0
        right=0
        while right<n:
            if self.s[right]==' ':
                if left<right:
                    str_arr.append(self.s[left:right])
                right+=1
                left=right
            else:
                right+=1
        str_arr.append(self.s[left:right])
        return str_arr
    
    def findSubString(self,sub):
        n=self.length()
        temp=CustomString(sub)
        n_sub=temp.length()
        index=[]
        for i in range(n-n_sub+1):
            if self.s[i:i+n_sub]==sub:
                index.append(i)
        return index
    
    def titleCase(self):
        words=self.splitUp()
        new_char=''
        for i in words:
            new_char+=self.caps(i[0]) + self.small(i[1:])
            new_char+=' '
        temp=CustomString(new_char)
        return temp.removeWhiteSpace()
    
    def up(self):
        return self.caps(self.s)
    
                
s=CustomString(" Hello olleh  ")
print(s.length())
print(s.findSubString("hel"))
print(s.isPalindrome())
print(s.capitalise())
print(s.reverse())
print(s.up())
print(s.low())
print(s.titleCase())
print(s.removeWhiteSpace())
print(s.exchange('h','k'))

