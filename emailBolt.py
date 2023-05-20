import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def getInformation():
    try:
        with sr.Microphone() as source:
            print('I am listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def sendEmail(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('Sender_Email', 'Sender_Email_password')
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'user1': 'user1@gmail.com',
    'user2': 'user2@gmail.com',
    'user3': 'user3@gmail.com',
    'user4': 'user4@gmail.com',
    'user5': 'user5@gmail.com',
}

def getEmailContent():
    talk('To Whom you want to send email? ')
    name = getInformation()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email? ')
    subject = getInformation()
    talk('Tell me the text in your email: ')
    message = getInformation()
    sendEmail(receiver, subject, message)
    talk('Your email is sent')
    talk('Do you want to send more email? ')
    send_more = getInformation()
    if 'yes' in send_more:
        getEmailContent()


getEmailContent()