def setup():
    size(500, 500)
    colorMode(HSB)
    #colorMode(RGB)
    
def draw():
    #Greyscale
    #RGB
    #RGBA
    background(0)
    f = 10.0
    g = 20.0
    h = 5.0 
    
    #Adding
    
    f = f + 1
    f =+ 1
    
    #Subtracting
    
    g -= 30
    g = g - 27
    
    #multiplying
    
    g = f * h
    h *= 2
    
    #Divide
    g = f / h
    h = h / 2.5
    
    f = pow(g + 5)
    
    h = h - 7
    g += f
    f += g
    h = f - (g + 5)
    
    println("f: " + f)
    println("g: " + f)
    println("h: " + f)
        
            
    print(f/2)
    println(f)
        
    stroke(80, 255, 255)
    line(mouseX, 10, 100, mouseY)
    rect(20, 20, 50, 100)
    noStroke()
        
    circle(100, mouseY, 5)
    fill(90, mouseX / 2, 255)
    ellipse(200, 200, 100, 10)
    point(90, 100)    
    
    
