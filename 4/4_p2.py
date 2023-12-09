import numpy as np
import time

start_time = time.time()

with open("4\input.txt", 'r') as file:
    total_score = 0
    copies = [1] * 194
    copies_b = np.array(copies)
    y=0
    ans=0
    
    for line in file:
        line = line.split(':')
        line = line[1].replace('\n','')
        card_id = line[0]
        card_id = card_id.replace('Card ','')
        nums = line.split('|')
        w_nums = nums[0].split(' ')
        g_nums = nums[1].split(' ')
        
        while '' in w_nums:
            w_nums.remove('')
        
        while '' in g_nums:
            g_nums.remove('')
             
        for card in card_id:
            i=0
            score=0
            
            for nums in g_nums:
                if g_nums[i] in w_nums:
                    score +=1
                i+=1
            m=0
            k=y+1
            while m < 1:
                copies_b[k:score+k] +=copies_b[y]
                m+=1
            y+=1
                
    ans=sum(copies_b)           
    print(copies_b)
    print(ans)

print("--- %s seconds ---" % (time.time() - start_time))  