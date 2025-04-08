import pandas
import pickle

file = pandas.read_excel("CEOM - Automatización de Mensajes por WhatsApp.xlsx", sheet_name="DATOS DE ENVÍO", skiprows=2)

file.columns = ["telefono", "fecha", "hora", "direccion", "motivo", "instrucciones"]

messages = []

for i, row in file.iterrows():
    if pandas.isna(row["telefono"]):
        continue
    numero = f"+549{int(row['telefono'])}"
    fecha = pandas.to_datetime(row["fecha"]).strftime('%d/%m/%Y')
    hora = row["hora"].strftime('%H:%M')
    mensaje = f"""Hola! Este es un recordatorio para tu turno médico:
    📅 *Fecha:* {fecha}
    🕒 *Hora:* {hora}
    📍 *Dirección:* {row['direccion']}
    📝 *Motivo:* {row['motivo']}
    📌 *Instrucciones:* {row['instrucciones']}

    Por favor, confirmá tu asistencia. ¡Gracias!
    """
    messages.append((numero, mensaje))

with open("messages.pkl", "wb") as f:
    pickle.dump(messages, f)

print(f"Se prepararon {len(messages)} mensajes.")