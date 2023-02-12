import random
import time

from Homie.homie import escuchar, hablar


# a: 1 or 11
# j, q, k = 10
# < 17 otra carta


def get_points(cards):
    ases = 0
    points = 0
    for card in cards:
        if card == 'a':
            ases += 1
            points += 11
        elif card == 'j' or card == 'q' or card =='k':
            points += 10
        else:
            points += card

    while ases > 0 and points > 21:
        ases -= 1
        points -= 10

    return points


class HomieBlackjack:

    def __init__(self, gui_object):
        self.gui = gui_object
        self.cards = ('a', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'j', 'q', 'k')
        self.homie_cards = [random.choice(self.cards)]
        self.your_cards = [random.choice(self.cards)]
        self.gui.blackjack(self.homie_cards, self.your_cards)
        self.game_on()

    def game_on(self):

        while True:
            if get_points(self.your_cards) > 21:
                hablar('vaya, te has pasado de 21. has perdido, lo siento')
                break
            elif get_points(self.your_cards) == 21:
                hablar('Wao tienes 21. has ganado, felicidades')
                break
            else:
                order = escuchar().lower()
                if 'dame' in order:
                    self.your_cards.append(random.choice(self.cards))
                    self.gui.blackjack(self.homie_cards, self.your_cards)
                elif 'me quedo' == order:
                    while get_points(self.homie_cards) < 17:
                        self.homie_cards.append(random.choice(self.cards))
                        self.gui.blackjack(self.homie_cards, self.your_cards)
                        time.sleep(1)
                    if get_points(self.homie_cards) > 21:
                        hablar('vaya, creo que me he pasado de 21. he perdido, buena partida')
                    elif get_points(self.homie_cards) == 21:
                        hablar('Wao. tengo 21, lo siento')
                    elif get_points(self.homie_cards) > get_points(self.your_cards):
                        hablar(f'Tengo {get_points(self.homie_cards)} y tu tienes {get_points(self.your_cards)}. '
                               f'has perdido, lo siento')
                    elif get_points(self.homie_cards) < get_points(self.your_cards):
                        hablar(f'Tengo {get_points(self.homie_cards)} y tu tienes {get_points(self.your_cards)}. '
                               f'he perdido, felicidades')
                    else:
                        hablar(f'vaya, ambos tenemos {get_points(self.your_cards)}. '
                               f'parece que es un empate, buena partida')
                    break

                elif 'tengo' in order:
                    hablar(f'actualmente tienes {get_points(self.your_cards)} puntos')
                elif 'tienes' in order:
                    hablar(f'tengo {get_points(self.homie_cards)} puntos')
                elif 'salir' in order or 'vámonos' in order or 'salgamos' in order:
                    hablar('entendido')
                    break

        self.gui.main_window()
