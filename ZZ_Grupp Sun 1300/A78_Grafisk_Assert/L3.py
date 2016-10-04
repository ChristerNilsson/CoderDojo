from Assert import fc,sc,sw,rd,circle,bg,push,col

def lektion3(ass):

    with ass.check("horizontalLine"): 
        if ass.errors(): return
        sc(1,0,1)
        line(10,70, 190,70)


    with ass.check("verticalLine"): 
        if ass.errors(): return
        sw(10)
        sc(1,1,0)
        line(110,30,110,170) 
                
    with ass.check("yellowLine"): 
        if ass.errors(): return
        sc(1, 1, 0)
        line(20, 30,  140, 160)


    with ass.check("skislope"):
        if ass.errors(): return
        bg(0)
        sc(1,0,0)
        #for[i=0;i<20;i++]
        for i in range(21):
            line(i*10,0,200,i*10)
    
                        
    with ass.check("sunshine"):
        if ass.errors(): return
        bg(0)
        sc(1,1,0)
        for i in range(11):
            line(20*i, 0, 200 - (20 * i), 200)
            line(200, i*20, 0, 200 - (20 * i))
            