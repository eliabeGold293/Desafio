"""
5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada? 

"""

# SUPONHA QUE EU ESTEJA NA SALA B (sala_b)
sala_a = []
sala_b = []
sala_c = []

salas = [sala_a, sala_b, sala_c]

class Lampada:

    def __init__(self, interruptor, estado):
        self.interruptor = interruptor
        self.estado = estado

        lampada = [{"interruptor": self.interruptor, "estado": self.estado}]

        if self.interruptor == "interruptor1":
            sala_a.append(lampada)
        elif self.interruptor == "interruptor2":
            sala_b.append(lampada)
        elif self.interruptor == "interruptor3":
            sala_c.append(lampada)
        else:
            print("Digite um nome de lampada válida")

    def ligada():
        if sala_a or sala_b or sala_c:
            at = True
        return at
    
    def desligada():
        if sala_a or sala_b or sala_c:
            at = False
        return at

while True:
    print("\n")
    ususario_lampada = input("Digite 'interruptor1', 'interruptor2', 'interruptor3' ou digite '0' para parar: ")
    
    if ususario_lampada == "0": # condicional de parada
        break
    pessoa_liga = Lampada(ususario_lampada, estado="ligado")



    if pessoa_liga and not sala_b and not sala_c:
        print("\n")
        print("sala_a está ligada | (interruptor1 é da sala_a)")

    elif pessoa_liga and not sala_b and not sala_a:
        print("\n")
        print("sala_c esta ligada | (interruptor3 é da sala_c) ")

    elif pessoa_liga and sala_a and not sala_b:
        print("\n")
        print("sala_c esta ligada | (interruptor3 é da sala_c) ")

    elif pessoa_liga and sala_c and not sala_b:
        print("\n")
        print("sala_a está ligada | (interruptor1 é da sala_a)")

    elif pessoa_liga and not sala_a and not sala_c:
        print("\n")
        print("A sala_b ligou a luz, que sorte a minha | (interruptor2 é da sala_b)")
        print("")
        break

    print("\n")
    for sala in salas:
        print(sala)







    











