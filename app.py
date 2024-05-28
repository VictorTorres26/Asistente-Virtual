import speech_recognition as sr
import pywhatkit
import pyttsx3
import wikipedia
import datetime
import keyboard
import os
from pygame import mixer
import subprocess as sub

# import datetime
# import keyboard

name = "Yarvis"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


sites = {
    'abc': 'abc.com/live',
    'amazon prime video': 'amazon.com/primevideo',
    'appletvplus': 'apple.com/apple-tv-plus',
    'brainlylat': 'brainly.lat',
    'callbell': 'callbell.io',
    'cbsall_access': 'cbs.com/all-access',
    'clamatocubano': 'clamato.com',
    'codesnippets': 'codesnippets.joyent.com',
    'crunchyroll': 'crunchyroll.com',
    'deporplay': 'depor.com',
    'deporequipo': 'depor.com',
    'dailymotion': 'dailymotion.com',
    'disney': 'disneyplus.com',
    'edteam': 'edteam.com',
    'espn': 'espn.com/watch/espnplus',
    'funimation': 'funimation.com',
    'google': 'google.com',
    'google_sites': 'sites.google.com',
    'hbo_max': 'hbomax.com',
    'hulu': 'hulu.com',
    'instagram': 'instagram.com',
    'la_tradicional_de_salgado': 'facebook.com/LaTradicionalDeSalgado',
    'lemonbe': 'lemonbe.com',
    'linkedin': 'linkedin.com',
    'mamma_pasta': 'facebook.com/MammaPasta',
    'medium': 'medium.com',
    'middlesex_health': 'middlesexhealth.org',
    'microsoft': 'microsoft.com',
    'nbc': 'nbc.com/live',
    'netflix': 'netflix.com',
    'peacock': 'peacocktv.com',
    'pinterest': 'pinterest.com',
    'problemas_matematicos': 'bbc.com/mundo',
    'quora': 'quora.com',
    'reddit': 'reddit.com',
    'retrogaming': 'retrogaming.com',
    'slingtv': 'sling.com',
    'snapchat': 'snapchat.com',
    'soundcloud': 'soundcloud.com',
    'spotify': 'spotify.com',
    'stackoverflow': 'stackoverflow.com',
    'target': 'target.com',
    'ted': 'ted.com',
    'tiktok': 'tiktok.com',
    'tubi': 'tubitv.com',
    'twitter': 'twitter.com',
    'twitch': 'twitch.tv',
    'udemy': 'udemy.com',
    'ups': 'ups.com',
    'vimeo': 'vimeo.com',
    'vudu': 'vudu.com',
    'walmart': 'walmart.com',
    'wikipedia': 'wikipedia.org',
    'whatsapp': 'web.whatsapp.com',
    'wordpress': 'wordpress.com',
    'youtube': 'youtube.com',
    'youtube_tv': 'tv.youtube.com',
    'zara': 'zara.com'
    # Agrega aquí más sitios web utilizando la misma sintaxis
}


def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    rec = ''
    try:
        with sr.Microphone() as source:
            print('Escuchando...')
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language="es")
            rec = rec.lower()

            if name in rec:
                rec = rec.replace(name, '')

    except:
        print('Algo ha salido mal...')
    return rec


def run_molly():
    while True:
        rec = listen()

        if 'reproduce' in rec:
            music = rec.replace('reproduce', '')
            print("Reproduciendo" + music)
            talk("Reproduciendo" + music)
            pywhatkit.playonyt(music)

        elif 'busca' in rec:
            busca = rec.replace('busca', '')
            wikipedia.set_lang('es')
            wiki = wikipedia.summary(busca, 2)
            print(busca + ': ' + wiki)
            talk(wiki)

        elif 'alarma' in rec:
            num = rec.replace('alarma', '')
            num = num.strip()
            talk('Alarma activada a las ' + num + 'horas')
            print('Alarma activada a las ' + num + 'horas')

            while True:
                if datetime.datetime.now().strftime('%H:%M') == num:
                    print('DESPIERTA!!!')
                    mixer.init()
                    mixer.music.load('mp3/alarma_gallo.mp3')
                    mixer.music.play()
                    if keyboard.read_key() == 's':
                        mixer.music.stop()
                        break

        elif 'abre' in rec:
            abre = rec.replace('abre', '')
            for site in sites:
                if site in rec:
                    sub.call(f'start chrome.exe {sites[site]}', shell=True)
                    print(f'Abriendo {site}')
                    talk(f'Abiendo {site}')

        elif 'cierra' in rec:
            adios = rec.replace('adios', '')
            print('Hasta luego')
            talk('Hasta luego')
            break


if __name__ == '__main__':
    run_molly()
