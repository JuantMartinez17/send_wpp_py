import prepare_messages;
import send_message;

def main():
    try:
        print("Preparando mensajes...")
        prepare_messages.run()
        
        print("\nEnviando mensajes...")
        send_message.run()

        print("\n Todo finalizado correctamente.")

    except Exception as e:
        print("\n Ocurrió un error durante la ejecución:")
        print(str(e))

if __name__ == "__main__":
    main()