import pandas
import pickle

def run():
    file = pandas.read_excel("CEOM - Automatización de Mensajes por WhatsApp.xlsx", sheet_name="DATOS DE ENVÍO", skiprows=2)
    data = file.values
    file.columns = ["telefono", "fecha", "hora", "direccion", "motivo", "instrucciones"]

    messages = []

    for i in range(len(data)):
        row = data[i]
        phone = row[0]
        if pandas.isna(row["phone"]):
            continue
        date = pandas.to_datetime(row[1]).strftime('%d/%m/Y')
        time = pandas.to_datetime(row[2]).strftime('%H:%M')
        address = row[3]
        appointment = row[4]
        instruction = row[5]
        phone = f"+549{int(phone)}"
        message = f"""Hola! Este es un recordatorio para tu turno médico:
        📅 *Fecha:* {date}
        🕒 *Hora:* {time}
        📍 *Dirección:* {address}
        📝 *Motivo:* {appointment}
        📌 *Instrucciones:* {instruction}

        Por favor, confirmá tu asistencia. ¡Gracias!
        """

        messages.append((phone, message))

    with open("messages.pkl", "wb") as f:
        pickle.dump(messages, f)

    print(f"Se prepararon {len(messages)} mensajes.")