# wittgenstein-NLTK-TLF
NLTK and bash quantitative parsing of TLF

## Software necesario (win10)

- python 3.8

- pip install -U nltk

- ejecutar 
  - import nltk
  - nltk.download() -- ALL

- pip install -U numpy
- pip install -U matplotlib
- pip install scipy

Se puede echar un vistazo a:
		
https://answers.microsoft.com/en-us/windows/forum/all/microsoft-visual-c-140/6f0726e2-6c32-4719-9fe5-aa68b5ad8e6d

https://www.scivision.dev/python-windows-visual-c-14-required/


## wittgenstein (tractatus logico-philosophicus)

No necesita presentación. 
Se ha definido el GRADO de un aforismo del texto, es igual a la cantidad de cifras tras el "." que aparece en la indexación de los aforismos: 

El aforismo 2.21 (por ejemplo) tiene GRADO = 2. 
El aforismo 6 tiene GRADO = 0
El aforismo 3.121 tiene GRADO = 3

## Ficheros de input

Se adjuntan los ficheros de input utilizados.

El tratactus en ingles
El tratactus en español

Para cada una de estas versiones se incluyen subdirectorios donde el texto se ha separado:

- Por capítulos
- Por grados

El texto tiene 7 capítulos. Los capítulos 1 y 7 son triviales ó muy escuetos. 

El texto tiene aforismos de grado entre 0 y 5 (muy pocos con grado 5)




## bash

### bash.1

el fichero trad.1.txt es el tratactus en ESP

La longitud promedio de los aforismos del tratado (ESP) es:

~~~

cat trad.1.txt |awk '{sub(/[^ ]+ /, ""); print $0}'> kk  ; tr -d [:punct:] < kk >temp1.txt 

tr [:upper:] [:lower:] < temp1.txt > temp2.txt ; tr [:upper:] [:lower:] < temp1.txt > temp2.txt 

cat 1.trad.norm.txt | while read line; do count=$(echo $line | wc -c); echo $count $line |awk '{print $1}'; done > num_char_perLine.1.txt 

cat num_char_perLine.1.txt |awk '{sum+=$1} END { print "Average = ",sum/NR}' 

~~~

**Average = 230.156**



### bash.2

¿Cuantos aforismos hay de cada grado? 

~~~

cat trad.1.txt | awk '{print $1}'| awk -F. '{print $1 "-" $2 "-" length($2)}'> grado.trad.1.txt

for i in {0..5}; do awk -v var=$i -F- '{if($3==var)print $0}' grado.trad.1.txt | wc -l  ; done

~~~

- 7
- 25
- 124
- 245
- 118
- 7

Para cada uno de los grados  {0,1,...5}

![aforismos por grados](img/graf1.png)


### bash.3

La longitud promedio de los aforismos según su grado:

~~~
paste -d"-" grado.trad.1.txt num_char_perLine.1.txt > grado_char1.txt

for i in {0..5}; do awk -v var=$i -F- '{if($3==var)print $4}' grado_char1.txt |awk '{sum+=$1} END { print "Average_Por_grado = ",sum/NR}'   ; done

~~~

Y se obtiene:

grado_0 =  69.1429  
grado_1 =  164.04  
grado_2 =  195.597  
grado_3 =  243.547  
grado_4 =  257.703  
grado_5 =  279.857  

Cuanto mayor es el grado, mayor es la longitud del aforismo

![longitud_aforismos por grados](img/graf2.png)


## nltk

### Aforismos mónicos

Se sustituye la ruta donde residen los aforismos (en inglés) del siguiente script:

~~~

import nltk
from nltk.corpus import PlaintextCorpusReader
corpus_root = r'C:\Users\guille\Google Drive\NLTK\NLTK\tratactus\eng_tratactus\afo'
newcorpus = PlaintextCorpusReader(corpus_root, '.*')
tokens = nltk.word_tokenize(newcorpus.raw())
words = newcorpus.words()
words = [word.lower() for word in words]
for fileid in newcorpus.fileids():
 num_chars = len(newcorpus.raw(fileid))
 num_words = len(newcorpus.words(fileid))
 num_sents = len(newcorpus.sents(fileid))
 print (num_chars , num_words, num_sents, fileid)

~~~

Se obtiene un CSV así:

num_chars num_words num_sents fileid  
56 		15 	1  	1.1.txt  
78 		19  	1  	1.11.txt  
96 		22  	1  	1.12.txt  
48 		12  	1  	1.13.txt  
35 		9   	1  	1.2.txt  
88 		20  	1  	1.21.txt  
37 		10  	1  	1.txt  
83 		21  	1  	2.01.txt  
97 		19  	1  	2.011.txt  
162     	35  	1  	2.012.txt  
707    		136  	6  	2.0121.txt  
285     	58  	2  	2.0122.txt  
214     	44  	3  	2.0123.txt  

Que contiene para cada aforismo: numero de caracteres, numero de palabras, numero de frases, y el fileid (que identifica al aforismo en cuestión)


Si llamamos al fichero resultante (por ejemplo) kk.txt
~~~
awk 'NF>0' kk.txt > kk.txt.bueno; mv kk.txt.bueno kk.txt

totales=`wc -l kk.txt | awk '{print $1}'` ;  monicos=`awk '$3==1' kk.txt | wc -l` ; awk "BEGIN {print $monicos/$totales}"
~~~

**0.441634**

Es decir, el 44% de los aforismos del texto contienen un sola sentencia.

Si vemos el % de aforismos mónicos según su capítulo:

~~~
for j in {1..7}; do cat kk.txt | awk '{print $4}' | awk -v var=$j -F"." '$1==var' | wc -l ; done > totales
	
for i in {1..7}; do cat kk.txt | awk '$3==1' | awk '{print $4}' | awk -v var=$i -F"." '$1==var'  | wc -l ; done > parciales

paste totales parciales > kk
	
awk '{print "% de aforismos de una sola sentencia. Capítulo "NR"  " $2/$1}' kk
~~~

% de aforismos mónicos. Capítulo 1  1  
% de aforismos mónicos. Capítulo 2  0.818182  
% de aforismos mónicos. Capítulo 3  0.478873  
% de aforismos mónicos. Capítulo 4  0.311321  
% de aforismos mónicos. Capítulo 5  0.358108  
% de aforismos mónicos. Capítulo 6  0.346154  
% de aforismos mónicos. Capítulo 7  1  


**El texto es lacónico a más no poder**

Si calculamos los aforismos mónicos (su %) a tenor del grado del aforismo:

tomando el grado > 1:


~~~
for i in {1..5}; do awk -F"." 'NF>2' kk.txt | awk -v var=$i -F"." '{ if (length($2) == var) print $0}' > grado_$i.txt ; done

for k in {1..5}; do cat grado_$k.txt > kk 
 for j in {1..7}; do cat kk | awk '{print $4}' | awk -v var=$j -F"." '$1==var' | wc -l ; done 	> totales
 for i in {1..7}; do cat kk | awk '$3==1' | awk '{print $4}' | awk -v var=$i -F"." '$1==var'  | wc -l ; done	> parciales
 paste totales parciales	> subtot
 awk -v var=$k '{if( $1 + 0 != 0) print "% de afo. de 1 sentencia. Para el GRADO="var" ___Capítulo "NR"  " $2/$1}' subtot
done
~~~

Que devuelve unos datos curiosos:


