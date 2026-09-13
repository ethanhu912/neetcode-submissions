class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        substrings = []
        for word1 in words:
            for word2 in words[words.index(word1)+1:]:
                if word1 in word2:
                    substrings.append(word1)
                    break
        return substrings
                