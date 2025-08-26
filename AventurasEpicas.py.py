class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo.lower()

    def atacar(self):
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        else:
            ataque = "golpe desconhecido"
        print(f"o {self.tipo} atacou usando {ataque}")

if __name__ == "__main__":
    herois = [
        Heroi("Gandalf", 100, "mago"),
        Heroi("Conan", 35, "guerreiro"),
        Heroi("Li Mei", 28, "monge"),
        Heroi("Hattori", 30, "ninja")
    ]
    for heroi in herois:
        heroi.atacar()
