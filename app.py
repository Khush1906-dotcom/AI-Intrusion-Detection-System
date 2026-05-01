import pickle
import numpy as np
import tkinter as tk
from tkinter import messagebox

# Load model
model = pickle.load(open("model.pkl", "rb"))

def predict():
    try:
        duration = float(entry1.get())
        src_bytes = float(entry2.get())
        dst_bytes = float(entry3.get())
        count = float(entry4.get())
        srv_count = float(entry5.get())

        sample = [0]*41
        sample[0] = duration
        sample[4] = src_bytes
        sample[5] = dst_bytes
        sample[22] = count
        sample[23] = srv_count

        sample = np.array([sample])
        prediction = model.predict(sample)

        if prediction[0] == 0:
            result.set("NORMAL TRAFFIC")
        else:
            result.set("ATTACK DETECTED")

    except:
        messagebox.showerror("Error", "Enter valid numbers")

# GUI
root = tk.Tk()
root.title("AI Intrusion Detection System")

tk.Label(root, text="Duration").pack()
entry1 = tk.Entry(root); entry1.pack()

tk.Label(root, text="Source Bytes").pack()
entry2 = tk.Entry(root); entry2.pack()

tk.Label(root, text="Destination Bytes").pack()
entry3 = tk.Entry(root); entry3.pack()

tk.Label(root, text="Connection Count").pack()
entry4 = tk.Entry(root); entry4.pack()

tk.Label(root, text="Service Count").pack()
entry5 = tk.Entry(root); entry5.pack()

tk.Button(root, text="Check", command=predict).pack()

result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 14)).pack()

root.mainloop()