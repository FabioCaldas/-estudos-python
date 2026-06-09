class ClienteSpotify:
    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano
        self.musica_atual = None

    def tocar_musica(self, musica):
        self.musica_atual = musica
        print(f"{self.nome} está ouvindo {self.musica_atual} nesse momento")

    def passar_musica(self, proxima_musica):
        self.musica_atual = proxima_musica
        print(f"{self.nome} agora está ouvindo {self.musica_atual}")

    def pausar_musica(self):
        if self.musica_atual:
            print(f"{self.nome} pausou a musica {self.musica_atual}")
        else:
            print(f"{self.nome} não esta tocando nenhuma música")

    def __str__(self):
        return f"Cliente: {self.nome} | Plano: {self.plano} | Música Atual: {self.musica_atual}"

    def cancelar_plano(self):
        self.plano = "Cancelado"
        print(f"{self.nome} cancelou o plano Spotify com sucesso.")


# Exemplo de uso
if __name__ == "__main__":
    cliente1 = ClienteSpotify("Alice", "Premium")
    cliente1.tocar_musica("Shape of You - Ed Sheeran")
    cliente1.passar_musica("Blinding Lights - The Weeknd")
    cliente1.pausar_musica()
    print(cliente1)
    cliente1.cancelar_plano()
    print(cliente1)



 