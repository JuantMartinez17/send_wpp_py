import pywhatkit
import datetime

numero = "+5491133292257"

mensaje = "Probando script con libreria pywhatkit"

now = datetime.datetime.now()

hora_envio = now.hour

min_envio = now.minute + 1


pywhatkit.sendwhatmsg(numero, mensaje, hora_envio, min_envio)