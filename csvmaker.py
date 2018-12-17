#!C:\Users\saiav\AppData\Local\Programs\Python\Python36-32\python.exe

import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer



def imdb_data_preprocess(inpath, outpath="./", name="imdb_tr.csv", mix=False):
	import pandas as pd 
	from pandas import DataFrame, read_csv
	import os
	import csv 
	import numpy as np 

	stopwords = open("stopwords.en.txt", 'r' , encoding="ISO-8859-1").read()
	stopwords = stopwords.split("\n")

	indices = []
	text = []
	rating = []

	i =  0 

	for filename in os.listdir(inpath+"pos"):
		data = open(inpath+"pos/"+filename, 'r' , encoding="ISO-8859-1").read()
		data = process(data, stopwords)

		indices.append(i)
		text.append(data)
		rating.append("1")
		i = i + 1

	for filename in os.listdir(inpath+"neg"):
		data = open(inpath+"neg/"+filename, 'r' , encoding="ISO-8859-1").read()
		data = process(data, stopwords)
		indices.append(i)
		text.append(data)
		rating.append("0")
		i = i + 1

	Dataset = list(zip(indices,text,rating))
	
	if mix:
		np.random.shuffle(Dataset)

	df = pd.DataFrame(data = Dataset, columns=['row_Number', 'text', 'polarity'])
	df.to_csv(outpath+name, index=False, header=True)

	pass


def process(sentence, stopwords):


	lemmatizer = WordNetLemmatizer()
	tokenizer = RegexpTokenizer(r'\w+')


	sentencewords = tokenizer.tokenize(sentence)
	
	pos_tagged = nltk.pos_tag(sentencewords)
	resultwords = [ word for word,tag in pos_tagged if tag!= 'NNP' and tag != "NNPS"]

	resultwords  = [lemmatizer.lemmatize(word) for word in resultwords if word.lower() not in stopwords]
	result = ' '.join(resultwords)
	return result
	
imdb_data_preprocess(inpath=train_path, mix=True)
