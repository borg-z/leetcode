from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # result = []
        # magazine = [x for x in magazine]
        # for l in ransomNote:
        #     if l in magazine:
        #         result.append(True)
        #         magazine.remove(l)
        #     else:
        #         result.append(False)
        # return all(result)


        ########

        # ransomNoteCounts = Counter(ransomNote)
        # magazineCounts = Counter(magazine)
        
        # for char, count in ransomNoteCounts.items():
        #     if magazineCounts[char] < count:
        #         return False
                
        # return True
        ########

        char_counts = [0] * 26  # Для каждой буквы алфавита
        
        for char in magazine:
            char_counts[ord(char) - ord('a')] += 1
        
        for char in ransomNote:
            index = ord(char) - ord('a')
            if char_counts[index] == 0:
                return False
            char_counts[index] -= 1
            
        return True