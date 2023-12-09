import numpy as np

total_wins = []
with open("6\input.txt", 'r') as file:
    data = file.readlines()
    time = data[0].split('\n')
    distance = data[1].split('\n')
    time = time[0].split(' ')
    distance = distance[0].split(' ')
    while '' in time:
        time.remove('')
    while '' in distance:
        distance.remove('')
    
    del time[0]
    del distance[0]
    
    time = ''.join(time)
    distance = ''.join(distance)

    time_2 = []
    distance_2 = []
    
    time_2.append(int(time))
    distance_2.append(int(distance))

    i=0
    for times in time_2:
        mm=0
        hold=0
        rem=0
        win=0
        while hold <= times:
            rem = times-hold
            mm = rem*hold
            hold+=1
            if mm > distance_2[i]:
                win+=1
        i+=1
        total_wins.append(win)
print(total_wins)    

            
        