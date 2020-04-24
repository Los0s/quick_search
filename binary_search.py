    





def search_on_list(list, item):
    low = 0
    high = len(list)
    timer = 0
    while True:
        timer += 1
        mid = (int(low) + int(high)) // 2 
        guess = list[mid]
        if guess == item:
            timer += 1
            return {'attempt' : timer,
            'number' : guess,
            'index' : mid}
            break
        elif guess < item:
            low = mid
        elif guess > item:
            high = mid
        if timer == 60:
            return None
    else:
        return('Цыкл завешон удачно')
        return None
    
    