Zadatak 1
Skripta 5.1. učitava skup podataka koji se nalazi u csv datoteci occupancy_processed.csv.
Ova datoteka sadrži podatke koji su prikupljeni u prostoriji veličine 6m x 4.6m tijekom 4 dana [1]. 
Zbog jednostavnosti skup sadrži samo dva atributa: mjerenja dobivena sa senzora temperature i mjerenja sa senzora CO2. 
Izlazna (ciljna) veličina je zauzetost prostorije (0 – prazna prostorija, 1 – u prostoriji se nalazi barem jedna osoba). 
Cilj je izgraditi klasifikator koji će na temelju trenutnih mjerenja dobivenih sa senzora temperature 
i sa senzora CO2 procijeniti zauzetost prostorije.

a) Pokrenite skriptu i pogledajte dobiveni dijagram raspršenja. Što primjećujete?
Klasa Zauzeta ima veće vrijednosti CO2. Postoje preklapanja, te je skup neuravnotezen jer ima više primjera klase Zauzeta od klase Slobodna (0=8228, 1=1901).
b) Koliko podatkovnih primjera sadrži učitani skup podataka?
length: 10129
c) Kakva je razdioba podatkovnih primjera po klasama?
10129
0: 8228 81%
1: 1901 19%

Zadatak 2
Izgradite i evaluirajte algoritam K najbližih susjeda. Slijedite ovaj redoslijed:
a) Podijelite podatke na skup za učenje i skup za testiranje (omjer 80%-20%) pomoću funkcije train_test_split. Koristite opciju stratify=y.
b) Pomoću StandardScaler skalirajte ulazne veličine.
c) Pomoću klase KNeighborsClassifier izgradite algoritam K najbližih susjeda.
d) Evaluirajte izgrađeni klasifikator na testnom skupu podataka:
a. prikažite matricu zabune

b. izračunajte točnost klasifikacije
Točnost:  0.9236842105263158
c. izračunajte preciznost i odziv po klasama
        precision recall
0       0.98      0.96      
1       0.85      0.92      
e) Što se događa s rezultatima ako se koristi veći odnosno manji broj susjeda?
k[1, 2, 3, 4, 10, 15, 20, 25]
vidimo da ukoliko je k vrlo visok ili vrlo nizak dolazi do nize preciznosti, najbolji rezultat je oko 10. 
f) Što se događa s rezultatima ako ne koristite skaliranje ulaznih veličina?
(k=5) Točnost sa skaliranjem 0.95, bez skaliranja 0.93.

Umjesto algoritma K najbližih susjeda koristite stablo odlučivanja te ponovite korake a) do d) iz prethodnog zadatka.
Točnost:  0.8842105263157894
Preciznost i odziv po klasama:
               precision    recall  f1-score   support

           0       0.97      0.97      0.97      1646
           1       0.88      0.88      0.88       380

    accuracy                           0.96      2026
   macro avg       0.93      0.93      0.93      2026
weighted avg       0.96      0.96      0.96      2026
a) Vizualizirajte dobiveno stablo odlučivanja.
b) Što se događa s rezultatima ako mijenjate parametar max-depth stabla odlučivanja?
Promjenom depth-a [1, 2, 3, 4, 10, 15, 20, 25] pojavljuje je underfitting odnosno model je prejednostavan, povecavanjem dubine dobijamo bolje rezultate, te nakon odredjene tocke poboljsanje je zanemarivo.
c) Što se događa s rezultatima ako ne koristite skaliranje ulaznih veličina?
