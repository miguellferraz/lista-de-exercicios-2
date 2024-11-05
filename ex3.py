import turtle

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def moverParaPonto(ponto):
    turtle.penup()
    turtle.goto(ponto.x, ponto.y)
    turtle.pendown()

def desenharComPonto():
    turtle.speed(1)
    
    ponto1 = Ponto(150, 140)
    moverParaPonto(ponto1)
    turtle.dot(10, "blue")  

    ponto2 = Ponto(-110, -190)
    moverParaPonto(ponto2)
    turtle.dot(10, "red") 

    turtle.done()

desenharComPonto()
