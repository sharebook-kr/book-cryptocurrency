class SuperMario:
    def __init__(self):
        self.pos = 0
    def forward(self):
        self.pos = self.pos + 20

mario = SuperMario()
mario.forward()
print(mario.pos)
