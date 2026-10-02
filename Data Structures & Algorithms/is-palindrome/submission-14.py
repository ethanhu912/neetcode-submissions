class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for letter in s:
            if letter.isalnum():
                new_s += letter
        
        new_s = new_s.lower()
        print(new_s)

        pointer1 = 0
        pointer2 = len(new_s) - 1

        while pointer1 < pointer2:
            if new_s[pointer1] != new_s[pointer2]:
                print(str(pointer1) + " " + str(pointer2))
                return False
            pointer1 += 1
            pointer2 -= 1

        return True