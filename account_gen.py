#taco bell food account generator 1.0
#make sure bluestacks is open and on taco bell app

import random
import string
import os
import json
from time import sleep
import pip

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])
        __import__(package)
        
import_or_install('names')
import_or_install('easygui')
import_or_install('pyautogui')

try:
    import names
    import easygui
    import pyautogui
except:
    pass


def append(data):
    with open("accounts.csv", "a") as file:
        file.write('{},{},{},{}\n'.format(data["first_name"], data["last_name"], data["email"], data["password"]))

def uid():
    password = ''
    password += ''.join(random.choice(string.ascii_lowercase) for i in range(4))
    password += ''.join(random.choice(string.ascii_uppercase) for i in range(4))
    password += ''.join(random.choice(['!', '\\', '{', '_', '}', '[', ']', '(', ')']) for i in range(4))
    return password

def new_user():
    user = {}
    user["first_name"] = names.get_first_name()
    user["last_name"] = names.get_last_name()
    id = uid()
    user["email"] = '{}.{}{}@yahoo.com'.format(user["first_name"], user["last_name"], random.randint(0,1000))
    user["password"] = id
    return user

def run_inputs(coordinates):
    pyautogui.moveTo(coordinates['sign_up'][0], coordinates['sign_up'][1], duration=1) #Sign Up
    pyautogui.click()
    pyautogui.moveTo(coordinates['email_input_box'][0], coordinates['email_input_box'][1], duration=1) #Email Address
    pyautogui.click()
    pyautogui.typewrite('{}\t{}\t{}\t\t{}\t '.format(user["email"], user["first_name"], user["last_name"], user["password"]), interval=.1)
    pyautogui.moveTo(coordinates['confirm_button'][0], coordinates['confirm_button'][1], duration=1)
    pyautogui.click()
    pyautogui.moveTo(coordinates['log_out'][0], coordinates['log_out'][1], duration=4)
    pyautogui.click()
    pyautogui.moveTo(coordinates['okay_buttton'][0], coordinates['okay_buttton'][1], duration=4)
    pyautogui.click()
    pyautogui.moveTo(coordinates['account'][0], coordinates['account'][1], duration=2)
    pyautogui.click()
    
def get_coordinates():
    coordinates = {}
    easygui.msgbox("Follow these steps to record where your script needs to click through the application.\nTo record each button, just hover over them after clicking the \"OK\" button inside of this message box.\nTheir location will be recorded 4 seconds after closing this message.")
    easygui.msgbox("Hover your mouse over the \"Account\" button in the app.")
    sleep(4)
    coordinates["account"] = pyautogui.position()
    easygui.msgbox("Account button location recorded.\nClick the \"Account\" button and then after, click \"OK\" to close this message.")
    easygui.msgbox("Hover your mouse over the \"Sign Up\" button in the app.")
    sleep(4)
    coordinates["sign_up"] = pyautogui.position()
    easygui.msgbox("Sign up button location recorded.\nClick the \"Sign Up\" button and then after, click \"OK\" to close this message.")
    easygui.msgbox("Hover your mouse over the \"Email Address\" text box in the app.")
    sleep(4)
    coordinates["email_input_box"] = pyautogui.position()
    easygui.msgbox("Email address input box has been recorded.\nHover your mouse over the \"Confirm\" button in the app.")
    sleep(4)
    coordinates["confirm_button"] = pyautogui.position()
    easygui.msgbox("Enter in random account details, and click confirm. After clicking confirm, click \"OK\" to close this message.")
    easygui.msgbox("Hover your mouse over the \"Log Out\" button in the app.")
    sleep(4)
    coordinates["log_out"] = pyautogui.position()
    easygui.msgbox("Log out button location recorded.\nClick the \"Log Out\" button and then after, click \"OK\" to close this message.\nDO NOT CLICK THE \"OKAY\" button in the app!")
    easygui.msgbox("Hover your mouse over the \"Okay\" button in the pop up.")
    sleep(5)
    coordinates["okay_buttton"] = pyautogui.position()
    easygui.msgbox("Close the \"Okay\" button.\nAll locations have been recorded. This only needs to be run once, however the Android emulator needs to be in the same place when running.")
    with open('coords.json', 'w') as file:
        file.write(json.dumps(coordinates, indent=4))
    return coordinates
    
if __name__ == "__main__":
    
    coordinates = {}
    if(os.path.exists(os.path.join(os.getcwd(), "coords.json"))):
        with open('coords.json', 'r') as file: 
            coordinates = json.load(file)
    else:
        easygui.msgbox("The script will run 10 times from starting. Make sure the emulator is in the same position as recording.")
        coordinates = get_coordinates()
        sleep(3)
    for i in range(10):
        user = new_user()
        run_inputs(coordinates)
        append(user)