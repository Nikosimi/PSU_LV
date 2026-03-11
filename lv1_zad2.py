#Napišite program koji od korisnika zahtijeva upis jednog broja koji predstavlja nekakvu ocjenu i nalazi se između 0.0 i 1.0. 
# Ispišite kojoj kategoriji pripada ocjena na temelju sljedećih uvjeta:
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#Ako korisnik nije utipkao broj, ispišite na ekran poruku o grešci (koristite try i except naredbe). 
# Također, ako je broj izvan intervala [0.0 i 1.0] potrebno je ispisati odgovarajuću poruku.

try:
    ocjena = float(input("Unesite ocjenu izmedju 0.0 i 1.0:"))
    
    if(ocjena<0.0 or ocjena>1.0):
        print("Uneseni broj je izvan zadanog intervala")
    elif(ocjena>=0.9):
        print("Ocjena: A")
    elif(ocjena>=0.8):
        print("Ocjena: B")
    elif(ocjena>=0.7):
        print("Ocjena: B")
    elif(ocjena>=0.6):
        print("Ocjena: B")
    else:
        print("Ocjena: B")
except:
    print("Broj nije unesen")