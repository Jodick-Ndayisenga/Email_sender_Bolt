# Email Sender Bolt

The provided code is a simple email-sending application using the smtplib, speech_recognition, pyttsx3, and email.message libraries in Python. Let's break down the code and understand what it does and how it accomplishes its task.

### Importing necessary libraries:

```python

import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
```

The code imports the required libraries: smtplib for sending emails, speech_recognition for speech recognition functionality, pyttsx3 for text-to-speech synthesis, and EmailMessage from email.message for creating email messages.

### Initializing speech recognition and text-to-speech engines:

```python

listener = sr.Recognizer()
engine = pyttsx3.init()
```

The code initializes instances of the speech recognition engine (listener) and the text-to-speech engine (engine).

### Defining a function to convert text to speech:

```python

def talk(text):
    engine.say(text)
    engine.runAndWait()
```

The talk() function takes a text parameter, converts it to speech using the engine, and plays the synthesized speech.

### Defining a function to get speech input:

```python

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
```

The getInformation() function uses the microphone as the audio source. It captures speech using the listener and utilizes Google's speech recognition service (listener.recognize_google()) to convert the speech into text. The recognized text is then returned as the result.

### Defining a function to send an email:

```python

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
```

The sendEmail() function takes the email receiver, subject, and message as parameters. It establishes a connection with the SMTP server (smtp.gmail.com in this case), logs in using the sender's email credentials, creates an EmailMessage object, sets the email headers (from, to, subject), sets the email content, and sends the email using the SMTP server.

    Defining a dictionary of email addresses:

```python

email_list = {
    'user1': 'user1@gmail.com',
    'user2': 'user2@gmail.com',
    'user3': 'user3@gmail.com',
    'user4': 'user4@gmail.com',
    'user5': 'user5@gmail.com',
}
```

The email_list dictionary stores a mapping of user names to their corresponding email addresses.

### Defining a function to get email content and send the email:

```python
def getEmailContent():
    talk('To whom do you want to send an email?')
    name = getInformation()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = getInformation()
    talk('Tell me the text in your email:')
    message = getInformation()
    sendEmail(receiver, subject, message)
    talk('Your email is sent.')
    talk('Do you want to send more email? ')
    send_more = getInformation()
    if 'yes' in send_more:
        getEmailContent()
```

### Prompting for the recipient:

    The function uses the talk() function to speak the prompt "To whom do you want to send an email?".
    It then calls the getInformation() function to capture speech input and assigns it to the variable name.
    The name is used to look up the corresponding email address from the email_list dictionary and assigns it to the variable receiver.

### Prompting for the subject:

    The function uses the talk() function to speak the prompt "What is the subject of your email?".
    It again calls the getInformation() function to capture speech input and assigns it to the variable subject.

### Prompting for the message:

    The function uses the talk() function to speak the prompt "Tell me the text in your email:".
    It calls the getInformation() function to capture speech input and assigns it to the variable message.

### Sending the email:

    The function calls the sendEmail() function with the receiver, subject, and message as arguments to send the email.
    The sendEmail() function utilizes the provided email address, subject, and message content to send the email using the smtplib library.

### Notifying the completion:

    The function uses the talk() function to inform the user that their email has been sent.

### Recursive call for sending more emails:

    The function uses the talk() function to ask the user if they want to send more emails.
    It calls the getInformation() function to capture speech input and assigns it to the variable send_more.
    If the captured input contains the word "yes", the function recursively calls itself, allowing the user to send another email.
