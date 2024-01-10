#Qno:1689

class Solution:
    def minPartitions(self, n: str) -> int:
        big=0
        for x in n:
            if int(x)>big:
                big=int(x)
        return big
    