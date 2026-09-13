class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_of_words = {}
        grouped_anagrams = []
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in dict_of_words:
                dict_of_words[sorted_word] = []
                dict_of_words[sorted_word].append(word)
            else:
                dict_of_words[sorted_word].append(word)
        
        for sorted_word in dict_of_words:
            grouped_anagrams.append(dict_of_words[sorted_word])
        
        return grouped_anagrams