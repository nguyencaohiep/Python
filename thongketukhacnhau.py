import re

dict_words = {}

for i in range(int(input())):
    words = re.findall("\\w+", input().lower())
    for word in words:
        dict_words[word] = dict_words.get(word, 0) + 1

dict_words = sorted(dict_words.items(), key=lambda kv: (-kv[1], kv[0]))
for k, v in dict_words:
    print(f"{k} {v}")