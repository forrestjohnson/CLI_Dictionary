import json
from difflib import SequenceMatcher

def find_similar(OBJ_dictionary, word):
    ratios = []
    for dict_word in OBJ_dictionary.keys():
        ratio = SequenceMatcher(None, word.lower(), dict_word.lower()).ratio()
        if ratio >= 0.6:
            ratios.append((ratio, dict_word))
    return ratios

def print_definition(def_list):
    for definition in def_list:
        print(definition)

def print_def_not_found():
    print("The word doesn't exist. Please double check it.")

def get_Y_or_N(closest_word):
    Y_or_N = input(f'Did you mean {closest_word} instead? Enter Y if yes, or N if no: ')
    return Y_or_N.lower() == 'y'

if __name__ == "__main__":
    with open("data.json", "r") as JSON_dictionary:
        OBJ_dictionary = {k: v for k, v in json.load(JSON_dictionary).items()}
    
    word = input("Enter word: ")
    found_match = False
    for dict_word in OBJ_dictionary.keys():
        if word.lower() == dict_word.lower():
            found_match = True
            match_word = dict_word
            break
    
    if found_match:
        print_definition(OBJ_dictionary[match_word])
    else:
        ratios = find_similar(OBJ_dictionary, word)
        if ratios and get_Y_or_N(max(ratios)[1]):
            print_definition(OBJ_dictionary[max(ratios)[1]])
        else:
            print_def_not_found()
