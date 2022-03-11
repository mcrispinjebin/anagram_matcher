class AnagramMatcher:
    """
    Anagram Matcher class gets the list of words in the constructor, sorts each word and prepopulates a hash map
    with sorted word against the original words. FInd method fetches the anagram word from the hash map
    """
    def __init__(self, list_str: list[str]):
        self.input_list = list_str
        self.populated_map = dict()
        self.pre_populate_hash_map()

    def pre_populate_hash_map(self):
        """
        Sorts each word in the input list and stores the sorted word with the list of original input words
        :return:
        """
        for word in self.input_list:
            sorted_word = "".join(sorted(word))

            if sorted_word in self.populated_map:
                self.populated_map[sorted_word].append(word)
            else:
                self.populated_map[sorted_word] = [word]

    def find(self, match_str: str) -> str:
        """
        Sorts the match str provided as str and checks against the hash map and returns the strings in csv format.
        :param match_str: str
        :return:
        """
        sorted_match_str = "".join(sorted(match_str))
        if sorted_match_str in self.populated_map:
            return ", ".join(self.populated_map[sorted_match_str])
        else:
            return ""
