# Hunter Davis
# huntertigerdavis@gmail.com
# CECS 378 Sec 01 Lab 1

import string
import itertools


def main():
    ciphertext1 = "fqjcb rwjwj vnjax bnkhj whxcq nawjv nfxdu mbvnu ujbbf nnc"
    ciphertext2 = " oczmz vmzor jocdi bnojv dhvod igdaz admno ojbzo rcvot jprvi oviyv aozmo cvooj ziejt dojig toczr dnzno " \
                  "jahvi fdiyv xcdzq zoczn zxjiy"
    ciphertext3 = "ejitp spawa qleji taiul rtwll rflrl laoat wsqqj atgac kthls iraoa twlpl qjatw jufrh lhuts qataq itats " \
                  "aittk stqfj cae"
    ciphertext4 = " iyhqz ewqin azqej shayz niqbe aheum hnmnj jaqii yuexq ayqkn jbeuq iihed yzhni ifnun sayiz yudhe sqshu " \
                  "qesqa iluym qkque aqaqm oejjs hqzyu jdzqa diesh niznj jayzy uiqhq vayzq shsnj jejjz nshna hnmyt isnae " \
                  "sqfun dqzew qiead zevqi zhnjq shqze udqai jrmtq uishq ifnun siqa uoij qqfni syyle iszhn bhmei squih " \
                  "nimnx hsead shqmr udququaqeu iisqe jshnj oihyy snaxs hqihe lsilu ymhni tyz"

    plaintext1 = " He who fights with monsters should look to it that he himself does not become a monster. " \
                 "And if you gaze long into an abyss , the abyss also gazes into you."

    plaintext2 = "There is a theory which states that if ever anybody discovers exactly what the Universe is for and " \
                 "why it is here, it will instantly disappear and be replaced by something even more bizarre and " \
                 "inexplicable. There is another theory which states that this has already happened."

    plaintext3 = "Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in " \
                 "my soul; whenever I find myself involuntarily pausing before coffin warehouses , and bringing up " \
                 "the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, " \
                 "that it requires a strong moral principle to prevent me from deliberately stepping into the street, " \
                 "and methodically knocking people’s hats off - then, I account it high time to get to sea as soon as I can."



    # Ciphertext 1
    ciphertext1 = str(ciphertext1)
    ciphertext1 = white_space_removal(ciphertext1)
    #print(ciphertext1)
    alphabet = string.ascii_lowercase
    #print(alphabet)
    caesar_cipher(ciphertext1, alphabet)
    #frequency_checker(ciphertext1)

    # Ciphertext 2
    ciphertext2 = str(ciphertext2)
    #print("Len of ciphertext2:", len(ciphertext2))

    ciphertext2 = white_space_removal(ciphertext2)
    #print(ciphertext2)
    #alphabet = string.ascii_lowercase
    caesar_cipher(ciphertext2, alphabet)
    #frequency_checker(ciphertext2)

    #print(possible_phrases_dict) # Not in main

    # ciphertext3 = str(ciphertext3)
    # ciphertext3 = white_space_removal(ciphertext3)
    # caesar_cipher(ciphertext3, alphabet)
    #
    # ciphertext4 = str(ciphertext4)
    # ciphertext4 = white_space_removal(ciphertext4)
    # caesar_cipher(ciphertext4, alphabet)





    # Part 2: Encryption: Substitution
    key1 = "gvplhqaxcwjtrnukiebsfdyzom"

    scrambled = substitution_encrypter(plaintext1, key1)
    print("Encrypted:", scrambled)
    plain = substitution_decrypter(scrambled, key1)
    print("Unencrypted:", plain)

    scrambled = substitution_encrypter(plaintext2, key1)
    print("Encrypted:", scrambled)
    plain = substitution_decrypter(scrambled, key1)
    print("Unencrypted:", plain)

    scrambled = substitution_encrypter(plaintext3, key1)
    print("Encrypted:", scrambled)
    plain = substitution_decrypter(scrambled, key1)
    print("Unencrypted:", plain)


    exit()
    # Calling substitution cipher
    substitution_cipher(ciphertext3)
    substitution_cipher(ciphertext4)


