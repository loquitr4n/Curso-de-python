class RemoteControl:
    def __init__(self):
        self.vol = 0
        self.energy = False
        self.channel = 4.0
        self.nf = False

    def power(self):
        if not self.energy:
            self.energy = True
        else:
            self.energy = False

    def mais_canal(self, seta):
        if self.energy:
            self.channel += seta
        else:
            print('Ligue a TV.')

    def menos_canal(self, seta):
        if self.energy:
            self.channel -= seta
        else:
            print('Ligue a TV.')

    def mais_vol(self, seta):
        if self.energy:
            self.vol += seta
        else:
            print('Ligue a TV.')

    def menos_vol(self, seta):
        if self.energy:
            self.vol -= seta
        else:
            print('Ligue a TV.')

    def netflix(self):
        if not self.nf:
            self.nf = True
            print('ABRINDO NETFLIX')
        else:
            self.nf = False


if __name__ == '__main__':
    televisao = RemoteControl()
    televisao.power()
    televisao.mais_canal(9)
    televisao.menos_canal(2)
    televisao.mais_vol(52)
    televisao.menos_vol(20)
    televisao.menos_canal(7)
    televisao.netflix()
    print(televisao.channel)
    print(televisao.vol)

