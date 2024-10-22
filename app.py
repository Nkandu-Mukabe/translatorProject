# B language rules:
#
# Any vowel is followed by a b and then that same vowel
# ----------
# dog => dobog
# cat => cabat


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            translation = translation + letter + "b" + letter.lower()
        else:
            translation = translation + letter
    return translation


print(translate(input("enter a phrase: ")))
