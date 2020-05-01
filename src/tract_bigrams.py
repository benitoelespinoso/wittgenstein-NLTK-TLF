import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
from nltk.collocations import *
from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder
from operator import itemgetter
from nltk import FreqDist
WNL = nltk.WordNetLemmatizer()
# 
f = open('C:\\Users\\guille\\Google Drive\\NLTK\\DEF\\ficheros_in\\Tratactus\\ing\\en.tratactus.txt', encoding="utf8")
raw = f.read()
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)
words = [w.lower() for w in tokens]
#
def prepareStopWords():
 stopwordsList = []
 stopwordsList = stopwords.words('english')
 stopwordsList.append('The')
 stopwordsList.append('I')
 stopwordsList.append('It')
 stopwordsList.append('In')
 stopwordsList.append('Is')
 stopwordsList.append('p')
 stopwordsList.append('q')
 stopwordsList.append('1')
 stopwordsList.append('X')
 stopwordsList.append('=')
 stopwordsList.append('/')
 stopwordsList.append('2')
 stopwordsList.append('0')
 stopwordsList.append('+')
 stopwordsList.append('dx')
 stopwordsList.append('fx')
 stopwordsList.append('N')
 stopwordsList.append('E')
 stopwordsList.append('x')
 stopwordsList.append('z')
 stopwordsList.append('Pp')
 stopwordsList.append('Pq')
 
 return stopwordsList


stopwords = prepareStopWords()

# fdist = FreqDist(text)
# fdist_no_punc_no_stopwords = nltk.FreqDist(dict((word, freq) for word, freq in fdist.items() if word not in stopwords and word.isalpha()))

# bigramas
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(
 words)
finder.nbest(bigram_measures.pmi, 10)
finder.apply_freq_filter(3)
finder.nbest(bigram_measures.pmi, 10)

# WC para los bigramas mas frecuentes
stopWords = stopwords
text_content = [''.join(re.split("[ .,;:!?‘’``''@#$%^_&*()<>{}~\n\t\\\-]", word)) for word in text]

text_content = [word for word in text_content if word not in stopWords]
text_content = [s for s in text_content if len(s) != 0]
text_content = [WNL.lemmatize(t) for t in text_content]
finder = BigramCollocationFinder.from_words(text_content)
bigram_measures = BigramAssocMeasures()
scored = finder.score_ngrams(bigram_measures.raw_freq)
scoredList = sorted(scored, key=itemgetter(1), reverse=True)
word_dict = {}
listLen = len(scoredList)

for i in range(listLen):
 word_dict['_'.join(scoredList[i][0])] = scoredList[i][1]

WC_height = 500
WC_width = 1000
WC_max_words = 100
wordCloud = WordCloud(max_words=WC_max_words, height=WC_height, width=WC_width)
wordCloud.generate_from_frequencies(word_dict)
plt.title('Most frequently occurring bigrams connected with an underscore_')
plt.imshow(wordCloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# WC de los bigramas menos frecuentes, salvar fichero
scoredList = sorted(scored, key=itemgetter(1))
scoredListLen = len(scoredList)-1
maxLenCnt = 0
MINSCORE = 0.000265

indx = 0
while (indx < scoredListLen) and (scoredList[indx][1] < MINSCORE):
 indx += 1

word_dict2 = {}
while (indx < scoredListLen) and (maxLenCnt < WC_max_words):
 word_dict2['_'.join(scoredList[indx][0])] = scoredList[indx][1]
 indx +=  1
 maxLenCnt += 1

if len(word_dict2) > 0:
 wordCloud.generate_from_frequencies(word_dict2)
 plt.title('Least frequently occurring bigrams connected with an underscore_')
 plt.imshow(wordCloud, interpolation='bilinear')
 plt.axis("off")
 plt.show()
 # wordCloud.to_file("WordCloud_Bigrams_Infrequent_words.png")
else:
 print("\nThere were no words to display in the word cloud.")

