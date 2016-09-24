# Lathund till Grafisk Assert

## Färger:    
* blå == 0,0,1
* grön == 0,1,0
* cyan == 0,1,1
* röd == 1,0,0
* magenta == 1,0,1
* gul == 1,1,0
* svart == 0
* grå == 0.5
* vit == 1

* bakgrundsfärg:
  * vit == bg(1)    
  * gul == bg(1,1,0)       
* fyllningsfärg:
  * ingen == fc()   
  * vit == fc(1)  
  * gul == fc(1,1,0)  
  * röd, halvgenomskinlig == fc(1,0,0, 0.5)    
* streckfärg:
  * ingen == sc()
  * vit == sc(1)
  * gul == sc(1,1,0)      
  * röd, halvgenomskinlig == sc(1,0,0, 0.5)
* strecktjocklek
  * en pixel == sw(1)                                 
  * två pixlar == sw(2)                                 

* translate(x,y)         
* rd(degrees)                                                
* rectMode(CENTER)          
  * CORNER
  * CORNERS
  * CENTER
  * RADIUS
* ellipseMode(CENTER)
  * CORNER
  * CORNERS
  * CENTER
  * RADIUS

* point(x,y)  
* line(x1,y1, x2,y2)  
* ellipse(x,y, w,h)
* circle(x,y,r)                                              
* rect(x,y, w,h)
* triangle(x1,y1, x2,y2, x3,y3)
* quad(x1,y1, x2,y2, x3,y3, x4,y4)  
* arc(x,y, w,h, start,stopp, PIE)  

* textAlign(CENTER,CENTER)
 * Horizontal
  * LEFT
  * CENTER
  * RIGHT
 * Vertical
  * TOP
  * CENTER
  * BOTTOM
* textSize(n)
* text("Python",x,y)

Dessa funktioner har lagts till för att underlätta:

  * bg(1) == background(255) 
  *  fc(1,0,0) == fill(255,0,0)
  * sc(0.5) == stroke(128)
  * sw(1) == strokeWeight(1)
  * circle(x,y,r) == ellipse(x,y, 2*r,2*r)
  * rd(45) == rotate(radians(45))