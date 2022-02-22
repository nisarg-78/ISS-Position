import requests
import json
import time
from tkinter import *

root = Tk()
root.resizable(False,False)
root.title('ISS Position V.1')

#GLOBAL VARIABLES

current_time = ''
longitude = ''
latitide = ''
message = ''

#FUNCTIONS

def get_pos():
    result = requests.get('http://api.open-notify.org/iss-now.json')
    result_dict = result.json()

    current_time.config(text = str(time.ctime(int(result_dict['timestamp']))))
    longitude.config(text = str(result_dict['iss_position']['latitude']))
    latitude.config(text = str(result_dict['iss_position']['longitude']))
    message.config(text = str(result_dict['message']).upper())


#WIDGETS

_current_time = Label(root, text = 'Time: ',font=('Helvetica', 20, ))
_current_time.grid(row=0, column=0,)
_longitude = Label(root, text = 'Longitude: ',font=('Helvetica', 20, ))
_longitude.grid(row=1, column=0,)
_latitude = Label(root, text = 'Latitude: ',font=('Helvetica', 20, ))
_latitude.grid(row=2, column=0,)
_message = Label(root, text = 'Message: ',font=('Helvetica', 20, ))
_message.grid(row=3, column=0,)

current_time = Label(root, text = '',font=('Helvetica', 20, ))
current_time.grid(row=0, column=1,)
longitude = Label(root, text = '',font=('Helvetica', 20, ))
longitude.grid(row=1, column=1,)
latitude = Label(root, text = '',font=('Helvetica', 20, ))
latitude.grid(row=2, column=1,)
message = Label(root, text = '',font=('Helvetica', 20, ))
message.grid(row=3, column=1,)

button = Button(root,command=get_pos, text='UPDATE POSITION',font=('Century 12',15), padx=20, pady=20)
button.grid(row=4,column=0,columnspan=3)

get_pos()
root.mainloop()

