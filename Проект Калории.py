import tkinter as tk
from tkinter import messagebox


def calculate_calories(age, gender, weight, height, activity_level):
    bmr = 0


    if gender.upper() == 'M':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender.upper() == 'F':
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    if activity_level == 1:
        return bmr * 1.2
    elif activity_level == 2:
        return bmr * 1.375
    elif activity_level == 3:
        return bmr * 1.55
    elif activity_level == 4:
        return bmr * 1.725
    elif activity_level == 5:
        return bmr * 1.9
    else:
        return bmr

def show_result(total_calories):
    result_text = (
        f"Необходимое количество калорий для поддержания веса: {total_calories:.2f} ккал.\n"
        f"Рекомендуемое количество калорий для завтрака: {(total_calories * 0.25):.2f} ккал."
    )
    messagebox.showinfo("Результат", result_text)


def submit_button_clicked():
    try:
        age = int(age_entry.get())
        gender = gender_var.get().upper()
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        activity_level = int(activity_level_var.get())

        total_calories = calculate_calories(age, gender, weight, height, activity_level)
        show_result(total_calories)
    except ValueError:
        messagebox.showerror("Ошибка", "Проверьте введенные значения.")


root = tk.Tk()
root.title("Расчёт калорий")


root.geometry("400x500")
root.config(bg="#212121")


header = tk.Label(root, text="Калькулятор калорий", font=("Helvetica", 20, "bold"), fg="#ff00ff", bg="#212121")
header.grid(row=0, columnspan=2, pady=20)


age_label = tk.Label(root, text="Возраст (лет):", font=("Arial", 12), bg="#212121", fg="#00ffcc")
age_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
age_entry = tk.Entry(root, font=("Arial", 12), bd=2, relief="solid", width=20, fg="#ff00ff", bg="#333333")
age_entry.grid(row=1, column=1, padx=10, pady=5)


gender_label = tk.Label(root, text="Пол:", font=("Arial", 12), bg="#212121", fg="#00ffcc")
gender_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
gender_var = tk.StringVar(value="M")
male_radio = tk.Radiobutton(root, text="Мужской", variable=gender_var, value="M", font=("Arial", 12), bg="#212121",
                            fg="#00ffcc", selectcolor="#ff00ff")
female_radio = tk.Radiobutton(root, text="Женский", variable=gender_var, value="F", font=("Arial", 12), bg="#212121",
                              fg="#00ffcc", selectcolor="#ff00ff")
male_radio.grid(row=2, column=1, sticky="w", padx=10, pady=5)
female_radio.grid(row=2, column=2, sticky="w", padx=10, pady=5)

weight_label = tk.Label(root, text="Вес (кг):", font=("Arial", 12), bg="#212121", fg="#00ffcc")
weight_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
weight_entry = tk.Entry(root, font=("Arial", 12), bd=2, relief="solid", width=20, fg="#ff00ff", bg="#333333")
weight_entry.grid(row=3, column=1, padx=10, pady=5)


height_label = tk.Label(root, text="Рост (см):", font=("Arial", 12), bg="#212121", fg="#00ffcc")
height_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
height_entry = tk.Entry(root, font=("Arial", 12), bd=2, relief="solid", width=20, fg="#ff00ff", bg="#333333")
height_entry.grid(row=4, column=1, padx=10, pady=5)


activity_level_label = tk.Label(root, text="Уровень физической активности:", font=("Arial", 12), bg="#212121",
                                fg="#00ffcc")
activity_level_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
activity_level_var = tk.IntVar(value=1)
activity_level_optionmenu = tk.OptionMenu(root, activity_level_var, 1, 2, 3, 4, 5)
activity_level_optionmenu.config(font=("Arial", 12), width=17, bg="#ff00ff", fg="#212121")
activity_level_optionmenu.grid(row=5, column=1, padx=10, pady=5)


submit_button = tk.Button(root, text="Рассчитать", command=submit_button_clicked, font=("Arial", 14), bg="#00ffcc",
                          fg="black", bd=0, relief="flat", width=20, height=2)
submit_button.grid(row=6, columnspan=2, pady=20)



def on_hover(event):
    event.widget.config(bg="#ff6347")


def on_leave(event):
    event.widget.config(bg="#00ffcc")


submit_button.bind("<Enter>", on_hover)
submit_button.bind("<Leave>", on_leave)

root.mainloop()