#Napišite program koji od korisnika zahtijeva unos imena tekstualne datoteke. Program nakon toga treba tražiti linije oblika:
#Primijenjeno strojno učenje – laboratorijske vježbe – VJEŽBA 1 7
#X-DSPAM-Confidence: <neki_broj>
#koje predstavljaju pouzdanost korištenog spam filtra. Potrebno je izračunati srednju vrijednost pouzdanosti. Koristite datoteke mbox.txt i mbox-short.txt
#Primjer
#Ime datoteke: mbox.txt
#Average X-DSPAM-Confidence: 0.894128046745
#Ime datoteke: mbox-short.txt
#Average X-DSPAM-Confidence: 0.750718518519

name = input("Unesi ime datoteke: ")

try: 
    file = open(name)
    
    sum = 0
    counter = 0
    
    for line in file:
        if line.startswith("X-DSPAM-Confidence:"):
            broj = float(line.split(":")[1])
            sum += broj
            counter+=1
    if counter > 0:
        average = sum/counter
        print("Ime datoteke: ", name)
        print("Average X-DSPAM-Confidence: ", average)
    else:
        print("Nije nista pronadjeno")
except:

    print("Greska u otvaranju datoteke!")
