from unlock_secrets import all_the_shit


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
def oumls(asciiValue):
    ouml = {
        229: 26, # å
        228: 27, # ä
        246: 28  # ö
    }

    return ouml.get(asciiValue)

noOfLetters = 29
result = ""
key = 'abcdefghijklmnopqrstuvwxyzåäö'

def decrypt(n, ciphertext):
    """Decrypt the string and return the plaintext"""
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % noOfLetters
            result += key[i]
        except ValueError:
            result += l

    return result

def crack_ceaser(msg):

    max = 0
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

    for char in msg:
        # å,ä & ö needs be taken extra care as their ascii value is not in series
        if ord(char) > 227:
            posInAlphabet = oumls(ord(char))
        else:
            # 97 = ascii code for a
            posInAlphabet = (ord(char) | 32) - 97

        if 0 <= posInAlphabet and posInAlphabet < noOfLetters:
            letterCount[posInAlphabet] += 1

    letterFreq = letterCount.copy()
    #print (letterFreq)

    for offSet in range(noOfLetters):

        for currLetter in range(noOfLetters):
            letterFreq[offSet] += (0.01 * letterCount[currLetter] * weight[((currLetter + offSet) % noOfLetters)])
            if (max < letterFreq[offSet]):
                max = letterFreq[offSet]

    #print (letterFreq)
    #print ("ans?: ", letterFreq.index(max))
    #print (((noOfLetters - letterFreq.index(max)) % noOfLetters))

    return decrypt(letterFreq.index(max), msg)

for msg in all_the_shit:
    print(crack_ceaser(msg))

'''
print("Round 1: ")
msg1 = "Dpygyp gzaöxåäayp aö påzghxxzaefp ftwskö töögefttö ägzppö åghpeep ztezxhxxzazex zppzaeep exypxfethxxö äppzgöfxxö."
print(crack_ceaser(msg1))
print("round 2:")
print(crack_ceaser("Aivpi rövisitöåäw iqpmöääii vqqv awquisiåäi uiixmzgv ägzqvgg määg tgpqitömmv sqqvämqåährmv åmqvgä pitsmqtmaiä."))
print("round 3:")
print(crack_ceaser("jsjod qvöwbj smev anrh tyäwlyo moeo eifgänicmnx noceä rsxaxwg nicpäcexm."))
print("round 4:")
print(crack_ceaser("ix ed eäaxtijä fkkijt ckejeäbjk aodjjäbrdötbat ckjjt däcxdir xiädx ed ittdkj åxhaakftbtt ckäijkjjtltijt ckeweijt."))
print("round 5:")
print(crack_ceaser("rol lmnwduwgw åb gl ibwnmld eghwo hblhbmewo daå bwdglmhgfw ggwgbe."))
'''





'''
<?php

function crack_caesar($str) {

	for ($off = 0; $off < 26; ++$off) {

		for ($i = 0; $i < 26; ++$i) {
			if ($max < ($s[$off]+= 0.01 * $c[$i] * $weight[($i + $off) % 26])) {
				$max = $s[$off];
			}
		}
	}
	return (26 - array_search($max, $s)) % 26;
}

?>
'''

