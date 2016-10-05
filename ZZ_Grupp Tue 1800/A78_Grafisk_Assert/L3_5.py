from Assert import fc,sc,sw,rd,circle,bg,push,col

# for loops

def lektion3_5(ass):
    
    with ass.check("for01"): 
        if ass.errors(): return
        rectMode(CENTER)
        for i in range(10) :
            x=20*i+10
            y=10
            w=10
            h=10
            rect(x,y,w,h)

                        
    with ass.check("for02"): 
        if ass.errors(): return        
        rectMode(CENTER)
        for i in range(10) :
            x=10
            y=20*i+10
            w=10
            h=10
            rect(x,y,w,h)

                        
    with ass.check("for03"): 
        if ass.errors(): return
        rectMode(CENTER)
        for i in range(10) :
            x=20*i+10
            y=20*i+10
            w=10
            h=10
            rect(x,y,w,h)

                        
    with ass.check("for04"): 
        if ass.errors(): return
        rectMode(CENTER)
        for i in range(10) :
            for j in range(10) :
        
                x=20*i+10
                y=20*j+10
                w=10
                h=10
                rect(x,y,w,h)
                                                    
    with ass.check("for05"): 
        if ass.errors(): return
        rectMode(CENTER)
        for i in range(10) :
            x=20*i+10
            y=10
            w=2*i
            h=2*i
            rect(x,y,w,h)

    with ass.check("for06"): 
        if ass.errors(): return
        rectMode(CENTER)
        for i in range(10) :
            x=20*i+10
            y=10
            w=2*i
            h=2*i
            fc(i/10.0,0,0)
            rect(x,y,w,h)

    with ass.check("for07"): 
        if ass.errors(): return
        ellipseMode
        for i in range(10) :
            x=20*i+10
            y=10
            w=2*i
            h=2*i
            fc(i/10.0,0,0)
            ellipse(x,y,w,h)
                        
    with ass.check("for08"): 
        if ass.errors(): return
        for i in range(10,0,-1) :
            x=100
            y=100
            w=20*i
            h=20*i
            fc(i/10.0,0,0)
            ellipse(x,y,w,h)
                        
    with ass.check("for09"): 
        if ass.errors(): return
        for i in range(10,0,-1) :
            x=10*i
            y=10*i
            w=20*i
            h=20*i
            fc(i/10.0,0,0)
            ellipse(x,y,w,h)
                        
    with ass.check("for10"): 
        if ass.errors(): return
        for i in range(10) :
            for j in range(10):
        
                x=20*i+10
                y=20*j+10 
                w=i+j 
                h=i+j 
                fc(i/10.0,j/10.0,0)
                circle(x,y,w/2)
                                
    with ass.check("for11"): 
        if ass.errors(): return
        sc()
        rectMode(CENTER)
        for i in range(10) :
            for j in range(10):
                with push():
                  #  rd(5)
            
                    x=20*i+10
                    y=20*j+10 
                    #translate(x,y)
                    w=10
                    h=10 
                    fc(i/10.0,j/10.0,0)
                    rect(x,y,w,h)
                    

    with ass.check("for12"): 
        if ass.errors(): return

                                
                        