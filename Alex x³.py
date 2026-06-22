import tkinter as tk
from tkinter import messagebox


class SquareCalculator(tk.Tk):
    """A simple Tkinter calculator that squares a number."""

    def __init__(self):
        super().__init__()
        self.title("Square Calculator")
        self.geometry("4000x2000")
        self._build_ui()

    def _build_ui(self):
        tk.Label(
            self,
            text="Square Calculator",
            font=("Times New Roman", 16, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(
            self,
            text="Base Number:"
        ).grid(row=1, column=0, sticky="e", padx=10, pady=5)

        self.base_var = tk.StringVar()
        tk.Entry(
            self,
            textvariable=self.base_var,
            width=15
        ).grid(row=1, column=1, padx=10, pady=5)

        tk.Button(
            self,
            text="Calculate",
            command=self._calculate_square,
            width=12
        ).grid(row=2, column=0, columnspan=2, pady=10)

        self.result_var = tk.StringVar(value="Result: ")
        tk.Label(
            self,
            textvariable=self.result_var,
            font=("Times New Roman", 12)
        ).grid(row=3, column=0, columnspan=2, pady=10)

    def _calculate_square(self):
        try:
            base = float(self.base_var.get())

            result = base ** 2
            self.result_var.set(f"Result: {result:g}")

        except ValueError:
            self.result_var.set("Result: Error")
            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid number only."
            )


if __name__ == "__main__":
    SquareCalculator().mainloop()