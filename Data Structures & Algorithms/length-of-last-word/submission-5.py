class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        print(s)

        index = len(s)-1
        print(index)
        count = 0
        print(count)

        while s[index] != " " and index >= 0:
            count += 1
            index -= 1
        
        return count