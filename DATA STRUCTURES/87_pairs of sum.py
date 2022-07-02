def pairs(list, pair):
    c=0
    for i in range(len(list)):
        c = pair - list[i]
        if c in list[i+1:]:
            print(str(list[i]) + " " + str(c)  + '= 8')
pairs([2, 3, 4, 5, 6, 7], 8)
