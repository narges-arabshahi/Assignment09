import re
from unittest import result


class kasr:
    def __init__(self,s,m):
        self.soorat=s
        self.makhraj=m
    def show(self):
        print(self.soorat,"/",self.makhraj)
    def mul(self,mehman):
        result=kasr(None,None)
        result.soorat=self.soorat * mehman.soorat
        result.makhraj=self.makhraj * mehman.makhraj
        return result
    def sum(self,mehman):
        result=kasr(None,None)
        result.soorat=self.soorat * mehman.makhraj + self.makhraj * mehman.soorat
        result.makhraj=self.makhraj * mehman.makhraj
        return result
    def sub(self,mehman):
        result=kasr(None,None)
        result.soorat=self.soorat * mehman.makhraj - self.makhraj * mehman.soorat
        result.makhraj=self.makhraj * mehman.makhraj
        return result
    def div(self,mehman):
        result=kasr(None,None)
        result.soorat=self.soorat * mehman.makhraj
        result.makhraj=self.makhraj * mehman.soorat
        return result

a=kasr(3,5)
b=kasr(4,3)
a.show()
b.show()
c=a.mul(b)
c.show()
d=a.sum(b)
d.show()
e=a.sub(b)
e.show()
f=a.div(b)
f.show()