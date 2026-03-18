#Napišite Python skriptu koja će učitati tekstualnu datoteku naziva SMSSpamCollection.txt [1]. Ova datoteka
#sadrži 425 SMS poruka pri čemu su neke označene kao spam, a neke kao ham. Primjer dijela datoteke:
#ham Go until jurong point, crazy.. Available only in bugis n great world la e buffet... Cine there got amore wat...
#ham Ok lar... Joking wif u oni...
#spam Did you hear about the new "Divorce Barbie"? It comes with all of Ken's stuff!
#ham Yup next stop.
#a) Izračunajte koliki je prosječan broj riječi u SMS porukama koje su tipa ham, a koliko je prosječan broj riječi u
#porukama koje su tipa spam.
#b) Koliko SMS poruka koje su tipa spam završava uskličnikom ?

file = open("/Users/nikos/SMSSpamCollection.txt")

ham_br=[]
spam_br=[]
usklicnik_br=0

for line in file:
    line = line.rstrip()
    if not line:
        continue
    parts = line.split('\t',1)
    if len(parts)<2:
        continue

    label = parts[0].strip()
    poruka = parts[1].strip()

    rijeci = poruka.split()
    br_rijeci = len(rijeci)

    if label == 'ham':
        ham_br.append(br_rijeci)
    elif label == 'spam':
        spam_br.append(br_rijeci)
        if poruka.endswith('!'):
            usklicnik_br += 1
file.close()

#a
if ham_br:
    average_ham = sum(ham_br)/len(ham_br)
else:
    average_ham=0

if spam_br:
    average_spam = sum(spam_br)/len(spam_br)
else:
    average_spam = 0

print("Prosjecan broj ham poruka: ",average_ham)
print("Prosjecan broj spam poruka: ",average_spam)

#b
print("Broj spam poruka s usklicnikom: ",usklicnik_br)