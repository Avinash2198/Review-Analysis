#!C:\Users\saiav\AppData\Local\Programs\Python\Python36-32\python.exe


import cgi
import pandas as pd
import pymysql
from random import randint
import re
import csv



train_path = "data_IMDB/train/"



formData =cgi.FieldStorage()
names=formData.getvalue('names')
email =formData.getvalue('emailid')
review=formData.getvalue('review')
event=formData.getvalue('event')
rollno = formData.getvalue('rollno')
sentiment = ""

stopwords = open("stopwords.en.txt", 'r' , encoding="ISO-8859-1").read()
stopwords = stopwords.split("\n")



def unigram_process(data):
	from sklearn.feature_extraction.text import CountVectorizer
	vectorizer = CountVectorizer()
	vectorizer = vectorizer.fit(data)
	return vectorizer	

def retrieve_data(name="imdb_tr.csv", train=True):
	
	data = pd.read_csv(name,header=0, encoding = 'ISO-8859-1')
	X = data['text']
	
	if train:
		Y = data['polarity']
		return X, Y

	return X

def naivebayes_MultinomialNB(Xtrain, Ytrain, Xtest):
	from sklearn.naive_bayes import MultinomialNB
	clf = MultinomialNB()
	clf.fit(Xtrain, Ytrain)
	Ytest= clf.predict(Xtest)
	return Ytest

if __name__ == "__main__":
	
	
	
	[Xtrain, Ytrain] = retrieve_data()

	uni_vectorizer = unigram_process(Xtrain)
	Xtrain_uni = uni_vectorizer.transform(Xtrain)


	input_text = review
	


	d=[]
	d.append(input_text)
	Xtest_uni = uni_vectorizer.transform(d)
	
	Ytest_uni = naivebayes_MultinomialNB(Xtrain_uni, Ytrain, Xtest_uni)

	if Ytest_uni == 0:
		sentiment="neg"
	else:
		sentiment = "pos"
		
Id = randint(10000, 99999)



if(event=="fest"):
    db=pymysql.connect("localhost",user="root",password="",db="fest",autocommit=True)
    cursor=db.cursor()
    sqli="INSERT INTO all_reviews VALUES (\"%d\",\"%s\",\"%s\",\"%s\",\"%s\")" % (Id,names,email,review,sentiment)
    cursor.execute(sqli)
    if(sentiment=="pos"):
        sqlp="INSERT INTO postive VALUES (\"%d\",\"%s\")" % (Id,review)
        cursor.execute(sqlp)
    if(sentiment=="neg"):
        sqln="INSERT INTO negative VALUES (\"%d\",\"%s\")" % (Id,review)
        cursor.execute(sqln)
    db.close()
	
if(event=="intracollege"):
    db=pymysql.connect("localhost",user="root",password="",db="intra_college",autocommit=True)
    cursor=db.cursor()
    sqli="INSERT INTO all_reviews VALUES (\"%d\",\"%s\",\"%s\",\"%s\",\"%s\")" % (Id,names,rollno,review,sentiment)
    cursor.execute(sqli)
    if(sentiment=="pos"):
        sqlp="INSERT INTO postive VALUES (\"%d\",\"%s\")" % (Id,review)
        cursor.execute(sqlp)
    if(sentiment=="neg"):
        sqln="INSERT INTO negative VALUES (\"%d\",\"%s\")" % (Id,review)
        cursor.execute(sqln)
    db.close()


print (""" Content-type:text/html \n\n
<!DOCTYPE html>
<html lang="en">
<head>
<title>My review analysis</title>
</head>
<body>
<br><br><br>
<p><center><h3>Thank You for giving Feedback</h3></center></p>
<br><br><br>
<center><a href="index.html">BACK TO HOME PAGE</a></center>
</body>
</html>
""").format()
