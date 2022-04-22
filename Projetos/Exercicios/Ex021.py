# Faça um programa em python que abra e reproduza o audio de um arquivo mp3


from pygame import mixer
mixer.init()
mixer.music.load('pa11.mp3')
mixer.music.play()
while(mixer.music.get_busy()): pass

