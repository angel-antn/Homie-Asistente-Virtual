import speech_recognition
from gtts import gTTS
from playsound import playsound
import os
import pywhatkit
import random

from Homie.homie_bcv import get_dolar_bcv, get_euro_bcv, calc_dolar, calc_euro
from Homie.homie_datetime import conseguir_fecha, conseguir_hora
from Homie.homie_horoscope import get_horoscopo
from Homie.homie_weather import is_gonna_rain, get_temp
from Homie.homie_wikipedia import get_wiki


def escuchar():
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        recognizer.pause_threshold = 0.5
        audio = recognizer.listen(source)
        try:
            order = recognizer.recognize_google(audio, language='es')
            return order
        except speech_recognition.UnknownValueError:
            return 'Ha ocurrido un error inesperado'
        except speech_recognition.RequestError:
            return 'Ha ocurrido un error inesperado'


def hablar(mensaje):
    speech = gTTS(text=mensaje, lang='es', slow=False)
    speech.save('Sounds/respuesta.mp3')
    playsound(sound='Sounds/respuesta.mp3', block=True)
    os.remove('Sounds/respuesta.mp3')


def init_homie(gui_object):
    primera_vuelta = True
    hablar('hola soy Homie, tu asistente domótico')

    while True:

        if primera_vuelta:
            hablar(random.choice([
                '¿Que puedo hacer por ti?',
                '¿En que puedo ayudarte?'
            ]))
            primera_vuelta = False
        else:

            while True:
                order = escuchar().lower()
                if 'homie' in order or 'homy' in order or 'home' in order or 'omi' in \
                        order or 'jomi' in order or 'sony' in order or 'ovi' in order:
                    hablar(random.choice([
                        '¿Que más puedo hacer por ti?',
                        '¿Hay algo más que pueda hacer por ti?',
                        '¿En que más puedo ayudarte?'
                    ]))
                    break

        playsound(sound='Sounds/sfx_hablar.mp3', block=False)
        order = escuchar().lower()

        if 'alexa' in order or 'siri' in order:

            hablar('no me parece gracioso...')

        elif 'soy ' in order:

            order = order.split()
            nombre = order[order.index('soy') + 1]
            hablar(f'hola {nombre}, mucho gusto')
            primera_vuelta = True

        elif 'saluda a ' in order:

            nombre = order.replace('saluda a ', '')
            hablar(f'hola {nombre}, un placer')

        elif 'cómo estás' in order:

            hablar('muy bien, gracias por preguntar')

        elif 'dame la hora' in order or 'qué hora es' in order:

            hablar(conseguir_hora())

        elif 'dame la fecha' in order or 'qué día es hoy' in order:

            hablar(conseguir_fecha())

        elif 'quiero escuchar ' in order:

            hablar('enseguida')
            nombre = order.replace('quiero escuchar ', '')
            pywhatkit.playonyt(topic=nombre, use_api=False, open_video=True)

        elif 'quiero jugar' in order\
                or 'blackjack' in order or 'black jack' in order or '21' in order or 'veintiuno' in order:
            hablar('Juguemos blackjack')
            from Homie.homie_blackjack import HomieBlackjack
            HomieBlackjack(gui_object)

        elif 'pronóstico del clima' in order and 'en' in order:

            hablar('entendido, dame un momento')
            city = order.split('en')
            hablar(is_gonna_rain(city[1]))

        elif 'temperatura' in order and 'de' in order:

            hablar('entendido, dame un momento')
            city = order.split('de')
            hablar(get_temp(city[1]))

        elif 'frase' in order or 'lírica' in order:

            words = []
            with open('Quotes/quotes.txt', mode='r', encoding='utf-8') as file:
                words += file.readlines()
            hablar(random.choice(words).split('-')[0])

        elif 'chiste' in order:

            words = []
            with open('Quotes/chistes.txt', mode='r', encoding='utf-8') as file:
                words += file.readlines()
            hablar(random.choice(words))

        elif 'horóscopo' in order and 'de' in order and \
                (('aries' in order and order.split().index('aries') == order.split().index('de') + 1) or
                 ('tauro' in order and order.split().index('tauro') == order.split().index('de') + 1) or
                 ('géminis' in order and order.split().index('géminis') == order.split().index('de') + 1) or
                 ('cáncer' in order and order.split().index('cáncer') == order.split().index('de') + 1) or
                 ('leo' in order and order.split().index('leo') == order.split().index('de') + 1) or
                 ('virgo' in order and order.split().index('virgo') == order.split().index('de') + 1) or
                 ('libra' in order and order.split().index('libra') == order.split().index('de') + 1) or
                 ('escorpio' in order and order.split().index('escorpio') == order.split().index('de') + 1) or
                 ('sagitario' in order and order.split().index('sagitario') == order.split().index('de') + 1) or
                 ('capricornio' in order and order.split().index('capricornio') == order.split().index('de') + 1) or
                 ('acuario' in order and order.split().index('aries') == order.split().index('de') + 1) or
                 ('piscis' in order and order.split().index('aries') == order.split().index('de') + 1)):

            signo = order.split(' de ')[1].split()[0]
            hablar('entendido, dame un momento')
            try:
                hablar(get_horoscopo(signo))
            except Exception as e:
                hablar(f'Lo siento, no he podido conseguir el horóscopo de {signo}')
                print(e)

        elif 'busca en wikipedia' in order:

            buscar = order.split('wikipedia')[1]
            hablar('entendido, dame un momento')
            try:
                hablar(get_wiki(buscar))
            except Exception as e:
                hablar(f'Lo siento, no he podido conseguir nada en wikipedia acerca de {buscar}')
                print(e)

        elif 'precio del dólar' in order or 'en cuánto está el dólar' in order:

            try:
                hablar(get_dolar_bcv())
            except Exception as e:
                hablar(f'Lo siento, no he podido conseguir el precio del dólar')
                print(e)

        elif 'cuánto son' in order and '$' in order:

            text = order.split()
            if 'coma' not in order:
                for i in text:
                    if '$' in i:
                        text = i.replace('$', '')
                        break
            else:
                text_2 = order.split()
                for i in range(len(text)):
                    if 'coma' == text[i]:
                        text = text[i-1]
                        break
                for i in text_2:
                    if '$' in i:
                        text += f".{i.replace('$', '')}"
                        break
            try:
                hablar(calc_dolar(float(text)))
            except Exception as e:
                hablar(f'Lo siento, no he podido conseguir el precio de {text} dólares')
                print(e)

        elif 'cuánto son' in order and '€' in order:

            text = order.split()
            if 'coma' not in order:
                for i in range(len(text)):
                    if '€' == text[i]:
                        text = text[i - 1]
                        break
            else:
                text_2 = order.split()
                for i in range(len(text)):
                    if 'coma' == text[i]:
                        text = text[i-1]
                        break
                for i in range(len(text_2)):
                    if '€' == text_2[i]:
                        text += f".{text_2[i-1]}"
                        break
            try:
                hablar(calc_euro(float(text)))
            except Exception as e:
                hablar(f'Lo siento, no he podido conseguir el precio de {text} euros')
                print(e)

        elif 'precio del euro' in order or 'en cuánto está el euro' in order:

            try:
                hablar(get_euro_bcv())
            except Exception as e:
                hablar(f'Lo siento, no he podido conseguir el precio del euro')
                print(e)

        elif 'quién es la más linda' in order:

            hablar('obviamente yo')

        elif 'cambia el modo' in order or 'cambia de modo' in order or 'cambia el tema' in order\
                or 'cambia de tema' in order:
            gui_object.update_theme()
            if gui_object.theme == 0:
                hablar('modo claro activado')
            else:
                hablar('modo oscuro activado')

        elif 'nada' in order:

            hablar('entendido, llámame si necesitas algo')

        else:

            playsound(sound='Sounds/sfx_error.mp3', block=False)
            hablar('no entiendo')
            primera_vuelta = True
