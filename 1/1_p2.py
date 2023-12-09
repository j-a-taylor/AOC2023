input_file = open(r"1\input.TXT","r")

cali_values = input_file.readlines()
words = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
rev_words = {'eno':1, 'owt':2, 'eerht':3, 'ruof':4, 'evif':5, 'xis':6, 'neves':7, 'thgie':8, 'enin':9, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

one_array = []
two_array = []
final_array = []

ans = 0

for line in cali_values:
    digits_low = []
    digits_low_index = []

    for word in words:
        if word in line:
            if len(digits_low_index):
                if line.index(word) < digits_low_index[0]:
                    digits_low.pop(0)
                    digits_low_index.pop(0)
                    digits_low.insert(0,int(words.get(word)))
                    digits_low_index.insert(0,line.index(word))
                    
            else:
                digits_low.insert(0,int(words.get(word)))
                digits_low_index.insert(0,line.index(word))

    one_array.append(int(str(digits_low[0])))

for line in cali_values:
    line = line[::-1]
    digits = []
    digits_index = []

    for rev_word in rev_words:
        if rev_word in line:
            if len(digits_index):
                if line.index(rev_word) < digits_index[0]:
                    digits.pop(0)
                    digits_index.pop(0)
                    digits.insert(0,int(rev_words.get(rev_word)))
                    digits_index.insert(0,line.index(rev_word))
                    
            else:
                digits.insert(0,int(rev_words.get(rev_word)))
                digits_index.insert(0,line.index(rev_word))
                 
    two_array.append(int(str(digits[0])))

#print(f"Collected numbers: {one_array}")
#print(f"Collected numbers: {two_array}")

i=0

for no in one_array:
    final_array.append(str(one_array[i]) + str(two_array[i]))
    final_array[i] = int(final_array[i])
    i = i+1
    
#print(final_array)
ans = sum(final_array)
print(ans)