import collections
import re


def mostCommonWord(paragraph: str, banned) -> str:
    words = []
    i = 0
    #change string to modified list
    for word in re.sub('[\W]', ' ', paragraph).lower().split():
        if word not in banned:
            words.append(word)

    # used counter
    c = collections.Counter(words)
    return c.most_common(1)[0][0]