import tkinter as tk
from tkinter import messagebox

class KBCGame:
    def __init__(self, root):
        self.root = root
        self.root.title("KBC Game for Kids")
        
        self.questions = [
            {
                "question": "Which animal says 'quack, quack'?",
                "options": [
                    "Dog",
                    "Cat",
                    "Duck",
                    "Lion"
                ],
                "correct_option": 2
            },
            {
                "question": "What color is the sky on a sunny day?",
                "options": [
                    "Green",
                    "Blue",
                    "Red",
                    "Yellow"
                ],
                "correct_option": 1
            },
            # Add more questions here...
        ]
        
        self.current_question = 0
        self.score = 0
        
        self.question_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.question_label.pack(pady=10)
        
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Helvetica", 12), command=lambda idx=i: self.check_answer(idx))
            button.pack(pady=5)
            self.option_buttons.append(button)
        
        self.next_button = tk.Button(root, text="Next Question", font=("Helvetica", 12), command=self.next_question)
        self.next_button.pack(pady=10)
        
        self.update_question()

    def update_question(self):
        question_data = self.questions[self.current_question]
        self.question_label.config(text=question_data["question"])
        
        for i in range(4):
            self.option_buttons[i].config(text=question_data["options"][i])
        
    def check_answer(self, selected_option):
        question_data = self.questions[self.current_question]
        if selected_option == question_data["correct_option"]:
            self.score += 10
            messagebox.showinfo("Correct", "Correct answer! You've won 10 points.")
        else:
            messagebox.showerror("Incorrect", "Sorry, that's the wrong answer.")
        
        self.next_question()
        
    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.update_question()
        else:
            messagebox.showinfo("Game Over", f"Your total score is {self.score}")
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = KBCGame(root)
    root.mainloop()