def white_space_removal(ciphertext):
    # Removing whitespace & non-alpha characters
    ciphertext = ciphertext.replace(" ", "")
    ciphertext = ciphertext.replace(".", "")
    ciphertext = ciphertext.replace(",", "")
    ciphertext = ciphertext.replace(";", "")
    ciphertext = ciphertext.replace("'", "")
    ciphertext = ciphertext.replace("-", "")
    ciphertext = ciphertext.replace("\'", "")
    ciphertext = ciphertext.replace("’", "")
    ciphertext = ciphertext.replace("`", "")
    ciphertext = ciphertext.replace("~", "")
    ciphertext = ciphertext.replace("|", "")
    ciphertext = ciphertext.lower()
    #print(ciphertext)
    return ciphertext

def caesar_cipher(ciphertext, alphabet):
    # Shift cipher
    # Creates all permutations of caesar_cipher
    #copy_cipher = ciphertext

    # Dictionary to keep score of each decipher attempt
    possible_phrases_dict = dict()

    # Looping through each character in the alphabet
    for key in range(len(alphabet)):
        translated = ''
        # Looping through each character in ciphertext
        for symbol in ciphertext:
            # Check if that letter is in the alphabet
            if symbol in alphabet:
                # Shifting letters
                num = alphabet.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(alphabet)
                if num < len(alphabet):
                    translated = translated + alphabet[num]
            else:
                translated = translated + symbol
        print("Key " + str(key) + ": " + str(translated))
        var = frequency_checker(translated)
        if var is not None:
            possible_phrases_dict.update(var)

    #print(possible_phrases_dict)
    # Sort and print by freq values
    possible_phrases_dict = sorted(possible_phrases_dict.items(), reverse=True, key=lambda x: x[1])
    # Printing sorted dictionary values by most likely score
    print("Point Totals:")
    for element in possible_phrases_dict:
        print(element[0], "::", element[1])
    # Printing the highest score which is the most likely answer
    print("Most likely answer:", possible_phrases_dict[0], "\n")

