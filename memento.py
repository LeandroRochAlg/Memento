import tkinter as tk
from tkinter import scrolledtext

class Memento:
    def __init__(self, state):
        self.state = state

class TextEditor:
    def __init__(self, text_widget):
        self.text_widget = text_widget  # instância da tela de texto do tkinter
        self.history = []
        self.future = []

    def type_text(self, text):
        self.text_widget.insert(tk.END, text)

    def save(self):
        state = self.text_widget.get("1.0", tk.END) # obtém o conteúdo do widget
        self.history.append(Memento(state))
        self.future.clear()

    def undo(self):
        if self.history:
            self.future.append(Memento(self.text_widget.get("1.0", tk.END)))
            memento = self.history.pop()

            # Atualiza o conteúdo do widget
            self.text_widget.delete("1.0", tk.END)
            self.text_widget.insert(tk.END, memento.state)

    def redo(self):
        if self.future:
            self.history.append(Memento(self.text_widget.get("1.0", tk.END)))
            memento = self.future.pop()

            # Atualiza o conteúdo do widget
            self.text_widget.delete("1.0", tk.END)
            self.text_widget.insert(tk.END, memento.state)

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Editor de Texto com Memento")
        self.geometry("600x400")

        self.text_editor = TextEditor(self.create_text_widget())
        self.create_buttons()

    def create_text_widget(self):
        text_widget = scrolledtext.ScrolledText(self, wrap=tk.WORD)
        text_widget.pack(expand=True, fill=tk.BOTH)
        return text_widget

    def create_buttons(self):
        button_frame = tk.Frame(self)
        button_frame.pack(fill=tk.X, side=tk.BOTTOM)

        btn_undo = tk.Button(button_frame, text="Undo", command=self.text_editor.undo)
        btn_undo.pack(side=tk.LEFT)

        btn_redo = tk.Button(button_frame, text="Redo", command=self.text_editor.redo)
        btn_redo.pack(side=tk.LEFT)

        btn_save = tk.Button(button_frame, text="Save", command=self.text_editor.save)
        btn_save.pack(side=tk.LEFT)

        btn_type = tk.Button(button_frame, text="Type Sample Text", command=lambda: self.type_sample_text())
        btn_type.pack(side=tk.LEFT)

    def type_sample_text(self):
        self.text_editor.type_text("Este é um exemplo de texto.\n")
        self.text_editor.save()

if __name__ == "__main__":
    app = Application()
    app.mainloop()