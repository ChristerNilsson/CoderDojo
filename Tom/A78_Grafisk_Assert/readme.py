Lathund till Grafisk Assert
===========================

Färger:    
    0,0,1 blå
    0,1,0 grön 
    0,1,1 cyan
    1,0,0 röd
    1,0,1 magenta
    1,1,0 gul
    
    0     svart   
    0.5   grå  
    1     vit

bakgrundsfärg:         vit    gul        
                       bg(1)  bg(1,1,0)                    (*)

fyllningsfärg:  ingen  vit    gul        röd, halvgenomskinlig
                fc()   fc(1)  fc(1,1,0)  fc(1,0,0, 0.5)    (*)
        
streckfärg:     ingen  vit    gul        röd, halvgenomskinlig
                sc()   sc(1)  sc(1,1,0)  sc(1,0,0, 0.5)    (*)

strecktjocklek: sw(pixlar)                                 (*)

translate(x,y)         
rd(degrees)                                                (*)
rectMode(CENTER)          CORNER/CORNERS/CENTER/RADIUS
ellipseMode(CENTER)       CORNER/CORNERS/CENTER/RADIUS

point(x,y)
line(x1,y1, x2,y2)
ellipse(x,y, w,h)
circle(x,y,r)                                              (*)
rect(x,y, w,h)
triangle(x1,y1, x2,y2, x3,y3)
quad(x1,y1, x2,y2, x3,y3, x4,y4)
arc(x,y, w,h, start,stopp, PIE)

textAlign(CENTER,CENTER)  LEFT/CENTER/RIGHT  TOP/CENTER/BOTTOM
textSize(n)
text("Python",x,y)

(*) Dessa funktioner har lagts till av Christer.
  bg(1) == background(255)
  fc(1,0,0) == fill(255,0,0)
  sc(0.5) == stroke(128)
  sw(1) == strokeWeight(1)
  circle(x,y,r) == ellipse(x,y, 2*r,2*r)
  rd(45) == rotate(radians(45))