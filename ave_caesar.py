from unlock_secrets import all_the_shit
import ngramscore as ns
from pycipherMod import Caesar
from break_caesar import break_caesar

'''
A : 12.22        K :  4.97        U :  5.01
B :  0.28        L :  5.76        V :  2.25
C :  0.28        M :  3.20        W :  0.09
D :  1.04        N :  8.83        X :  0.03
E :  7.97        O :  5.61        Y :  1.74
F :  0.19        P :  1.84        Z :  0.05
G :  0.39        Q :  0.01        Å :  0.00
H :  1.85        R :  2.87        Ä :  3.58
I : 10.82        S :  7.86        Ö :  0.44
J :  2.04        T :  8.75   
'''


def oumls(ascii_value):
    ouml = {
        229: 26,  # å
        228: 27,  # ä
        246: 28   # ö
    }

    return ouml.get(ascii_value)


noOfLetters = 29
result = ""
key = 'abcdefghijklmnopqrstuvwxyzåäö'


def decrypt(n, ciphertext):
    """Decrypt the string and return the plaintext"""
    decrypt_result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % noOfLetters
            decrypt_result += key[i]
        except ValueError:
            decrypt_result += l

    return decrypt_result


def crack_ceaser(curr_msg):

    max_value = 0
    weight = [
        12.22, 0.28, 0.28, 1.04, 7.97,
        0.19, 0.39, 1.85, 10.82, 2.04,
        4.97, 5.76, 3.20, 8.83, 5.61,
        1.84, 0.01, 2.87, 7.86, 8.75,
        5.01, 2.25, 0.09, 0.03, 1.74,
        0.05, 0.00, 3.58, 0.44
    ]
    letterCount = [
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0
    ]

    for char in curr_msg:
        # å,ä & ö needs be taken extra care as their ascii value is not in series
        if (ord(char) > 227):
            posInAlphabet = oumls(ord(char))
        else:
            # 97 = ascii code for a
            posInAlphabet = (ord(char) | 32) - 97

        if (0 <= posInAlphabet < noOfLetters):
            letterCount[posInAlphabet] += 1

    letterFreq = letterCount.copy()
    # print (letterFreq)

    for offSet in range(noOfLetters):

        for currLetter in range(noOfLetters):
            letterFreq[offSet] += (0.01 * letterCount[currLetter] * weight[((currLetter + offSet) % noOfLetters)])
            if (max_value < letterFreq[offSet]):
                max_value = letterFreq[offSet]

    # print (letterFreq)
    # print (letterCount)
    # print("ans?: ", letterFreq.index(max_value))
    # print (((noOfLetters - letterFreq.index(max_value)) % noOfLetters))

    return decrypt(letterFreq.index(max_value), curr_msg)


fitness = ns.NgramScore('finnish_quadgrams.txt')
"""
ctext = 'Aivpi rövisitöåäw iqpmöääii vqqv awquisiåäi uiixmzgv ägzqvgg määg tgpqitömmv sqqvämqåährmv åmqvgä pitsmqtmaiä'
crack_ceaser(ctext)
"""
hits = 0

for msg in all_the_shit:
    origScore = fitness.score(msg)
    # print("fitness unDec: ", origScore)
    # print(msg)
    decMsg = crack_ceaser(msg)
    decMsg2 = Caesar(break_caesar(msg)[1]).decipher(msg, True)
    diyScore = fitness.score(decMsg)
    # print("fitness diy: ", diyScore)
    # print(decMsg)
    pyModScore = fitness.score(decMsg2)
    # print("fitness pyMod: ", pyModScore)
    # print(decMsg2)
    # print("Differences = ", abs(origScore) - abs(diyScore), " / ", abs(origScore) - abs(pyModScore))
    # print("--- DONE! ---")

    if (abs(origScore) - abs(pyModScore) > 120):
        print("fitness unDec: ", origScore)
        print(msg)
        print("fitness diy: ", diyScore)
        print(decMsg)
        print("fitness pyMod: ", pyModScore)
        print(decMsg2)
        print("Differences = ", abs(origScore) - abs(diyScore), " / ", abs(origScore) - abs(pyModScore))
        print("--- DONE! ---")
        hits += 1

print("Hits: ", hits)

# print(crack_ceaser("Aivpi rövisitöåäw iqpmöääii vqqv awquisiåäi uiixmzgv ägzqvgg määg tgpqitömmv sqqvämqåährmv åmqvgä pitsmqtmaiä."))
