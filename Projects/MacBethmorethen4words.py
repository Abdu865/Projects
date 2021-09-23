import string
from collections import Counter

Cheem= open('macbeth.txt')
McBeth = Cheem.readlines()
list_of_words_longer_then_five=[] # letter words from raw txt into this list
tallied_words_longer_then_five={} # counted words from list words
for line in McBeth:
    for word in line.translate(str.maketrans('', '', string.punctuation)).lower().split():
    # Strips punctiation and makes all letters lowercase. Then slits at each space
        if len(word) > 4 and not (word == "macbeth"):
            list_of_words_longer_then_five.append(word)

counter_list= Counter(list_of_words_longer_then_five)
print(counter_list)



#import re
#match = re.findall(r'([^A-Z\s]|[^a-z\s])|((^|\s)[a-z]{4,7}(\s|$))', McBeth)
#print(match)
###
