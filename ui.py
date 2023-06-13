import tkinter as tk
from graph import Graph

class MetroTravelUI:
    def __init__(self, graph, airport_codes):
        self.graph = graph
        self.airport_codes = airport_codes
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

        if origin not in self.airport_codes or destination not in self.airport_codes:
            self.result_label.config(text="Origen o destino no válido.")
            return

        src_idx = self.airport_codes.index(origin)
        dest_idx = self.airport_codes.index(destination)

        cost, path = self.graph.find_route(src_idx, dest_idx, has_visa)
        if cost == float('inf'):
            self.result_label.config(text="No se encontró una ruta válida.")
        else:
            path = [self.airport_codes[i] for i in path]
            self.result_label.config(text=f"Ruta: {' -> '.join(path)}\nCosto: ${cost}")
