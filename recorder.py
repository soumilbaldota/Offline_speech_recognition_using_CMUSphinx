import speech_recognition as sr 
r=sr.Recognizer()
with sr.Microphone() as source:
	print("calibrating , wait")
	r.adjust_for_ambient_noise(source,duration=5)
	print("ok, speak now")
	audio=r.listen(source)
	print('done')

strin=r.recognize_sphinx(audio)
print(strin)

