import pandas

file = pandas.read_excel("CEOM - Automatización de Mensajes por WhatsApp", sheet_name="DATOS DE ENVIO", skiprows=2)

file.columns = ["telefono", "fecha", "hora", "direccion", "motivo", "instrucciones"]

messages = []

for i, row in file.iterrows():
    if pandas.isna(row["telefono"]):
        continue
    numero = f"+549{int(row['telefono'])}"
    fecha = pd.to_datetime(row["fecha"]).strftime('%d/%m/%Y')
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