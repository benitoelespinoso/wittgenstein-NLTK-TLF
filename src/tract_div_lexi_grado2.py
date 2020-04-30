import nltk
from nltk.corpus import PlaintextCorpusReader
corpus_root = r'C:\Users\guille\Google Drive\NLTK\DEF\ficheros_in\Tratactus\esp\afo'
from nltk import FreqDist
newcorpus = PlaintextCorpusReader(corpus_root, '.*')
tokens = nltk.word_tokenize(newcorpus.raw())
text = nltk.Text(tokens)
stopwords = nltk.corpus.stopwords.words('spanish')

from nltk import word_tokenize
import matplotlib.pyplot as plt

lexDiver = []
storyLen = []
len2id = {}

for fileid in newcorpus.fileids():
     tempLen = len(newcorpus.raw(fileid))
     storyLen.append(tempLen)
     len2id[tempLen] = fileid

for fileid in newcorpus.fileids():
 words = [w for w in word_tokenize(newcorpus.raw(fileid)) if w.isalpha()]
 lD = len(words) / float(len(set(words)))
 lexDiver.append(round(lD, 2))

lenDiverPairs = zip(storyLen, lexDiver)
u = list(lenDiverPairs)
u.sort(key=lambda pair: pair[0])
X = [l for (l,d) in u]
Y = [d for (l,d) in u]

plt.figure()
plt.scatter(X, Y)
offset = (plt.gca().get_xticks()[1] - plt.gca().get_xticks()[0]) / 10
for (pt, label) in enumerate(X):
    plt.annotate(len2id[label],
                  xy=(X[pt], Y[pt]),
                  xytext=(X[pt]+offset, Y[pt]))

plt.xlabel('Story length')
plt.ylabel('Lexical diversity')
plt.grid()
plt.show()
# con liena de regresion
from scipy import stats
pNames = ['slope', 'intercept', 'r_value', 'p_value', 'std_err']
parameters = stats.linregress(X,Y)
	
X = [l for (l,d) in u]
Y = [d for (l,d) in u]
from numpy import array
aX = array(X)
rY = parameters[0]*aX + parameters[1]
plt.figure()

plt.scatter(X, Y)

plt.plot(X, rY, 'r')

offset = (plt.gca().get_xticks()[1]-plt.gca().get_xticks()[0])/10

for (pt, label) in enumerate(X):
 plt.annotate(len2id[label],
  xy=(X[pt], Y[pt]),
  xytext=(X[pt]+offset, Y[pt]))


plt.xlabel('Story length')
plt.ylabel('Lexical diversity')
plt.grid()
plt.show()
