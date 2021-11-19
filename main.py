import requests
from bs4 import BeautifulSoup

def getting_the_code():
    ''' this function takes no input and scrapes a website to get a table for Morse code
    and returns the table as soup object'''
    url = 'https://encyclopedia2.thefreedictionary.com/List+of+Morse+Code'
    response= requests.get(url).text
    soup = BeautifulSoup(response,'html.parser')
    table = soup.find(name='table')
    return table

table = getting_the_code()

def Morse_dict(table):
    '''This function takes the soup-object table returned by another function and return
    a dictionary containing the letter and code as key-value pairs'''
    morse_code = {}
    for row in table.find_all('tr')[2:39]:
        if 'and P' in row.text[1: ].strip():
            pass
        else:
            morse_code[row.text[0]] = row.text[1: ].strip().replace('\xa0','')

    morse_code[''] = ' '
    morse_code[' '] = '|'
    return morse_code

morse_code = Morse_dict(table)


def text_to_morse(text):
    ''' This function takes input as text from the user and returns a string with Morse code
     to this text'''
    code = ''
    for char in text:
            code += morse_code[char.upper()] + morse_code['']
    return code[:-1]


def morse_to_text(morse_code, code):
    ''' This function takes Morse code from the user and returns a string containing the converted text'''
    reverse_morse_code = {v: k for k, v in morse_code.items()}
    text = ''
    for char in code.split(' '):
        text += reverse_morse_code[char]
    return text.title()

while True:
    cont = input('Enter T for text to Morse, Or enter M for Morse to text or Enter to exit: ')
    if cont.lower() == 't':
        text = input('Enter text to convert to Morse code: ')
        try:
            print(text_to_morse(text))
        except KeyError:
            print('\n Please provide valid text A-z and 0-9 \n')
            continue
    elif cont.lower() == 'm':
        code = input('Enter Morse code to convert to text: ')
        try:
            print(morse_to_text(morse_code,code))
        except KeyError:
            print('\nPlease provide valid Morse code - and . and spaces and | for word separation \n')
            continue
    else:
        break