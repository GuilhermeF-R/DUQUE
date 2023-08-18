import speech_recognition as sr
import pyttsx3
import datetime
import pyautogui as pg
from time import sleep
def enviarMensagem_wpp():
    #Abrir Zap no Chrome
    pg.press('win')
    sleep(0.8)
    pg.write('brave')
    sleep(1)
    pg.press('enter')
    sleep(2)
    pg.write('https://web.whatsapp.com/')
    sleep(1)
    pg.press('enter')
    sleep(9)


def get_current_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Diga algo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Reconhecendo...")
            command = recognizer.recognize_google(audio, language="pt-BR")
            print("Comando detectado:", command)
            process_command(command.lower())

        except sr.UnknownValueError:
            print("Não foi possível entender o áudio.")
        except sr.RequestError as e:
            print(f"Erro ao solicitar resultados do serviço de reconhecimento: {e}")

def process_command(command):
    if "olá" in command:
        speak("Olá! Como posso ajudar?")
    elif "como você está" in command:
        speak("Estou bem, obrigada por perguntar!")
    elif "qual é a hora" in command:
        current_time = get_current_time()
        speak(f"Hora atual, {current_time}")
        print()
    elif "tchau" in command:
        speak("Até logo! Tenha um bom dia.")
        exit()

    elif "mensagem no whatsapp" in command:
        enviarMensagem_wpp()
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            speak("Para quem quer enviar?")
            recognizer.adjust_for_ambient_noise(source)
            audioContato = recognizer.listen(source)

            try:
                print("Reconhecendo...")
                contato_nome = recognizer.recognize_google(audioContato, language="pt-BR")
                print("Comando detectado:", contato_nome)

            except sr.UnknownValueError:
                print("")
            except sr.RequestError as e:
                print(f"Erro ao solicitar resultados do serviço de reconhecimento: {e}")

        pg.click(x = 218, y = 199)
        sleep(0.5)
        pg.write(contato_nome)
        sleep(1)
        pg.click(x = 234, y = 331)
        sleep(1.5)

        with sr.Microphone() as source:
            speak('O que deseja enviar?')
            recognizer.adjust_for_ambient_noise(source)
            audioMensagem = recognizer.listen(source)

            try:
                    print("Reconhecendo...")
                    mensagemContato = recognizer.recognize_google(audioMensagem, language="pt-BR")
                    print("Comando detectado:", mensagemContato)
                    process_command(mensagemContato.lower())

            except sr.UnknownValueError:
                print("Não foi possível entender o áudio.")
            except sr.RequestError as e:
                print(f"Erro ao solicitar resultados do serviço de reconhecimento: {e}")

        pg.write(mensagemContato)
        sleep(2)
        pg.press('enter')

    else:
        speak("Desculpe, não entendi o comando.")

if __name__ == "__main__":
    speak("Olá! Estou ouvindo.")
    while True:
        main()
