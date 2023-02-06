#String to Morse Code

MORSE_MAPPING = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    "'": '.----.',
}


def string_to_morse(string):
    string = string.upper()
    morse = ''
    for letter in string:
        if letter != ' ':
            morse += MORSE_MAPPING[letter] + ' '
        else:
            morse += ' '
            
    return morse

def morse_to_string(morse):
    morse += ' '
    text = ''
    letter = ''
    for char in morse:
        if char != ' ':
            i = 0
            letter += char
        else:
            i += 1
            if i == 2:
                text += ' '
            else:
                text += list(MORSE_MAPPING.keys())[list(MORSE_MAPPING.values()).index(letter)]
                letter = ''
    return text

