import tkinter as tk

def add_topic():
    topic = entry_field.get()
    listbox.insert(tk.END, topic)  # This assumes your topic is entered as a string.

root = tk.Tk()
root.title("Topic Manager")

frame = tk.Frame(root)
frame.pack()

entry_field = tk.Entry(frame, width=50)
entry_field.pack()

listbox = tk.Listbox(frame, height=10, width=50)
listbox.pack()

button = tk.Button(frame, text="Add Topic", command=add_topic)  # This assumes your topic is entered as a string.
button.pack()

root.mainloop()
