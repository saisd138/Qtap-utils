import nfc

def on_connect(tag):
    uid = tag.identifier.hex()
    print(f'UID: {uid}')
    return True  # Set the flag to exit the loop

clf = nfc.ContactlessFrontend('tty:S0')  # Use 'tty:AMA0' or other port based on your configuration

try:
    card_read = False  # Flag to indicate whether a card has been read

    # Use an event-driven approach
    clf.connect(rdwr={'on-connect': on_connect})

except KeyboardInterrupt:
    pass  # Handle Ctrl+C gracefully

finally:
    clf.close()
