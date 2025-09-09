import tkinter as tk

def calculate():
    try:
        amount = int(entry.get())
        result_text = ""
        denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]

        for d in denominations:
            count = amount // d 
            amount %= d
            if count > 0:
                result_text += f"{d} x {count}\n"
        
        result_label.config(text=result_text)
    except:
        result_label.config(text="Enter a valid number!")

root = tk.Tk()
root.title("Denomination Calculator")

tk.Label(root, text="Enter Amount:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Calculate", command=calculate).pack(pady=5)

result_label = tk.Label(root, text="", justify="left")
result_label.pack(pady=10)

root.mainloop()