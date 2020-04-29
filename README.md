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

cat trad.1.txt |awk '{sub(/[^ ]+ /, ""); print $0}'> kk  ; tr -d [:punct:] < kk >temp1.txt ; tr [:upper:] [:lower:] < temp1.txt > temp2.txt ; tr [:upper:] [:lower:] < temp1.txt > temp2.txt 


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






## nltk



