class Solution:

    def calc(self, n: int):
        result: int = 0
        n = [x for x in str(n)]
        for i in n:
            result += pow(int(i),2)
        return result

    def isHappy(self, n: int) -> bool:
        
        numbers = set()
        while True:
            n = self.calc(n)
            if n in numbers:
                return False
            numbers.add(n)
            if n == 1:
                return True