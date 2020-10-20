import json
from difflib import get_close_matches

data = json.load(open('data.json'))
# print(type(data))


def translate(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        user_recom = input(("Did you mean %s instead Y or N  " %
                            get_close_matches(word, data.keys())[0])).lower()
        if user_recom == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif user_recom == 'n':
            return 'Word does not exist'
        else:
            return 'Incorrect input'

    else:
        return "Sorry Your Word Does Not Exist"


word = input("Enter the word you'd like to search for: ").lower()

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
