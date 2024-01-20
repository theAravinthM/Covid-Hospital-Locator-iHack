import json
from difflib import get_close_matches

jsonfile = json.load(open(r"./data1.json"))
word = input("enter the location: ")

def check(d):
    d = d.lower()
    if d in jsonfile:
        return jsonfile[d]
    elif len(get_close_matches(d,jsonfile.keys())) > 0:
        choice = input("Did you mean %s , Enter Y for YES, N for NO " %get_close_matches(d,jsonfile.keys())[0])
        if choice == "Y" or "y":
            return jsonfile[get_close_matches(d,jsonfile.keys())[0]]
        elif choice == "N" or "n":
            return "The location doesn't exist, please enter the correct location"
        else:
            return "you enterd the wrong choice"
    else:
        return "The location doesn't exist, please enter the correct location"

result = (check(word))
print("\n\nThe available hostpitals are:")
if type(result) == list:
    for i in result:
        print(i)
else:
    print(result)
