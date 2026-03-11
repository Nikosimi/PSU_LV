#Napišite Python skriptu koja će učitati tekstualnu datoteku naziva song.txt. Potrebno je napraviti rječnik koji kao
#ključeve koristi sve različite riječi koje se pojavljuju u datoteci, dok su vrijednosti jednake broju puta koliko se svaka
#riječ (ključ) pojavljuje u datoteci. Koliko je riječi koje se pojavljuju samo jednom u datoteci? Ispišite ih.

file = open("song.txt")

text = file.read()
words = text.split()

counter = {}

for word in words:
    if word in counter:
        counter[word]+=1
    else:
        counter[word] = 1
once = []

for word, num in counter.items():
    if num == 1:
        once.append(word)

print("Broj rijeci koje se pojavljuju jednom: ", len(once))
print("Rijeci koje se pojavljuju jednom: ")
for r in once:
    print(r)