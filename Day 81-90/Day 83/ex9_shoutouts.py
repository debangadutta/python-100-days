'''
Give shoutout to everyone using text-to-speech (pywin32)
'''
import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")

speak.Speak("Welcome to shoutout session!")

name_list = ["Debanga", "Ramesh", "Harry", "Tim", "Shinchan"]
i=1

for name in name_list:
    print(name)
    speak.Speak(f"Shoutout to number {i}: {name}")
    i+=1

speak.Speak("Thank you for coming!")