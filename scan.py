import nfc

def on_connect(tag):
    uid = tag.identifier.hex()
    print(f'UID: {uid}')
    return True  # Set the flag to exit the loop

clf = nfc.ContactlessFrontend('tty:AMA0')  # Use 'tty:AMA0' or other port based on your configuration
#bluetooth need to be disconnected using following command in config.txt
# dtoverlay=disable-bt

try:
    card_read = False  # Flag to indicate whether a card has been read

    # Use an event-driven approach
    clf.connect(rdwr={'on-connect': on_connect})

except KeyboardInterrupt:
    pass  # Handle Ctrl+C gracefully

finally:
    clf.close()
