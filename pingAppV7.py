from tkinter import *
from tkinter import ttk
import os
import tkinter as tki
import subprocess


root = Tk()
root.title("Device Reachability App")
root.geometry("450x280")
root.iconbitmap('C:/Users/admin/Documents/My-Python-Projects/python.ico')
mainframe = ttk.Frame(root, borderwidth=20, relief="sunken")
mainframe.grid(column=1, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(2, weight=2)
mainframe.rowconfigure(2, weight=1)

ipadd = StringVar()

# Create Run Test Function
def submit():
    ipadd = ipadd_entry.get("1.0",END)
    results_file = open('iplist.txt', 'w')
    results_file.write((ipadd) + "\n")
   
    iplist = open('iplist.txt', 'r')
    iplist.read()

    results_file = open('results.txt', 'w')
    
    for ip in iplist:
        ip = ip.rstrip('\n') # Removes line break
        show_results = ''
        response = os.popen(f'ping -n 2 {ip}').read()
        if 'Received = 2' in response:
            results_file.write((ip)+' is reachable' + '\n')
        elif 'Received = 0' in response:
            results_file.write(f'{ip} is NOT reachable' + "\n")
        
    show_results = f'Done Testing!'

    ipadd_entry.delete("1.0",END) # Empties text box
    
    results_label = Label(mainframe, text=show_results).grid(column=0, row=3, sticky=W)

# File Open Function
def show_results():
    subprocess.Popen(["notepad.exe", 'results.txt'])    

# Labels and Entry Boxes
ttk.Label(mainframe, text="Enter IP Address(s) or Hostname(s):").grid(column=0, row=0, sticky=W)
ipadd_entry =Text(mainframe, height = 5, width = 50)
ipadd_entry.grid(column=0, row=1, pady=5, sticky=W)

# Buttons
submit_button = Button(mainframe, text = "Run Test", command=submit, bg='green', fg='white').grid(column=0, row=2, columnspan=2, padx=1, pady=10, ipadx=50, ipady=10, sticky=W)
exit_button = Button(mainframe, text = "Exit", command=root.destroy, bg='red', fg='white').grid(column=0, row=3, columnspan=2, padx=1, pady=10, ipadx=30, ipady=10, sticky=E)
results_button = Button(mainframe, text = "Show Results", command=show_results, bg='blue', fg='white').grid(column=0, row=2, columnspan=2, padx=1, pady=10, ipadx=50, ipady=10, sticky=E)

root.mainloop()


# Controlling the number of pings in Linux - example: ping -c 4, will return 4 pings, change if statement to (number of pings) received, ex. '2 received'

# Controlling the number of pings in Windows - example: ping -n 4, will return 4 pings, change the if statement to Received = (number of pings), ex. 'Received = 2'