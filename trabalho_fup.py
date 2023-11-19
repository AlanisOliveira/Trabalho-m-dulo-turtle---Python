import turtle
import math
import random

# Criando pontuação
pontos = 0
vidas = 3

# Criando a tela
game = turtle.Screen()
game.bgcolor('black')
game.bgpic('AL4.gif')
game.title("Jogo da tartaruga")
game.setup(700, 700)


# criando a arena de jogo
borda = turtle.Turtle()
borda.color("white")
borda.penup()
borda.setposition(-300, -300)
borda.pendown()
borda.pensize(3)
for i in range(4):
    borda.forward(600)
    borda.left(90)
borda.hideturtle()

# Criando o jogador
alanis = turtle.Turtle()
alanis.color('white')
alanis.shape('turtle')
alanis.penup()
alanis.forward(100)
speed = 0

# Criando veneno
veneno = turtle.Turtle()
veneno.color('green')
veneno.shape('circle')
veneno.penup()
veneno.speed(0)
veneno.setposition(-100, -100)

# Criando a comida
comida = turtle.Turtle()
comida.color('red')
comida.shape('circle')
comida.penup()
comida.speed(0)
comida.setposition(-120, -120)
comida.forward(100)


# Pontuação Pontos
pon = turtle.Turtle()
pon.hideturtle()
pon.penup()
pon.speed(0)
pon.color("white")
pon.goto(-300, 300)
pon.write("Pontos: 0", align="left", font=("Times New Roman", 14, "bold"))


# Pontuação Vidas
life = turtle.Turtle()
life.hideturtle()
life.penup()
life.speed(0)
life.color("white")
life.goto(300, 300)
life.write("Vidas: 3", align="right", font=("Times New Roman", 14, "bold"))


# controlando o jogador

def turnleft():
    alanis.left(30)


def turnright():
    alanis.right(30)


def increasespeed():
    global speed
    speed += 1


def slowspeed():
    global speed
    speed -= 1


# Criando atalhos do teclado
game.listen()
game.onkey(turnleft, 'Left')
game.onkey(turnright, 'Right')
game.onkey(increasespeed, 'Up')
game.onkey(slowspeed, 'Down')

while True:
    alanis.forward(speed)

    # checando a borda
    if alanis.xcor() > 300 or alanis.xcor() < -300:
        alanis.forward(-10)
    if alanis.ycor() > 300 or alanis.ycor() < -300:
        alanis.forward(-10)

    # checando a colisão com o veneno
    d = math.sqrt(math.pow(alanis.xcor()-veneno.xcor(), 2) +
                  math.pow(alanis.ycor()-veneno.ycor(), 2))  # mede a distância entre dois pontos
    if d < 20:
        veneno.setposition(random.randint(-290, 290),
                           random.randint(-290, 290))
        vidas -= 1

    # Diminuindo as vidas
    life.undo()
    life.penup()
    life.write("Vidas: {}".format(vidas), False,
               align="right", font=("Times New Roman", 14, "bold"))

    # Checando a colisão com a comida
    d = math.sqrt(math.pow(alanis.xcor()-comida.xcor(), 2) +
                  math.pow(alanis.ycor()-comida.ycor(), 2))  # mede a distância entre dois pontos
    if d < 20:
        comida.setposition(random.randint(-290, 290),
                           random.randint(-290, 290))

        pontos += 1

    # contando os pontos
    pon.undo()
    pon.penup()
    pon.write("Pontos: {}".format(pontos), False,
              align="left", font=("Times New Roman", 14, "bold"))

    # verificando as vidas
    if vidas == 0:
        game.bgpic("end.gif")
        break

game.mainloop()
