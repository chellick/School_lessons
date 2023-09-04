"""
def generate_hashtag(s):
    if len(s) > 140 or len(s) == 0:
        return False
    else:
        a = s.title()
        a = a.replace(' ', '')
        return f'#{a}'
print(generate_hashtag(''))
"""

#_________________________________________________________________
"""
def duplicate_encode(word):
    from collections import Counter
    coll = Counter(word)
    for el in word:
        for key, value in coll:
            if el == key and value < 2:
                el = '('
            elif el == key and value > 2:
                el = ')'
    return word
print(duplicate_encode('qweqwe'))
"""
