# A program that askes for a length of sequence
# the higher length of sequnence the more number will print out



n = int(input("Enter the length of the sequence: ")) # Do not change this line
tala_1 = 1
tala_2 = 2
tala_3 = 3

for i in range(1, n+1):   
    if i == 1:       
        print(tala_1)
    elif i == 2:
        print(tala_2)
    elif i == 3:
        print(tala_3)
    else:
        tala_summa = tala_1 + tala_2 + tala_3
        tala_1 = tala_2
        tala_2 = tala_3
        tala_3 = tala_summa
        print(tala_summa)
   




