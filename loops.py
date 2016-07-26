ade = [3, 5, 5, 7, 5, 0, 7, 3, 8, 6]

def loop():
    for x in ade:
        if x == 3:
            print "bird"
        else:
            ade[x+1] = 3
            print ade[x]
            loop()
    
loop()