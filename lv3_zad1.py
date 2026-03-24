import pandas as pd
import numpy as np

mtcars = pd.read_csv('mtcars.csv')
#1 Kojih 5 automobila ima najveću potrošnju? (koristite funkciju sort)
print('#1')
mpg=mtcars.sort_values(by=['mpg'])
print(mpg.tail(5).car)
print('\n')

#2 Koja tri automobila s 8 cilindara imaju najmanju potrošnju?
print('#2')
cyl8=mtcars[mtcars.cyl==8]
mincyl8=cyl8.sort_values(by='mpg').head(3).car
print(mincyl8)
print('\n')


#3 Kolika je srednja potrošnja automobila sa 6 cilindara?
print('#3')
cyl6=mtcars[mtcars.cyl==6]
meanCyl6Mpg=cyl6.mpg.mean()
print(meanCyl6Mpg)
print('\n')

#4 Kolika je srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs?
print('#4')
cyl4Mass=mtcars[(mtcars.cyl==4)&(mtcars.wt>=2.000)&(mtcars.wt<=2.200)]
print(cyl4Mass.mpg.mean())
print('\n')

#5 Koliko je automobila s ručnim, a koliko s automatskim mjenjačem u ovom skupu podataka?
print('#5')
manualCars=mtcars[mtcars.am==0]
automaticCars=mtcars[mtcars.am==1]
print("Broj automobila s rucnim mjenjacem: ",manualCars.shape[0])
print("Broj automobila s automatskim mjenjacem: ",automaticCars.shape[0])
print(automaticCars)
print('\n')

#6 Koliko je automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga?
print('#6')
automaticHP=mtcars[(mtcars.am==1)&(mtcars.hp>100)]
print(automaticHP.shape[0])
print('\n')

#7 Kolika je masa svakog automobila u kilogramima?
print('#6')
wtCars=mtcars.wt
print(wtCars*1000*0.45359237)


print(mtcars.sort_values(by=['mpg']).head(5))