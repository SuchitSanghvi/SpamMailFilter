from nltk.corpus import words
from nltk.tokenize import RegexpTokenizer
from nltk import FreqDist
import nltk


def freqdata(data):
	# Tokenizing the sentence
	tokenizer = RegexpTokenizer(r'\w+')
	act_words = tokenizer.tokenize(data)
	allword = words.words()



	filtered_text = []

	for w in act_words:
		w = w.lower()
		if w in allword:
			if(len(w)>2):
				filtered_text.append(w)

	frequencydata = FreqDist(filtered_text)

	return frequencydata

def freqdata1(data):
	wordtokens = nltk.word_tokenize(data,language='english')

	filtered_text = []

	for w in wordtokens:
		w = w.lower()
		if(len(w)>2):
			filtered_text.append(w)

	frequencydata = FreqDist(filtered_text)

	return frequencydata



