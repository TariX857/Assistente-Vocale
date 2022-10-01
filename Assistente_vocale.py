from pyttsx3 import init
from speech_recognition import Recognizer, Microphone
import webbrowser
from random import choice

engine = init()
engine.say("In cosa posso aiutarti?")
engine.runAndWait()
r = Recognizer()

with Microphone() as source:
    print("Sta ascoltando...")
    audio = r.listen(source)
    testo = r.recognize_google(audio, language="it-IT").lower()
    risposta = "Riprova..."
    print(testo)
    if "ricetta" in testo:
        risposta = "Ho create per te un sito per questo!"
        webbrowser.open("#") #copia l'url della pagina html che ce nella cartella ricetta
    elif any(parola in testo for parola in ["ora", "ore", "che ore sono", "dimmi l'orario", "dimmi l'ora", "in che mese siamo", "che giorno della settimana è", "che giorno del mese è"]):
        webbrowser.open("https://www.lorologioonline.it/")
        risposta = "Ti ho aperto un orologio online per vederlo!"
    elif testo.startswith(("cosa", "come", "quanto")):
        risposta = choice(["Non è nelle mie capacità", "Mi spiace non ho capito", "Se ripeti posso aiutarti meglio"])
    engine.say(risposta)
    engine.runAndWait()


input("\nOra puoi chiudere la finestra.\nSe hai ancora bisogno di me chiudi e riapri\nPremi invio per chiudere!")