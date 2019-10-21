import re
import sys

sys.path.append('/pycipherMod/')

from ngramscore import NgramScore
from pycipherMod import Caesar

fitness = NgramScore('finnish_quadgrams.txt')  # load our quadgram statistics


def break_caesar(crypted_text):
    # make sure ciphertext has all spacing/punc removed and is uppercase
    # ctext = re.sub('[^A-Ö]', '', ctext.upper())
    # print(crypted_text)
    # try all possible keys, return the one with the highest fitness
    scores = []
    for i in range(29):
        scores.append((fitness.score(Caesar(i).decipher(crypted_text)), i))
    # print("max value: ", max(scores))
    return max(scores)


# example ciphertext
# ctext = 'Aivpi rövisitöåäw iqpmöääii vqqv awquisiåäi uiixmzgv ägzqvgg määg tgpqitömmv sqqvämqåährmv åmqvgä pitsmqtmaiä'
# max_key = break_caesar(ctext)

# print('best candidate with key (a,b) = ' + str(max_key[1]) + ':')
# print(Caesar(max_key[1]).decipher(ctext))
