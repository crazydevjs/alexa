while(True):
    import speech_recognition as sr 
    import pyttsx3
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        text = r.recognize_google(audio_data)
        print(text)
        if text=='hey Alexa how are you':
            engine = pyttsx3.init()
            engine.say("I am fine, Mr. Deepak How are you")
            engine.runAndWait()
            continue
        if text=='hi Alexa how are you':
            engine = pyttsx3.init()
            engine.say("I am fine, Mr. Deepak How are you")
            engine.runAndWait()
            continue
        if text=='can you tell me something about coding':
            engine = pyttsx3.init()
            engine.say("coding is the use of computer programming languages to give computers and machines instructions on what actions to perform. Coding is the way humans communicate with machines, and it allows us to create software like programs, operating systems, and mobile apps")
            engine.runAndWait()
            continue
        if text=='I am fine':
            engine = pyttsx3.init()
            engine.say("Good")
            engine.runAndWait()
            continue
        if text=='stop Alexa':
            engine = pyttsx3.init()
            engine.say("Okay!!")
            engine.runAndWait()
            break
        if text=='shut up Alexa':
            engine = pyttsx3.init()
            engine.say("Okay!!")
            engine.runAndWait()
            break
        
