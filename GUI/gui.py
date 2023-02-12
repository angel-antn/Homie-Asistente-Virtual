import threading
import tkinter as tk
from Homie.homie import init_homie

BACKGROUND = ('#fff', '#1a1c28')
PRIMARY_COLOR = '#4d98ff'
FONT = ('Arial black', 17, 'bold')


class Gui:

    def __init__(self):

        self.theme = 0

        self.widget_list = []

        self.root = tk.Tk()
        self.root.title('Homie - Asistente Domótico ')
        self.root.minsize(1000, 800)
        self.root.iconbitmap('Image/icon.ico')
        self.root.config(background=BACKGROUND[self.theme])

        self.frame = tk.Frame(background=BACKGROUND[self.theme])
        self.frame.pack(expand=True)

        self.label = None

        self.logo = tk.PhotoImage(file='Image/logo.png')
        self.logo_2 = tk.PhotoImage(file='Image/logo_2.png')
        self.cards = {
            'a': tk.PhotoImage(file='Image/Cards/a.png'),
            2: tk.PhotoImage(file='Image/Cards/2.png'),
            3: tk.PhotoImage(file='Image/Cards/3.png'),
            4: tk.PhotoImage(file='Image/Cards/4.png'),
            5: tk.PhotoImage(file='Image/Cards/5.png'),
            6: tk.PhotoImage(file='Image/Cards/6.png'),
            7: tk.PhotoImage(file='Image/Cards/7.png'),
            8: tk.PhotoImage(file='Image/Cards/8.png'),
            9: tk.PhotoImage(file='Image/Cards/9.png'),
            10: tk.PhotoImage(file='Image/Cards/10.png'),
            'j': tk.PhotoImage(file='Image/Cards/j.png'),
            'q': tk.PhotoImage(file='Image/Cards/q.png'),
            'k': tk.PhotoImage(file='Image/Cards/k.png'),
        }

        self.main_window()

        hilo = threading.Thread(target=init_homie, args=(self,))
        hilo.daemon = True
        hilo.start()

    def main_window(self):

        self.clean()

        self.label = tk.Label(self.frame, image=self.logo, background=BACKGROUND[self.theme])
        self.label.grid(row=0)

        self.widget_list += [self.label]

    def update_theme(self):
        self.theme = 1 if self.theme == 0 else 0
        self.root.config(background=BACKGROUND[self.theme])
        self.frame['background'] = BACKGROUND[self.theme]
        if self.label is not None:
            self.label['background'] = BACKGROUND[self.theme]

    def blackjack(self, homie_cards, your_cards):

        self.clean()

        homie_frame = tk.Frame(self.frame, background=BACKGROUND[self.theme])
        homie_frame.grid(row=0)

        logo_label = tk.Label(self.frame, image=self.logo_2, background=BACKGROUND[self.theme])
        logo_label.grid(row=1, pady=50)

        your_frame = tk.Frame(self.frame, background=BACKGROUND[self.theme])
        your_frame.grid(row=2)

        self.widget_list += [homie_frame, your_frame, logo_label]

        for i in range(len(homie_cards)):
            card = tk.Label(homie_frame, image=self.cards[homie_cards[i]], background=BACKGROUND[self.theme])
            card.grid(row=0, column=i, padx=(0, 10))
            self.widget_list.append(card)

        for i in range(len(your_cards)):
            card = tk.Label(your_frame, image=self.cards[your_cards[i]], background=BACKGROUND[self.theme])
            card.grid(row=0, column=i, padx=(0, 10))
            self.widget_list.append(card)

    def clean(self):
        for widget in self.widget_list:
            widget.destroy()
