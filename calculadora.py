import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("400x600")
        
        self.current_input = ""
        
        self.display = tk.Entry(self.root, font=('Arial', 24), borderwidth=2, relief="groove", justify='right')
        self.display.grid(row=0, column=0, columnspan=4, ipady=10)
        
        self.create_buttons()
    
    def create_buttons(self):
        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        row_val = 1
        col_val = 0
        
        for text in button_texts:
            button = tk.Button(self.root, text=text, font=('Arial', 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row_val, column=col_val, sticky='nsew', padx=5, pady=5)
            
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
        
        clear_button = tk.Button(self.root, text='C', font=('Arial', 18), command=self.clear_display)
        clear_button.grid(row=row_val, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)
        
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)
    
    def on_button_click(self, char):
        if char == '=':
            try:
                self.current_input = str(eval(self.current_input))
            except Exception as e:
                self.current_input = "Error"
        else:
            self.current_input += str(char)
        
        self.update_display()
    
    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current_input)
    
    def clear_display(self):
        self.current_input = ""
        self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
