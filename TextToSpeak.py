import pyttsx3

engine = pyttsx3.init()
engine.setProperty("voice","HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PL-PL_PAULINA_11.0")
engine.setProperty("rate", 150)

engine.say("Witaj, cześć ")
engine.runAndWait()

rate = engine.getProperty("rate")
print(rate)

#voices = engine.getProperty("voices")
#for voice in voices:
#    print("Voice: " + voice.name)
#    print("Voice ID: " + voice.id)
#    print("Voice Languages: " + str(voice.languages))
#    print("Voice Gender: " + str(voice.gender))
#    print("Voice Age: " + str(voice.age))
#    print("\n")
    