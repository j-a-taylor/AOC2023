input_file = open(r"1\ERRORTEST.TXT","r")

cali_values = input_file.readlines()
words = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

add_array = []
ans = 0

for line in (cali_values):
    line = line[::-1]
    print(line)


#make a words backwards dict
#create 2 loops, one for finding the lowest index value, the backwards one for finding the highest