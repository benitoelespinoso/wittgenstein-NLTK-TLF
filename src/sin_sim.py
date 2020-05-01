import nltk
from nltk.corpus import PlaintextCorpusReader
corpus_root = r'C:\Users\guille\Google Drive\NLTK\DEF\ficheros_in\Tratactus\esp\afo'
from nltk import FreqDist
newcorpus = PlaintextCorpusReader(corpus_root, '.*')
tokens = nltk.word_tokenize(newcorpus.raw())
text = nltk.Text(tokens)
stopwords = nltk.corpus.stopwords.words('spanish')
fdist = FreqDist(text)
fdist_no_punc_no_stopwords = nltk.FreqDist(dict((word, freq) for word, freq in fdist.items() if word not in stopwords and word.isalpha()))

# términos sinónimos o similares

text.similar("proposición")
# tomaremos los 3 primeros figura realidad lógica
text.similar("mundo")


# conextos comunes
text.common_contexts(["proposición","figura"])
text.common_contexts(["lenguaje","mundo"])



# comparativa de las apariciones de diversos términos. Se hace con proposición y con sus 3 primeros similares

cfd = nltk.ConditionalFreqDist(
 (target, fileid[:])
 for fileid in newcorpus.fileids()
 for w in newcorpus.words(fileid)
 for target in ['proposición', 'lógica']
 if w.lower().startswith(target))
cfd.plot()	

# idem para lenguaje y mundo. 

cfd = nltk.ConditionalFreqDist(
 (target, fileid[:])
 for fileid in newcorpus.fileids()
 for w in newcorpus.words(fileid)
 for target in ['mundo', 'lenguaje']
 if w.lower().startswith(target))
cfd.plot()