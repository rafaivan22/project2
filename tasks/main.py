import tkinter as tk
from tkinter import messagebox
import random
from fractions import Fraction

class FractionTrainerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Генератор задач с дробями для тренировки")
        self.master.geometry("400x400")

        self.level = tk.StringVar(value="easy")  # Уровень сложности (по умолчанию - легкий)
        self.score = 0
        self.attempts = 0

        # Инструкция
        self.instruction_label = tk.Label(self.master, text="Решите задачу с дробями", font=("Arial", 14))
        self.instruction_label.pack(pady=10)

        # Виджет для выбора уровня сложности
        self.level_label = tk.Label(self.master, text="Выберите уровень сложности:", font=("Arial", 12))
        self.level_label.pack(pady=5)

        self.easy_button = tk.Radiobutton(self.master, text="Легкий", variable=self.level, value="easy")
        self.easy_button.pack()
        self.medium_button = tk.Radiobutton(self.master, text="Средний", variable=self.level, value="medium")
        self.medium_button.pack()
        self.hard_button = tk.Radiobutton(self.master, text="Сложный", variable=self.level, value="hard")
        self.hard_button.pack()

        # Поле для ввода ответа
        self.answer_label = tk.Label(self.master, text="Ваш ответ:", font=("Arial", 12))
        self.answer_label.pack(pady=5)
        self.answer_entry = tk.Entry(self.master, font=("Arial", 14))
        self.answer_entry.pack(pady=5)

        # Кнопка для проверки ответа
        self.check_button = tk.Button(self.master, text="Проверить", command=self.check_answer, font=("Arial", 14))
        self.check_button.pack(pady=10)

        # Статистика
        self.stats_label = tk.Label(self.master, text="Правильных ответов: 0/0", font=("Arial", 12))
        self.stats_label.pack(pady=10)

        # Генерация начальной задачи
        self.generate_problem()

    def generate_problem(self):
        """Генерация задачи на дроби в зависимости от уровня сложности."""
        if self.level.get() == "easy":
            self.numerator1 = random.randint(1, 10)
            self.denominator1 = random.randint(2, 10)
            self.numerator2 = random.randint(1, 10)
            self.denominator2 = random.randint(2, 10)
            self.operation = random.choice(["+", "-"])
        elif self.level.get() == "medium":
            self.numerator1 = random.randint(1, 15)
            self.denominator1 = random.randint(2, 15)
            self.numerator2 = random.randint(1, 15)
            self.denominator2 = random.randint(2, 15)
            self.operation = random.choice(["+", "-", "*", "/"])
        else:
            self.numerator1 = random.randint(1, 25)
            self.denominator1 = random.randint(2, 25)
            self.numerator2 = random.randint(1, 25)
            self.denominator2 = random.randint(2, 25)
            self.operation = random.choice(["+", "-", "*", "/"])

        # Преобразуем дроби в тип Fraction для точных расчетов
        self.fraction1 = Fraction(self.numerator1, self.denominator1)
        self.fraction2 = Fraction(self.numerator2, self.denominator2)

        # Создаем строку задачи для отображения
        if self.operation == "+":
            self.correct_answer = self.fraction1 + self.fraction2
            self.problem = f"{self.fraction1} + {self.fraction2} = ?"
        elif self.operation == "-":
            self.correct_answer = self.fraction1 - self.fraction2
            self.problem = f"{self.fraction1} - {self.fraction2} = ?"
        elif self.operation == "*":
            self.correct_answer = self.fraction1 * self.fraction2
            self.problem = f"{self.fraction1} * {self.fraction2} = ?"
        else:
            self.correct_answer = self.fraction1 / self.fraction2
            self.problem = f"{self.fraction1} / {self.fraction2} = ?"

        # Обновляем текст задачи
        self.instruction_label.config(text=self.problem)

    def check_answer(self):
        """Проверка ответа пользователя."""
        try:
            user_answer = Fraction(self.answer_entry.get())  # Преобразуем введенное значение в дробь
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите дробь в правильном формате.")
            return

        # Проверка правильности ответа
        self.attempts += 1
        if user_answer == self.correct_answer:
            self.score += 1
            messagebox.showinfo("Правильно!", "Ответ верный!")
        else:
            messagebox.showinfo("Неправильно", f"Правильный ответ: {self.correct_answer}")

        # Обновляем статистику
        self.stats_label.config(text=f"Правильных ответов: {self.score}/{self.attempts}")

        # Генерация новой задачи
        self.answer_entry.delete(0, tk.END)
        self.generate_problem()

if __name__ == "__main__":
    root = tk.Tk()
    app = FractionTrainerApp(root)
    root.mainloop()
