with open("4\input.txt", 'r') as file:
    total_score = 0
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
                    if score == 0:
                        score +=1
                    else:
                        score = score*2
                i+=1
            print(score)
            total_score += score
    print(total_score)
        
        