import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
from gtts import gTTS
import sounddevice as sd
import soundfile as sf
import pywhatkit
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    tts = gTTS(text=text, lang='th', tld='com')
    filename = "voice.mp3"
    tts.save(filename)
    data, fs = sf.read(filename, dtype='float32')
    sd.play(data, fs)
    sd.wait()


def commands():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source, timeout=2)

    try:
        print("Processing...")
        query = r.recognize_google(audio, language='th-TH')
        print(f"User: {query}\n")

    except Exception as e:
        print(e)
        print("Please try again...")
        return "None"
    return query


def get_username():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        speak("กรุณาตั้งชื่อให้ฉัน Please name me")
        print("Wait for name...")
        audio = r.listen(source)

    try:
        name = r.recognize_google(audio, language='th-TH')
        return name
    except:
        print("ไม่สามารถรับรู้เสียงได้ กรุณาลองใหม่อีกครั้ง")
        return None


name = None
while not name:
    name = get_username()


def wishings(name):
    hour = int(datetime.datetime.now().hour)

    if hour >= 5 and hour < 10:
        speak(f"สวัสดีตอนเช้าค่ะ! ฉันชื่อ{name}")

    elif hour >= 11 and hour < 13:
        speak(f"สวัสดีตอนเที่ยงค่ะ! ฉันชื่อ{name}")

    elif hour >= 13 and hour < 16:
        speak(f"สวัสดีตอนบ่ายค่ะ! ฉันชื่อ{name}")

    elif hour >= 16 and hour < 19:
        speak(f"สวัสดีตอนเย็นค่ะ! ฉันชื่อ{name}")

    elif hour >= 19 and hour < 24:
        speak(f"สวัสดีตอนดึกค่ะ! ฉันชื่อ{name}")

    speak("มีอะไรให้รับใช้คะ")


if __name__ == "__main__":
    while True:
        wishings(name)
        query = commands().lower()
        if 'เวลา' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"ได้ค่ะตอนนี้เวลา {strTime}")
            print(strTime)

        elif 'เปิด cmd' in query:
            speak("โอเคกำลังเปิด cmd")
            os.startfile("C:\Windows\system32\cmd.exe")

        elif 'เปิดบราวเซอร์' in query:
            speak("โอเคกำลังเปิดบราวเซอร์")
            webbrowser.open("https://google.com")

        elif 'เปิดแผนที่' in query:
            speak("โอเคกำลังเปิดแผนที่")
            webbrowser.open("https://www.google.co.th/maps")

        elif 'เครื่องคิดเลข' in query:
            os.startfile('calc.exe')
            speak("กำลังเปิดเครื่องคิดเลข")

        elif 'ค้นหา' in query:
            search_term = query.split("ค้นหา")[-1].strip()
            search_url = f"https://www.google.com/search?q={search_term}"
            speak(f"กำลังค้นหา {search_term} ใน Google")
            webbrowser.open(search_url)
            print(search_term)

        elif 'เล่นเพลง' in query:
            song = query.split("เล่นเพลง")[-1].strip()
            pywhatkit.playonyt(song)
            speak(f"กำลังเล่นเพลง {song} บน YouTube")

        elif 'จบ' in query or 'ปิด' in query:
            sys.exit()

        else:
            try:
                result = eval(query.replace('คำนวณ', ''))
                speak(f"คำตอบคือ {result}")
                print(f"result {result}")
            except:
                speak("ขออภัย ไม่สามารถดำเนินการได้ โปรดลองอีกครั้ง")
