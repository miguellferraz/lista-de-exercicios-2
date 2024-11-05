import turtle

class Forma:
    def __init__(self, cor='black', tamanho=100):
        self.cor = cor
        self.tamanho = tamanho
    
    def desenhar(self):
        turtle.color(self.cor)
        turtle.dot(self.tamanho // 10)  

class Circulo(Forma):
    def desenhar(self):
        turtle.color(self.cor)
        turtle.begin_fill()
        turtle.circle(self.tamanho // 2)  
        turtle.end_fill()

class Quadrado(Forma):
    def desenhar(self):
        turtle.color(self.cor)
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(self.tamanho)
            turtle.right(90)
        turtle.end_fill()

def desenharFormas():
    turtle.speed(1)

    forma1 = Circulo(cor='red', tamanho=100)
    forma1.desenhar()
    
    turtle.penup()
    turtle.setpos(-150, 0)
    turtle.pendown()
    
    forma2 = Quadrado(cor='blue', tamanho=100)
    forma2.desenhar()

    turtle.done()

desenharFormas()
