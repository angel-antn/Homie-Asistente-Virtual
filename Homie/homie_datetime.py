import datetime


def conseguir_fecha():

    dia = {
        0: 'lunes',
        1: 'martes',
        2: 'miércoles',
        3: 'jueves',
        4: 'viernes',
        5: 'sábado',
        6: 'domingo'
    }

    mes = {
        1: 'enero',
        2: 'febrero',
        3: 'marzo',
        4: 'abril',
        5: 'mayo',
        6: 'junio',
        7: 'julio',
        8: 'agosto',
        9: 'septiembre',
        10: 'octubre',
        11: 'noviembre',
        12: 'diciembre'
    }

    return f'Hoy es {dia[datetime.datetime.now().date().weekday()]} ' \
           f'{datetime.datetime.now().date().day} de ' \
           f'{mes[datetime.datetime.now().date().month]} del {datetime.datetime.now().date().year}'


def conseguir_hora():

    hora = datetime.datetime.now().time().hour
    minuto = datetime.datetime.now().time().minute
    franja = 'am'

    if hora >= 12:
        hora -= 12
        franja = 'pm'

    if hora == 0:
        hora = 12

    return f'son las {hora} y {minuto} {franja}'
