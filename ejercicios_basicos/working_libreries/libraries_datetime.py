"""_summary_

    Using datetime library

"""

from datetime import date, datetime as dt

today: date = date.today()
print(str(today))
print(repr(today))

# fecha y hora
fecha_hora = dt.now()
print(fecha_hora)

# year
print(fecha_hora.year)
# month
print(fecha_hora.month)
# day
print(fecha_hora.day)
# hora
print(fecha_hora.hour)
# minutos
print(fecha_hora.minute)
# segundos
print(fecha_hora.second)