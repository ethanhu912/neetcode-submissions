class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        index = 0
        same_prefix = True
        while same_prefix == True:
            for word in strs[1:]:
                if index >= len(word) or index >= len(strs[0]):
                    same_prefix = False
                    break
                elif word[index] != strs[0][index]:
                    same_prefix = False
                    break
            if index >= len(strs[0]):
                break
            if same_prefix == True:
                prefix += strs[0][index]
                print(strs[0][index])
                print(index)
                index += 1
        return prefix
            