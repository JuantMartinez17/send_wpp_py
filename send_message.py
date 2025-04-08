import pywhatkit
from datetime import datetime
import pickle

def run ():
    with open("messages.pkl", "rb") as file:
        messages = pickle.load(file)

    for i, (num, msg) in enumerate(messages):
        now = datetime.now()
        hour = now.hour
        minute = now.minute + 1

        print(f"[{i+1}/{len(messages)}] Enviando mensaje a {num} a las {hour}:{minute:02d}...")

        try:
            pywhatkit.sendwhatmsg_instantly(
                phone_no=num,
                message=msg,
                wait_time=5,
                tab_close=True,
                close_time=3
            )
        except Exception as e:
            print(f"Error al enviar el mensaje a {num}: {e}")