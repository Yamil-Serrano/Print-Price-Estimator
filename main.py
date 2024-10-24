import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import sys

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Function to calculate the total cost of a 3D print
def calculate_price():
    # Get values entered by the user
    filament_price = float(entry_filament_price.get())
    filament_used = float(entry_filament_used.get())
    hours = float(entry_hours.get())
    minutes = float(entry_minutes.get())
    electricity_price = float(entry_electricity_price.get())
    printer_consumption = float(entry_printer_consumption.get())
    failure_rate = float(entry_failure_rate.get()) / 100

    total_time_hours = hours + (minutes / 60)
    filament_cost = (filament_price / 1000) * filament_used
    consumption_kwh = printer_consumption / 1000
    energy_cost = consumption_kwh * total_time_hours * electricity_price
    total_cost = filament_cost + energy_cost
    total_cost_with_failure = total_cost + (total_cost * failure_rate)

    label_result.config(text=f"Print cost: ${total_cost_with_failure:.2f}", font=('Helvetica', 14, 'bold'))

# Create the main window
window = tk.Tk()
window.iconbitmap(resource_path("resources/money.ico"))
window.title("Print Price Estimator")
window.geometry("700x350")
window.resizable(False, False)

# Create input frame
input_frame = ttk.LabelFrame(window, text="Input Parameters", padding="10")
input_frame.grid(column=0, row=0, padx=10, pady=5, sticky='nsew')

# Load icons with resource path
icon_filament_price = ImageTk.PhotoImage(Image.open(resource_path("resources/3d-printing-filament.png")).resize((16, 16)))
icon_filament_used = ImageTk.PhotoImage(Image.open(resource_path("resources/3d-printing-filament.png")).resize((16, 16)))
icon_hours = ImageTk.PhotoImage(Image.open(resource_path("resources/clock.png")).resize((16, 16)))
icon_minutes = ImageTk.PhotoImage(Image.open(resource_path("resources/clock.png")).resize((16, 16)))
icon_electricity_price = ImageTk.PhotoImage(Image.open(resource_path("resources/power.png")).resize((16, 16)))
icon_printer_consumption = ImageTk.PhotoImage(Image.open(resource_path("resources/power.png")).resize((16, 16)))
icon_failure_rate = ImageTk.PhotoImage(Image.open(resource_path("resources/warning.png")).resize((16, 16)))

# Input fields
ttk.Label(input_frame, image=icon_filament_price).grid(column=0, row=0, padx=5, pady=5, sticky='e')
ttk.Label(input_frame, text="Filament price ($/kg):").grid(column=1, row=0, padx=5, pady=5, sticky='w')
entry_filament_price = ttk.Entry(input_frame)
entry_filament_price.grid(column=2, row=0, padx=5, pady=5)

ttk.Label(input_frame, image=icon_filament_used).grid(column=0, row=1, padx=5, pady=5, sticky='e')
ttk.Label(input_frame, text="Filament used (g):").grid(column=1, row=1, padx=5, pady=5, sticky='w')
entry_filament_used = ttk.Entry(input_frame)
entry_filament_used.grid(column=2, row=1, padx=5, pady=5)

ttk.Label(input_frame, image=icon_hours).grid(column=0, row=2, padx=5, pady=5, sticky='e')
ttk.Label(input_frame, text="Print time (hours):").grid(column=1, row=2, padx=5, pady=5, sticky='w')
entry_hours = ttk.Entry(input_frame)
entry_hours.grid(column=2, row=2, padx=5, pady=5)

ttk.Label(input_frame, image=icon_minutes).grid(column=0, row=3, padx=5, pady=5, sticky='e')
ttk.Label(input_frame, text="Print time (minutes):").grid(column=1, row=3, padx=5, pady=5, sticky='w')
entry_minutes = ttk.Entry(input_frame)
entry_minutes.grid(column=2, row=3, padx=5, pady=5)

ttk.Label(input_frame, image=icon_electricity_price).grid(column=0, row=4, padx=5, pady=5, sticky='e')
ttk.Label(input_frame, text="Electricity price (¢/kWh):").grid(column=1, row=4, padx=5, pady=5, sticky='w')
entry_electricity_price = ttk.Entry(input_frame)
entry_electricity_price.grid(column=2, row=4, padx=5, pady=5)

ttk.Label(input_frame, image=icon_printer_consumption).grid(column=0, row=5, padx=5, pady=5, sticky='e')
ttk.Label(input_frame, text="Printer consumption (W):").grid(column=1, row=5, padx=5, pady=5, sticky='w')
entry_printer_consumption = ttk.Entry(input_frame)
entry_printer_consumption.grid(column=2, row=5, padx=5, pady=5)

ttk.Label(input_frame, image=icon_failure_rate).grid(column=0, row=6, padx=5, pady=5, sticky='e')
ttk.Label(input_frame, text="Failure rate (%):").grid(column=1, row=6, padx=5, pady=5, sticky='w')
entry_failure_rate = ttk.Entry(input_frame)
entry_failure_rate.grid(column=2, row=6, padx=5, pady=5)

# Calculate button
calculate_button = ttk.Button(input_frame, text="Calculate Price", command=calculate_price)
calculate_button.grid(column=0, row=7, columnspan=3, padx=5, pady=30)

# Right frame
right_frame = ttk.Frame(window)
right_frame.grid(column=1, row=0, padx=10, pady=5, sticky='nsew')

# Load and display 3D printer image
image = Image.open(resource_path("resources/3d-printer.png"))
image = image.resize((250, 250))
photo = ImageTk.PhotoImage(image)

label_image = ttk.Label(right_frame, image=photo)
label_image.image = photo
label_image.pack(pady=10)

# Result label
label_result = ttk.Label(right_frame, text="Print cost: $0.00", font=('Helvetica', 14, 'bold'))
label_result.pack(pady=10)

# Grid configuration
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)

if __name__ == '__main__':
    window.mainloop()
