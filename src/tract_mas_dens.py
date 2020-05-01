# adj
# texto entero

import nltk
from scipy import stats
from numpy import array
import matplotlib.pyplot as plt
from nltk.corpus import PlaintextCorpusReader
corpus_root = r'C:\Users\guille\Google Drive\NLTK\DEF\ficheros_in\Tratactus\ing\GRADOS\grado_4'
newcorpus = PlaintextCorpusReader(corpus_root, '.*')
tokens = nltk.word_tokenize(newcorpus.raw())
text = nltk.Text(tokens)
stopwords = nltk.corpus.stopwords.words('english')
from nltk import word_tokenize
from nltk.tag import pos_tag
V = ['VB', 'VBZ', 'VBP', 'VBD', 'VBG']
N = ['NN', 'NNS', 'NNP', 'NNPS']
ADV = ['RB', 'RBR', 'RBS']
ADJ = ['JJ', 'JJR', 'JJS']
wLen = []       # number of words
vLen = []       # number of verbs
advLen = []     # number of adverbs
adjLen = []     # number of adjectives
vLen, nLen, advLen, adjLen, wLen = ([] for i in range(5))
for fileid in newcorpus.fileids():
 tokens = word_tokenize(newcorpus.raw(fileid))
 words = [t for t in tokens if t.isalpha()]
 taggedW = pos_tag(words)
 verbs, nouns, advs, adjs = ([] for i in range(4))
 for (w,tag) in taggedW:
     if tag in V: verbs.append(w)
     elif tag in N: nouns.append(w)
     elif tag in ADV: advs.append(w)
     elif tag in ADJ: adjs.append(w)
 wLen.append(len(words))
 vLen.append(len(verbs))
 nLen.append(len(nouns))
 advLen.append(len(advs))
 adjLen.append(len(adjs))


plotData0 = [(wLen, vLen), (wLen, nLen), (wLen, adjLen)]
yaxisLabels = ['V x 1000', 'N x 1000', 'ADJ x 1000']
plt.figure(figsize=(7.5,7.5))


for (pane, data) in enumerate(plotData0):
 X, Y = data[0], data[1]
 slope, intercept = stats.linregress(X, Y)[0:2]
 rX = slope*array(X) + intercept
 plt.subplot(2, 2, pane+1)
 plt.scatter(X, Y)
 plt.plot(X, rX, 'r',
  label='slope={},\nintercept={}'.format(
  round(slope,2),
  round(intercept,2)))
 plt.ylim(plt.xlim())
 wTicks = [int(tk/1000) for tk in plt.gca().get_xticks()]
 plt.gca().set_xticklabels(wTicks)
 plt.gca().set_yticklabels(wTicks)
 offset = (plt.gca().get_xticks()[1]-plt.gca().get_xticks()[0])/10
 for pt in range(len(X)):
  plt.annotate(str(pt), # scifiCorpus[i]
   xy=(X[pt], Y[pt]),
   xytext=(X[pt]+offset, Y[pt]))
 plt.xlabel('words x 1000')
 plt.ylabel(yaxisLabels[pane])
 plt.legend(loc='upper left', fontsize='small')
 plt.grid()

plt.tight_layout()
plt.show()










# adverbios
# texto entero

import nltk
from scipy import stats
from numpy import array
import matplotlib.pyplot as plt
from nltk.corpus import PlaintextCorpusReader
corpus_root = r'C:\Users\guille\Google Drive\NLTK\DEF\ficheros_in\Tratactus\ing\GRADOS\grado_4'
newcorpus = PlaintextCorpusReader(corpus_root, '.*')
tokens = nltk.word_tokenize(newcorpus.raw())
text = nltk.Text(tokens)
stopwords = nltk.corpus.stopwords.words('english')
from nltk import word_tokenize
from nltk.tag import pos_tag
V = ['VB', 'VBZ', 'VBP', 'VBD', 'VBG']
N = ['NN', 'NNS', 'NNP', 'NNPS']
ADV = ['RB', 'RBR', 'RBS']
ADJ = ['JJ', 'JJR', 'JJS']
wLen = []       # number of words
vLen = []       # number of verbs
advLen = []     # number of adverbs
adjLen = []     # number of adjectives
vLen, nLen, advLen, adjLen, wLen = ([] for i in range(5))
for fileid in newcorpus.fileids():
 tokens = word_tokenize(newcorpus.raw(fileid))
 words = [t for t in tokens if t.isalpha()]
 taggedW = pos_tag(words)
 verbs, nouns, advs, adjs = ([] for i in range(4))
 for (w,tag) in taggedW:
     if tag in V: verbs.append(w)
     elif tag in N: nouns.append(w)
     elif tag in ADV: advs.append(w)
     elif tag in ADJ: adjs.append(w)
 wLen.append(len(words))
 vLen.append(len(verbs))
 nLen.append(len(nouns))
 advLen.append(len(advs))
 adjLen.append(len(adjs))


plotData0 = [(wLen, vLen), (wLen, nLen), (wLen, advLen)]
yaxisLabels = ['V x 1000', 'N x 1000', 'ADV x 1000']
plt.figure(figsize=(7.5,7.5))


for (pane, data) in enumerate(plotData0):
 X, Y = data[0], data[1]
 slope, intercept = stats.linregress(X, Y)[0:2]
 rX = slope*array(X) + intercept
 plt.subplot(2, 2, pane+1)
 plt.scatter(X, Y)
 plt.plot(X, rX, 'r',
  label='slope={},\nintercept={}'.format(
  round(slope,2),
  round(intercept,2)))
 plt.ylim(plt.xlim())
 wTicks = [int(tk/1000) for tk in plt.gca().get_xticks()]
 plt.gca().set_xticklabels(wTicks)
 plt.gca().set_yticklabels(wTicks)
 offset = (plt.gca().get_xticks()[1]-plt.gca().get_xticks()[0])/10
 for pt in range(len(X)):
  plt.annotate(str(pt), # scifiCorpus[i]
   xy=(X[pt], Y[pt]),
   xytext=(X[pt]+offset, Y[pt]))
 plt.xlabel('words x 1000')
 plt.ylabel(yaxisLabels[pane])
 plt.legend(loc='upper left', fontsize='small')
 plt.grid()

plt.tight_layout()
plt.show()

