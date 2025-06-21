import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()

        if from_unit == to_unit:
            result = temp
        elif from_unit == "Celsius":
            result = temp if to_unit == "Celsius" else (temp * 9/5 + 32 if to_unit == "Fahrenheit" else temp + 273.15)
        elif from_unit == "Fahrenheit":
            celsius = (temp - 32) * 5/9
            result = celsius if to_unit == "Celsius" else (temp if to_unit == "Fahrenheit" else celsius + 273.15)
        elif from_unit == "Kelvin":
            celsius = temp - 273.15
            result = celsius if to_unit == "Celsius" else (celsius * 9/5 + 32 if to_unit == "Fahrenheit" else temp)

        label_result.config(text=f"Result: {result:.2f} °{to_unit[0]}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Create main window
window = tk.Tk()
window.title("Temperature Converter")
window.geometry("400x250")
window.configure(bg="#f0f0f0")

# Heading
tk.Label(window, text="Temperature Converter", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

# Input temperature
frame = tk.Frame(window, bg="#f0f0f0")
frame.pack(pady=10)

tk.Label(frame, text="Enter Temperature:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, padx=5)
entry_temp = tk.Entry(frame, font=("Arial", 12))
entry_temp.grid(row=0, column=1, padx=5)

# Dropdowns
units = ["Celsius", "Fahrenheit", "Kelvin"]
tk.Label(frame, text="From:", font=("Arial", 12), bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5)
combo_from = ttk.Combobox(frame, values=units, font=("Arial", 12), state="readonly")
combo_from.set("Celsius")
combo_from.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="To:", font=("Arial", 12), bg="#f0f0f0").grid(row=2, column=0, padx=5, pady=5)
combo_to = ttk.Combobox(frame, values=units, font=("Arial", 12), state="readonly")
combo_to.set("Fahrenheit")
combo_to.grid(row=2, column=1, padx=5, pady=5)

# Convert button
tk.Button(window, text="Convert", command=convert_temperature, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white").pack(pady=10)

# Result display
label_result = tk.Label(window, text="Result: ", font=("Arial", 14), bg="#f0f0f0")
label_result.pack(pady=5)

# Run the application
window.mainloop()
