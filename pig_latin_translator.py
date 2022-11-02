print("\n"
      "English to Pig Latin Translator"
      "\n\n"
      "Notes for using this translator:"
      "\n"
      "   1. The 26 characters in the English alphabet (both uppercase and lowercase) are permitted."
      "\n"
      "   2. Punctuation marks are permitted, including periods, question marks, exclamation marks,\n"
      "      commas, and apostrophes."
      "\n")
user_input = input("Enter the word or phrase you wish to translate: ")
# user_input = "This is Sample text."
print("\n")


def valid_input(w):
    for character in w:
        if character.lower() not in "abcdefghijklmnopqrstuvwxyz" and character not in " .,!?'":
            print("error - invalid character input:")
            for character in w:
                if character.lower() not in "abcdefghijklmnopqrstuvwxyz" and character not in " .,!?'":
                    print(f"({character})")
            quit()


valid_input(user_input)
user_input_list = user_input.split()


def find_beginning_capitalization(x):
    user_input_beginning_capitalization = []
    for word in x:
        if word[0].isupper():
            user_input_beginning_capitalization.append([word, True])
        elif word[0].islower():
            user_input_beginning_capitalization.append([word, False])
        else:
            print("error - punctuation not permitted before a word:")
            for word in x:
                if word[0].isupper():
                    print("")
                elif word[0].islower():
                    print("")
                else:
                    print(f"({word})")
            quit()
    return user_input_beginning_capitalization


list_with_capitalization = find_beginning_capitalization(user_input_list)


def find_ending_punctuation(y):
    user_input_ending_punctuation = []
    for term in y:
        if term[0][-1] in ".,!?'":
            user_input_ending_punctuation.append([term[0], term[1], term[0][-1]])
        else:
            user_input_ending_punctuation.append([term[0], term[1], "no_punctuation"])
    return user_input_ending_punctuation


list_with_punctuation_and_capitalization = find_ending_punctuation(list_with_capitalization)


def translate(z):
    translation = ""
    for group in z:
        if group[1]:
            if group[2] in ".,!?'":
                if len(group[0]) == 2:
                    translation = translation + group[0][0] + "ay" + group[0][-1] + " "
                else:
                    translation = translation + group[0][1].upper() + group[0][2:-1] + group[0][0].lower() \
                              + "ay" + group[0][-1] + " "
            else:
                if len(group[0]) == 1:
                    translation = translation + group[0][0].upper() + "ay "
                else:
                    translation = translation + group[0][1].upper() + group[0][2:] + group[0][0].lower() + "ay "
        else:
            if group[2] in ".,!?'":
                translation = translation + group[0][1:-1] + group[0][0] + "ay" + group[0][-1] + " "
            else:
                translation = translation + group[0][1:] + group[0][0] + "ay "
    return translation


print(translate(list_with_punctuation_and_capitalization))
print("\n")