# Search each line and count most common letter, triads, quads, etc.
def frequency_checker(ciphertext):
    #global possible_phrases_dict

    # Search for most e, then t, a, o, i
    letter_frequency = \
        {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0,
         "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}

    duo_frequency = ["of", "to", "in", "it", "is", "be", "as", "at", "so", "we", "he", "by", "or", "on", "do", "if",
                     "me", "my", "an", "no", "us", "am", "th", "er", "re", "he", "ed", "nd", "ha", "en", "es", "nt",
                     "ea", "ti", "st", "io", "le", "ou", "ar", "as", "de", "rt", "ve"]

    triad_frequency = ["the", "and", "for", "are", "but", "not", "you", "all", "any", "can", "had", "her", "was", "one",
                       "our", "out", "day", "get", "has", "him", "his", "how", "man", "new", "now", "old", "see", "two",
                       "way", "who", "boy", "did", "its", "let", "put", "say", "she", "too", "use", "tha", "ent", "ion",
                       "tio", "nde", "nce", "edt", "tis", "oft", "sth", "men"]

    quad_frequency = ["that", "with", "have", "this", "will", "your", "from", "they", "know", "want", "been", "good",
                      "much", "some", "time"]

    #print(ciphertext)

    letter_counter = 0
    duo_counter = 0
    triad_counter = 0
    quad_counter = 0

    i = 0
    while i < len(triad_frequency):
        if i < len(duo_frequency):
            if duo_frequency[i] in ciphertext:
                duo_counter += 1
        if i < len(triad_frequency):
            if triad_frequency[i] in ciphertext:
                triad_counter += 1
        if i < len(quad_frequency):
            if quad_frequency[i] in ciphertext:
                quad_counter += 1
        i += 1
    print(duo_counter, triad_counter, quad_counter)

    # Old code; is updated above^
    # for i in duo_frequency:
    #     if i in ciphertext:
    #         duo_counter += 1
    # print(duo_counter)
    #
    #
    # for i in triad_frequency:
    #     if i in ciphertext:
    #         triad_counter += 1
    # print(triad_counter)
    #
    # for i in quad_frequency:
    #     if i in ciphertext:
    #         quad_counter += 1
    # print(quad_counter)

    freq_score = duo_counter + triad_counter + quad_counter

    # Add up all possible combinations, add to dictionary, display from highest to lowest counts
    if duo_counter > 0 or triad_counter > 0: # and quad_counter > 0:
        # Add to dictionary
        #print("Appending " + ciphertext)
        temp_dict = {ciphertext: freq_score}
        return temp_dict
    else:
        return None

def substitution_cipher(ciphertext):
    # Substitution Cipher
    # Creating all possible keys:
    # Method for solving variants of the substitution cipher
    # Find most common letter, set that as E
    # Backwards alphabet, shifted alphabet as key,
    # Analyze qwertyuiopasdfghjklzxcvbnm
    # AEIOUYBCDFGHJKLMNPQRSTVWXZ
    # Initializing our default key: Just the alphabet
    alphabet = list(string.ascii_lowercase)
    upper_alphabet = list(string.ascii_uppercase)
    possible_trans_dict = dict()
    counter = 0
    letter_frequency = \
        {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0,
         "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
    #temp_cipher = ciphertext
    ciphertext = list(ciphertext)
    #print(ciphertext)
    temp_ciphertext = list(ciphertext)
    for i in itertools.permutations(alphabet):
        #temp_ciphertext = list(ciphertext)
        #print(i)
        key = list(i)
        #print("Key:", key)

        # Substitute:
        # Loop through ciphertext;
        # Iterate a string like this:
        # alphabet[key.index(ciphertext[i])]
        #print("Old:", ciphertext) # SHOULD BE: ejitp!!
        for j in range(len(temp_ciphertext)):
            temp_ciphertext[j] = alphabet[key.index(temp_ciphertext[j])]
        # Translated
        #print("New:", temp_ciphertext, "\n")


        # Frequency Check
        temp_ciphertext2 = ''.join(temp_ciphertext)
        #print(temp_ciphertext2)
        var = frequency_checker(temp_ciphertext2)
        if var is not None:
            possible_trans_dict.update(var)
            # Check if the value of var going in is larger than the one already there
            # if var.values() in possible_trans_dict.values():
            #     possible_trans_dict.update(var)
            # for k in possible_trans_dict:
            #     if possible_trans_dict[k] <= var.values():
            #         possible_trans_dict.update(var)
        print(var)

        if counter > 90000:
            print(possible_trans_dict)
            exit()
        counter += 1

    possible_trans_dict = dict(possible_trans_dict)
    possible_trans_dict = sorted(possible_trans_dict.items(), reverse=True, key=lambda x: x[1])
    # Printing sorted dictionary values by most likely score
    print("Point Totals:")
    for element in possible_trans_dict:
        print(element[0], ":", element[1])
    # Printing the highest score which is the most likely answer
    #print("Most likely answer:", possible_trans_dict[0], "\n")

def substitution_encrypter(plaintext, cryptokey):

    plaintext = str(white_space_removal(plaintext))
    alphabet = list(string.ascii_lowercase)
    #print(plaintext)
    temp_ciphertext = list(plaintext)
    # temp_ciphertext = list(ciphertext)
    # print(i)
    key = list(cryptokey)
    # print("Key:", key)

    # Substitute:
    # Loop through ciphertext;
    # Iterate a string like this:
    # alphabet[key.index(ciphertext[i])]
    # print("Old:", ciphertext) # SHOULD BE: ejitp!!
    for j in range(len(temp_ciphertext)):
        temp_ciphertext[j] = alphabet[key.index(temp_ciphertext[j])]
    # Translated

    temp_ciphertext = ''.join(temp_ciphertext)
    #print("New:", temp_ciphertext, "\n")
    return temp_ciphertext

def substitution_decrypter(ciphertext, cryptokey):

    ciphertext = str(white_space_removal(ciphertext))
    alphabet = list(string.ascii_lowercase)

    ciphertext = list(ciphertext)
    #print(ciphertext)
    temp_ciphertext = list(ciphertext)
    # temp_ciphertext = list(ciphertext)
    # print(i)
    key = list(cryptokey)
    # print("Key:", key)

    # Substitute:
    # Loop through ciphertext;
    # Iterate a string like this:
    # alphabet[key.index(ciphertext[i])]
    # print("Old:", ciphertext) # SHOULD BE: ejitp!!
    for j in range(len(temp_ciphertext)):
        temp_ciphertext[j] = key[alphabet.index(temp_ciphertext[j])]
    # Translated
    # print("New:", temp_ciphertext, "\n")
    temp_ciphertext = ''.join(temp_ciphertext)
    return temp_ciphertext

main()