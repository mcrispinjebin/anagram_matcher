from string_processor import AnagramMatcher


if __name__ == "__main__":
    words_list = []
    n = int(input("Enter number of strings: "))

    for i in range(0, n):
        word = str(input("Enter the word: "))
        words_list.append(word)
    matcher = AnagramMatcher(words_list)

    iter_count = 0
    while True:
        match_str = str(input("Enter the string to be matched: "))
        if not match_str:
            if iter_count < 3:
                print("Please enter valid match string")
                iter_count += 1
                continue
            else:
                print("Please enter valid match string, ending program")
                break

        matched_words = matcher.find(match_str)
        if matched_words:
            print("Matched string(s): ", matcher.find(match_str))
        else:
            print("No words matched for given string")

        iter_word = str(input("Enter to continue finding, else type NA: "))
        if iter_word == "NA":
            break
