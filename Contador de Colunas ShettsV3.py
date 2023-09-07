import tkinter as tk

class ColumnCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("")
        self.root.attributes("-topmost", True)

        self.label = tk.Label(root, text="Digite a primeira e a segunda letra:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()
        self.entry.bind("<Return>", self.count_columns_enter)
        self.entry.bind("<Escape>", self.clear_entry)
        self.entry.bind("0", self.clear_entry)

        root.attributes("-alpha", 0.7)
        self.entry.configure(bg='white')

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        self.count_button = tk.Button(root, text="Contar Colunas", command=self.count_columns)
        self.count_button.pack()

        # Detecta quando a janela entra em modo de tela cheia e minimiza
        self.root.bind("<Configure>", self.check_fullscreen)

    def check_fullscreen(self, event):
        if self.root.state() == 'zoomed':
            self.root.iconify()

    def count_columns(self):
        letters = self.entry.get().upper()
        self.calculate_and_display_result(letters)

    def count_columns_enter(self, event):
        letters = self.entry.get().upper()
        self.calculate_and_display_result(letters)

    def clear_entry(self, event):
        self.entry.delete(0, tk.END)

    def calculate_and_display_result(self, letters):
        if len(letters) != 2 or not letters.isalpha():
            self.result_label.config(text="Digite duas letras válidas.")
            return

        first_letter = ord(letters[0])
        second_letter = ord(letters[1])

        if first_letter > second_letter:
            first_letter, second_letter = second_letter, first_letter

        column_count = second_letter - first_letter + 1
        self.result_label.config(text=f"Total de colunas: {column_count}")
    
if __name__ == "__main__":
    root = tk.Tk()
   
    app = ColumnCounterApp(root)
    root.mainloop()
