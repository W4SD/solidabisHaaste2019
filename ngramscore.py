# -- coding: utf-8 --
from math import log10


class NgramScore(object):
    def __init__(self, ngramfile, sep=' '):
        """ load a file containing ngrams and counts, calculate log probabilities """
        self.ngrams = {}

        with open(ngramfile, 'r', encoding='utf-8') as ngramFileHandler:
            for line in ngramFileHandler:
                key, count = line.split(sep)
                self.ngrams[key] = int(count)
        # eli täs kohtaa pitäs laskee per avain pituus
        self.L = len(self.ngrams.keys())
        self.N = sum(self.ngrams.values())
        # calculate log probabilities
        for key in self.ngrams.keys():
            self.ngrams[key] = log10(float(self.ngrams[key]) / self.N)
        self.floor = log10(0.01 / self.N)

    def score(self, text):
        """ compute the score of text """
        score = 0
        ngram_items = self.ngrams.__getitem__
        print("typeof items: ", type(ngram_items))
        self.ngrams
        # täs haetaan et jos tää määrä kirjaimii täst lauseest löyty ni lisätä score
        for i in range(len(text)):
            if i in self.ngrams:
                print("HIT")
                score += self.ngrams.__getitem__(text[i:i + self.L])
            else:
                score += self.floor
        return score


ns_fitness = NgramScore('finnish_monograms.txt')
print("typeOf:", type(ns_fitness))
# ns_fitness = NgramScore('finnish_quadgrams.txt')
# ns_fitness = NgramScore('english_quadgrams.txt')
uncrypted = 'köunidm oöqjdsdhkkö nm jåxsx oxäqågsdkdlårrå dmshrså kööidllöksö öktddksö iö sömrrhinhcdm intjnrrö nm nkkts öhdloöö dmdllåm mtnqdloöö onkudö.'
test_message = 'lavojen parketeilla on käyty pyörähtelemässä entistä laajemmalta alueelta ja tanssijoiden joukossa on ollut aiempaa enemmän nuorempaa polvea.'
print(ns_fitness.score(test_message))
print(ns_fitness.score(uncrypted))

