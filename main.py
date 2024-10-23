import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Function to calculate the total cost of a 3D print
def calculate_price():
    # Get values entered by the user
    filament_price = float(entry_filament_price.get())  # Filament price per kilogram
    filament_used = float(entry_filament_used.get())    # Filament used in grams
    hours = float(entry_hours.get())                    # Printing time in hours
    minutes = float(entry_minutes.get())                # Printing time in minutes
    electricity_price = float(entry_electricity_price.get())  # Electricity price per kWh
    printer_consumption = float(entry_printer_consumption.get())  # Printer consumption in watts
    failure_rate = float(entry_failure_rate.get()) / 100  # Failure rate as a percentage

    # Convert minutes to hours
    total_time_hours = hours + (minutes / 60)

    # Calculate filament cost
    filament_cost = (filament_price / 1000) * filament_used  # Filament cost in dollars

    # Calculate energy cost based on printer consumption and time
    consumption_kwh = printer_consumption / 1000  # Convert watts to kWh
    energy_cost = consumption_kwh * total_time_hours * electricity_price  # Energy cost in dollars

    # Calculate total print cost
    total_cost = filament_cost + energy_cost

    # Add failure rate to account for potential failed prints
    total_cost_with_failure = total_cost + (total_cost * failure_rate)

    # Display the result in the result label
    label_result.config(text=f"Print cost: ${total_cost_with_failure:.2f}", font=('Helvetica', 14, 'bold'))

# Create the main window for the application
window = tk.Tk()
window.iconbitmap("resources/money.ico")  # Set the window icon
window.title("Print Price Estimator")  # Set the window title
window.geometry("700x350")  # Set the window size
window.resizable(False, False)  # Disable window resizing

# Create a frame for the input fields
input_frame = ttk.LabelFrame(window, text="Input Parameters", padding="10")  # Label frame to organize inputs
input_frame.grid(column=0, row=0, padx=10, pady=5, sticky='nsew')

# Load icons for each label (resized to 16x16 pixels)
icon_filament_price = ImageTk.PhotoImage(Image.open("resources/3d-printing-filament.png").resize((16, 16)))
icon_filament_used = ImageTk.PhotoImage(Image.open("resources/3d-printing-filament.png").resize((16, 16)))
icon_hours = ImageTk.PhotoImage(Image.open("resources/clock.png").resize((16, 16)))
icon_minutes = ImageTk.PhotoImage(Image.open("resources/clock.png").resize((16, 16)))
icon_electricity_price = ImageTk.PhotoImage(Image.open("resources/power.png").resize((16, 16)))
icon_printer_consumption = ImageTk.PhotoImage(Image.open("resources/power.png").resize((16, 16)))
icon_failure_rate = ImageTk.PhotoImage(Image.open("resources/warning.png").resize((16, 16)))

# Labels, entry fields, and icons for each input parameter
ttk.Label(input_frame, image=icon_filament_price).grid(column=0, row=0, padx=5, pady=5, sticky='e')
ttk.Label(input_frame, text="Filament price ($/kg):").grid(column=1, row=0, padx=5, pady=5, sticky='w')
entry_filament_price = ttk.Entry(input_frame)  # Entry field for filament price
entry_filament_price.grid(column=2, row=0, padx=5, pady=5)

ttk.Label(input_frame, image=icon_filament_used).grid(column=0, row=1, padx=5, pady=5, sticky='e')
ttk.Label(input_frame, text="Filament used (g):").grid(column=1, row=1, padx=5, pady=5, sticky='w')
entry_filament_used = ttk.Entry(input_frame)  # Entry field for filament used
entry_filament_used.grid(column=2, row=1, padx=5, pady=5)

ttk.Label(input_frame, image=icon_hours).grid(column=0, row=2, padx=5, pady=5, sticky='e')
ttk.Label(input_frame, text="Print time (hours):").grid(column=1, row=2, padx=5, pady=5, sticky='w')
entry_hours = ttk.Entry(input_frame)  # Entry field for print hours
entry_hours.grid(column=2, row=2, padx=5, pady=5)

ttk.Label(input_frame, image=icon_minutes).grid(column=0, row=3, padx=5, pady=5, sticky='e')
ttk.Label(input_frame, text="Print time (minutes):").grid(column=1, row=3, padx=5, pady=5, sticky='w')
entry_minutes = ttk.Entry(input_frame)  # Entry field for print minutes
entry_minutes.grid(column=2, row=3, padx=5, pady=5)

ttk.Label(input_frame, image=icon_electricity_price).grid(column=0, row=4, padx=5, pady=5, sticky='e')
ttk.Label(input_frame, text="Electricity price ($/kWh):").grid(column=1, row=4, padx=5, pady=5, sticky='w')
entry_electricity_price = ttk.Entry(input_frame)  # Entry field for electricity price
entry_electricity_price.grid(column=2, row=4, padx=5, pady=5)

ttk.Label(input_frame, image=icon_printer_consumption).grid(column=0, row=5, padx=5, pady=5, sticky='e')
ttk.Label(input_frame, text="Printer consumption (W):").grid(column=1, row=5, padx=5, pady=5, sticky='w')
entry_printer_consumption = ttk.Entry(input_frame)  # Entry field for printer power consumption
entry_printer_consumption.grid(column=2, row=5, padx=5, pady=5)

ttk.Label(input_frame, image=icon_failure_rate).grid(column=0, row=6, padx=5, pady=5, sticky='e')
ttk.Label(input_frame, text="Failure rate (%):").grid(column=1, row=6, padx=5, pady=5, sticky='w')
entry_failure_rate = ttk.Entry(input_frame)  # Entry field for failure rate
entry_failure_rate.grid(column=2, row=6, padx=5, pady=5)

# Button to trigger the price calculation
calculate_button = ttk.Button(input_frame, text="Calculate Price", command=calculate_price)
calculate_button.grid(column=0, row=7, columnspan=3, padx=5, pady=30)

# Create a frame for the right side content (to display image and result)
right_frame = ttk.Frame(window)
right_frame.grid(column=1, row=0, padx=10, pady=5, sticky='nsew')

# Load and display the 3D printer image on the right side
image = Image.open("resources/3d-printer.png")
image = image.resize((250, 250))  # Resize the image to fit the window
photo = ImageTk.PhotoImage(image)

# Create a label to hold the 3D printer image
label_image = ttk.Label(right_frame, image=photo)
label_image.image = photo  # Keep a reference to avoid garbage collection
label_image.pack(pady=10)

# Label to display the result (cost of the print)
label_result = ttk.Label(right_frame, text="Print cost: $0.00", font=('Helvetica', 14, 'bold'))
label_result.pack(pady=10)

# Configure grid weights to allow for layout flexibility
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)

# Run the application
window.mainloop()
