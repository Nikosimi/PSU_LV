Zadatak 1
  - non_func(x) je nepoznata funkcionalna ovisnost f(x), dok je add_noise(y) šum odnosno pogreška.
  - x, y_true, y_measured su skup ulaza i izmjerenih izlaza.
  - xtrain, ytrain su skupovi za učenje, dok su xtest i ytest skupovi za testiranje.
  - linearModel = lm.LinearRegression() definira linearni model.
  - linearModel.fit(xtrain,ytrain) procjenjuje parametre theta.
  - ytest_p = linearModel.predict(xtest) daje predikciju izlazne veličine.
  - MSE_test = mean_squared_error(ytest, ytest_p) računa mean squared error na podacima testnog skupa.

Zadatak 2
  - Prethodni model je mogao samo dati pravac predikcije, dok se u ovome modelu može postići predikcija koja je zakrivljena.
  - Ovaj model je bolji jer se može bolje prilagoditi nelinarnoj funkciji, međutim može doći do overfittinga.

Zadatak 3.



Zadatak 4.
  1. Broj automobila:  6699
  
  2. Tip stupca:  name                 str
  year               int64
  selling_price    float64
  km_driven          int64
  fuel                 str
  seller_type          str
  transmission         str
  owner                str
  mileage          float64
  engine             int64
  max_power        float64
  seats              int64
  dtype: object
  
  3. Najskuplji automobil:  name             BMW X7 xDrive 30d DPE
  year                              2020
  selling_price                15.789592
  km_driven                         5000
  fuel                            Diesel
  seller_type                 Individual
  transmission                 Automatic
  owner                      First Owner
  mileage                          13.38
  engine                            2993
  max_power                        265.0
  seats                                7
  Name: 2591, dtype: object
  
  3. Najjeftiniji automobil:  name             Maruti 800 AC
  year                      1997
  selling_price        10.308919
  km_driven                80000
  fuel                    Petrol
  seller_type         Individual
  transmission            Manual
  owner              Third Owner
  mileage                   16.1
  engine                     796
  max_power                 37.0
  seats                        4
  Name: 4778, dtype: object
  
  4. Broj automobila proizvedeno 2012. godine:  575
  
  5. Automobil koji je prošao najviše km:  name             Maruti Wagon R LXI Minor
  year                                 2010
  selling_price                   12.175613
  km_driven                          577414
  fuel                               Petrol
  seller_type                    Individual
  transmission                       Manual
  owner                        Second Owner
  mileage                              18.9
  engine                               1061
  max_power                            67.0
  seats                                   5
  Name: 3067, dtype: object
  
  5. Automobil koji je prošao najmanje km:  name             Maruti Eeco 5 STR With AC Plus HTR CNG
  year                                               2011
  selling_price                                  12.25009
  km_driven                                             1
  fuel                                                CNG
  seller_type                                  Individual
  transmission                                     Manual
  owner                              Fourth & Above Owner
  mileage                                            15.1
  engine                                             1196
  max_power                                          73.0
  seats                                                 5
  Name: 6514, dtype: object
  
  6. Najčešći broj sjedala:  5
  
  7. Prosječna prijeđena kilometraža:
  
  Dizel:  88039.97234392114
  
  Benzin:  54101.882809861534

Zadatak 5.
