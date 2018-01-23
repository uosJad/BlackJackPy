from classes.player import Player, Card, Deck
import modules.menu

border = '--'
title = 'Black Jack Py; by Jason Wu'
for i in range(0, len(title)):
    border = border + '-'

print(border)
print(' ' + title)
print(' (Note: needs UTF-8 support)')
print(border)

modules.menu.runMenu()
