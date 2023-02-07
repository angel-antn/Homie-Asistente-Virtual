import customtkinter
from PIL import Image

import threading

from Homie.homie import init_homie


def init_gui():

    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')

    root = customtkinter.CTk()
    root.title('Homie - Asistente Domótico ')
    root.minsize(700, 500)

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(expand=True)

    label = customtkinter.CTkLabel(master=frame,
                                   image=customtkinter.CTkImage(dark_image=Image.open('Image/logo.png'),
                                                                size=(216, 198)),
                                   text='')
    label.pack(padx=40, pady=40)

    hilo = threading.Thread(target=init_homie)
    hilo.daemon = True
    hilo.start()

    root.mainloop()
