# Anagram Matcher

CLI Application that receives list of words and a match string to match its anagram words
---

[Python 3.9](https://www.python.org/downloads/release/python-390/)

---

**Contents**

1. [Testing](#testing)
1. [Q/A](#q/a)

---

### Testing ###

1. run the main.py in the repo to run the application.
1. Unit test cases are added in test_string_processor.py file. 

---

### Q/A ###

1. Total Time complexity : O(n*s(log(s))), Space complexity: O(n), <br /> n - len of input words in list, s - len of string to be matched <br /><br /> If constructor execution is left since it is prepopulated time complexity is O(slog(s)) <br /> <br /> 
2. The system can handle more load on find since the response time is minimal due to pre populating the hash map. <br /> Even the system can handle more input words in constructor, but need to find time lag between prepopulating and find.
---

---