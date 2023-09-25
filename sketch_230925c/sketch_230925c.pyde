def setup():
    global y
    size(500, 500)
    y = height / 2
    colorMode(HSB)
    
w = 50
hw = w / 2
x = hw
y = 0

def draw():
    global x
    background(0)
    noStroke()
    fill(x / 2, 255, 255);
    circle(x, y, w);
    x = x = 1
    
    if x == width:
        x = hw
        
