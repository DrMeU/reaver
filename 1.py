Sure thing. I'll create a simple GUI for the Reaver-WPS-Fork-T6X program using Python and Tkinter.

Here's the code:
```python
import tkinter as tk
import subprocess

def start_reaver():
    interface = interface_entry.get()
    channel = channel_entry.get()
    bssid = bssid_entry.get()
    crack = crack_entry.get()
    cmd = f'reaver -i {interface} -c {channel} -b {bssid} -a -N --crack {crack}'
    subprocess.run(cmd, shell=True)

root = tk.Tk()
root.title('Reaver-WPS-Fork-T6X GUI')

interface_label = tk.Label(root, text='Interface:')
interface_label.grid(row=0, column=0)
interface_entry = tk.Entry(root)
interface_entry.grid(row=0, column=1)

channel_label = tk.Label(root, text='Channel:')
channel_label.grid(row=1, column=0)
channel_entry = tk.Entry(root, width=5)
channel_entry.grid(row=1, column=1)

bssid_label = tk.Label(root, text='BSSID:')
bssid_label.grid(row=2, column=0)
bssid_entry = tk.Entry(root, width=17)
bssid_entry.grid(row=2, column=1)

crack_label = tk.Label(root, text='Crack method:')
crack_label.grid(row=3, column=0)
crack_entry = tk.Entry(root, width=32)
crack_entry.grid(row=3, column=1)

start_button = tk.Button(root, text='Start Reaver', command=start_reaver)
start_button.grid(row=4, column=0, columnspan=2)

root.mainloop()
```
This GUI allows you to specify the interface, channel, BSSID, and crack method for the Reaver-WPS-Fork-T6X program. When the "Start Reaver" button is clicked, it calls the `start_reaver()` function, which constructs a command using the entered information and executes it using the `subprocess.run()` function.

Note that this GUI is just a basic example to get you started. You can further customize it to fit your needs.
