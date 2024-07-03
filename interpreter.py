import tkinter as tk
from tkinter import messagebox

# Padrão Interpreter

class Expression:
    def interpret(self):
        pass

class Number(Expression):
    def __init__(self, value):
        self.value = int(value)

    def interpret(self):
        return self.value

class Add(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()

class Subtract(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()

class Multiply(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() * self.right.interpret()

class Divide(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() / self.right.interpret()

class Parser:
    def parse(self, expression):
        tokens = expression.split()
        output_queue = []
        operator_stack = []

        precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2
        }

        for token in tokens:
            if token.isdigit():
                output_queue.append(Number(token))
            elif token in precedence:
                while (operator_stack and
                       operator_stack[-1] in precedence and
                       precedence[operator_stack[-1]] >= precedence[token]):
                    self.pop_operator_to_output(operator_stack, output_queue)
                operator_stack.append(token)
            else:
                raise ValueError(f"Unknown token: {token}")

        while operator_stack:
            self.pop_operator_to_output(operator_stack, output_queue)

        if len(output_queue) != 1:
            raise ValueError("Invalid expression")

        return output_queue.pop()

    def pop_operator_to_output(self, operator_stack, output_queue):
        operator = operator_stack.pop()
        right = output_queue.pop()
        left = output_queue.pop()
        if operator == '+':
            output_queue.append(Add(left, right))
        elif operator == '-':
            output_queue.append(Subtract(left, right))
        elif operator == '*':
            output_queue.append(Multiply(left, right))
        elif operator == '/':
            output_queue.append(Divide(left, right))

# Integração com Tkinter

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interpreter Pattern Example")
        self.geometry("400x200")

        self.create_widgets()

    def create_widgets(self):
        self.expression_label = tk.Label(self, text="Enter expression:")
        self.expression_label.pack(pady=10)

        self.expression_entry = tk.Entry(self, width=40)
        self.expression_entry.pack(pady=10)

        self.evaluate_button = tk.Button(self, text="Evaluate", command=self.evaluate_expression)
        self.evaluate_button.pack(pady=10)

        self.result_label = tk.Label(self, text="Result:")
        self.result_label.pack(pady=10)

    def evaluate_expression(self):
        expression = self.expression_entry.get()
        parser = Parser()

        try:
            parsed_expression = parser.parse(expression)
            result = parsed_expression.interpret()
            self.result_label.config(text=f"Result: {result}")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid expression: {e}")

if __name__ == "__main__":
    app = Application()
    app.mainloop()