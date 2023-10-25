import pyperclip
import webbrowser
import time

def open_google_maps(address): #create a function that takes an address argument
    base_url= "https://www.google.com/maps/dir/?api=1&destination="
    #This line sets the base url for Google Maps directions. The 'destination' query parameter will
    #be appended to this base url
    destination = address.replace(" ", "+")
    #this line replaces spaces in the address with '+' character to encode the address for use in a
    #URL
    url = base_url + destination
    #this line constructs the full URL by concatenating the base URL and the encoded destination
    #address
    webbrowser.open(url, new =2)
    #this line intializes a variable to keep track of the previous clipboard content

previous_clipboard_content = None

while True:
    #get the clipbaord conetent
    clipboard_content = pyperclip.paste()
    #starts an infinite loop that will continuously check for clipboard changes
    #this line also gets the current copied text
    if clipboard_content != previous_clipboard_content:
    #this line checks if the clipboard content has changed since the last iteration
        print("New address copied:", clipboard_content)
    #this line prints a message indicating a new address has been copied
        open_google_maps(clipboard_content)
    #this line calls the google maps function with the new address as an argument which opens
    #Google Maps
        previous_clipboard_content = previous_clipboard_content
    #this line updates the 'previous_clipboard_content' variable to the current clipboard content
    time.sleep(15)
    #this line pauses the program for 15 seconds before checking the clipboard again... hopefully
    #helps prevent the program from excessive CPU resources

    #typically cntrl-c or some shortcut can be used to stop it manually