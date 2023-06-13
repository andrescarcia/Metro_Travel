import tkinter as tk
from graph import Graph

class MetroTravelUI:
    def __init__(self, graph):
        self.graph = graph
        self.root = tk.Tk()
        self.root.title("Metro Travel")

        self.origin_label = tk.Label(self.root, text="Origen:")
        self.origin_label.grid(row=0, column=0)
        self.origin_entry = tk.Entry(self.root)
        self.origin_entry.grid(row=0, column=1)

        self.destination_label = tk.Label(self.root, text="Destino:")
        self.destination_label.grid(row=1, column=0)
        self.destination_entry = tk.Entry(self.root)
        self.destination_entry.grid(row=1, column=1)

        self.visa_var = tk.BooleanVar()
        self.visa_check = tk.Checkbutton(self.root, text="Tiene visa", variable=self.visa_var)
        self.visa_check.grid(row=2, column=0, columnspan=2)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=3, column=0, columnspan=2)

        self.calculate_button = tk.Button(self.root, text="Calcular ruta", command=self.calculate_route)
        self.calculate_button.grid(row=4, column=0, columnspan=2)

    def run(self):
        self.root.mainloop()

    def calculate_route(self):
        origin = self.origin_entry.get().strip().upper()
        destination = self.destination_entry.get().strip().upper()
        has_visa = self.visa_var.get()

        cost, path = self.graph.find_route(origin, destination, has_visa)
        if cost is None:
            self.result_label.config(text="No se encontró una ruta válida.")
        else:
            self.result_label.config(text=f"Ruta: {' -> '.join(path)}\nCosto: ${cost}")
