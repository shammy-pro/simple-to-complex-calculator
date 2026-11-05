"""calculator"""
import tkinter as tk
import fractions
# from math import exp as expo
# to import the math module and the exp function from it,
#  used to calculate the exponential of a number.
from simpleeval import simple_eval

# Global variable to store the last result for Ans
# avoid using global statements they are hard(problematic) to debug

# Function to add button text to display


def add_to_display(value):
    """
    Add the specified value to the calculator display.

    Args:
        value (str): The text value to add to the display (e.g., "1", "+", "(")

    This function handles the initial "0" case by replacing it with the new value,
    otherwise it appends the value to the end of the current display text.
    """
    current = display.get()
    if current == "0":
        display.delete(0, tk.END)
        display.insert(0, value)
    else:
        display.insert(tk.END, value)


def delete_one():
    """deletes one character at the very end"""
    display.delete(len(display.get())-1)


def convert_percent():
    """to enable percentage conversion"""
    try:
        value = float(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(value / 100))
    except ValueError:
        pass


def square(n):
    """to find square"""
    return n**2


def square_func():
    """to square the current display value"""
    try:
        value = float(display.get())
        result = square(value)
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except ValueError:
        pass


def sqrt_func():
    """to find square root of the current display value"""
    try:
        value = float(display.get())
        result = value ** 0.5
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except ValueError:
        pass


def fraction_func():
    """to convert the current display value to fraction format n/d"""
    # so help me lord ^_~
    try:
        value = float(display.get())
        frac = fractions.Fraction(value).limit_denominator()
        display.delete(0, tk.END)
        display.insert(0, str(frac))
    except ValueError:
        pass


def evaluate(last_result=0):
    """to evaluate the expression in the display"""
    # sijui kwa nini na macho zangu kubwa sijaona statement iko hadi kwa triple qoutes
    try:
        expression = display.get().strip()
        if not expression:
            return
        # Replace Ans with last result
        expression = expression.replace('Ans', str(last_result))
        # Replace calculator symbols with Python operators
        expression = expression.replace('×', '*').replace('÷', '/')
        # Safe eval with restricted environment
        result = simple_eval(expression)
        last_result = result  # Update last result
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except ImportError:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# 1. Create the main window
root = tk.Tk()
root.title("SHAMMAH'S✌💕")  # simply title of your calculator
root.geometry("450x700")  # Sets the starting size (Width x Height)
root.resizable(True, True)  # the user can adjust the size of the window
root.configure(bg="pink")
# This turns the main window background black
# and whatever sits on it to be light blue

# 2. Add a Label (Text)
label = tk.Label(root, text="Ameingia sasa👌😎😉", font=("Times New Roman", 14))
# the word root is added since we are now building on the root its like our already laid foundation
label.after(200000, label.destroy)
# Position in row 0, span all columns
label.grid(row=0, column=0, columnspan=6, padx=10, pady=10)
# what does pady and padx do and ipady aND IPADX?

# """DISPLAY"""
display = tk.Entry(root, font=("times new roman", 28),
                   bg="black", fg="white", borderwidth=0, justify="right")
# this is to create an entry widget
display.grid(row=1, column=0, columnspan=5, rowspan=2,
             padx=10, pady=10, sticky="nsew")
# this positions the grid and column span
display.insert(0, "0")
# sets the default value

# """FIRST ROW"""
btn_shift = tk.Button(root, text="shift", font=("times new roman", 18),
                      bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                      command=lambda: add_to_display("shift"))
btn_shift.grid(row=3, column=0,
               padx=10, pady=10, sticky="nsew")

btn_alpha = tk.Button(root, text="alpha", font=("times new roman", 18),
                      bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                      command=lambda: add_to_display("alpha"))
btn_alpha.grid(row=3, column=1,
               padx=10, pady=10, sticky="nsew")
btn_up = tk.Button(root, text="˄", font=("times new roman", 18),
                   bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                   command=lambda: add_to_display("˄"))
btn_up.grid(row=3, column=2,
            padx=10, pady=10, sticky="nsew")
btn_mode = tk.Button(root, text="mode", font=("times new roman", 18),
                     bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                     command=lambda: add_to_display("mode"))
btn_mode.grid(row=3, column=3,
              padx=10, pady=10, sticky="nsew")
btn_on = tk.Button(root, text="ON", font=("times new roman", 18),
                   bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                   command=lambda: add_to_display("ON"))
btn_on.grid(row=3, column=4,
            padx=10, pady=10, sticky="nsew")
btn_open = tk.Button(root, text="(", font=("times new roman", 18),
                     bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                     command=lambda: add_to_display("("))
btn_open.grid(row=4, column=0,
              padx=10, pady=10, sticky="nsew")

btn_left = tk.Button(root, text="<", font=("times new roman", 18),
                     bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                     command=lambda: add_to_display("<"))
btn_left.grid(row=4, column=1,
              padx=10, pady=10, sticky="nsew")
btn_perc = tk.Button(root, text="%", font=("times new roman", 18),
                     bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                     command=convert_percent)
btn_perc.grid(row=4, column=2,
              padx=10, pady=10, sticky="nsew")
btn_right = tk.Button(root, text=">", font=("times new roman", 18),
                      bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                      command=lambda: add_to_display(">"))
btn_right.grid(row=4, column=3,
               padx=10, pady=10, sticky="nsew")
btn_close = tk.Button(root, text=")", font=("times new roman", 18),
                      bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                      command=lambda: add_to_display(")"))
btn_close.grid(row=4, column=4,
               padx=10, pady=10, sticky="nsew")
btn_frac = tk.Button(root, text="n/d", font=("times new roman", 18),
                     bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                     command=lambda: add_to_display("n/d"))
btn_frac.grid(row=5, column=0,
              padx=10, pady=10, sticky="nsew")

btn_factorials = tk.Button(root, text="n!", font=("times new roman", 18),
                           bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                           command=lambda: add_to_display("n!"))
btn_factorials.grid(row=5, column=1,
                    padx=10, pady=10, sticky="nsew")
btn_down = tk.Button(root, text="˅", font=("times new roman", 18),
                     bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                     command=lambda: add_to_display("˅"))
btn_down.grid(row=5, column=2,
              padx=10, pady=10, sticky="nsew")
btn_permutation = tk.Button(root, text="nPr", font=("times new roman", 18),
                            bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                            command=lambda: add_to_display("×"))
btn_permutation.grid(row=5, column=3,
                     padx=10, pady=10, sticky="nsew")
btn_combination = tk.Button(root, text="nCr", font=("times new roman", 18),
                            bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                            command=lambda: add_to_display("÷"))
btn_combination.grid(row=5, column=4,
                     padx=10, pady=10, sticky="nsew")
btn_power = tk.Button(root, text="xⁿ", font=("times new roman", 18),
                      bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                      command=lambda: add_to_display("1"))
btn_power.grid(row=6, column=0,
               padx=10, pady=10, sticky="nsew")

btn_powerroot = tk.Button(root, text="ⁿ√x", font=("times new roman", 18),
                          bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                          command=lambda: add_to_display("2"))
btn_powerroot.grid(row=6, column=1,
                   padx=10, pady=10, sticky="nsew")
btn_sin = tk.Button(root, text="sin", font=("times new roman", 18),
                    bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                    command=lambda: add_to_display("3"))
btn_sin.grid(row=6, column=2,
             padx=10, pady=10, sticky="nsew")
btn_cos = tk.Button(root, text="cos", font=("times new roman", 18),
                    bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                    command=lambda: add_to_display("4"))
btn_cos.grid(row=6, column=3,
             padx=10, pady=10, sticky="nsew")
btn_tan = tk.Button(root, text="tan", font=("times new roman", 18),
                    bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                    command=lambda: add_to_display("-"))
btn_tan.grid(row=6, column=4,
             padx=10, pady=10, sticky="nsew")
btn_sqrt = tk.Button(root, text="√", font=("times new roman", 18),
                     bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                     command=lambda: add_to_display("0"))
btn_sqrt.grid(row=7, column=0,
              padx=10, pady=10, sticky="nsew")

btn_sq = tk.Button(root, text="x²", font=("times new roman", 18),
                   bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                   command=lambda: add_to_display("x²"))
btn_sq.grid(row=7, column=1,
            padx=10, pady=10, sticky="nsew")
btn_naturallog = tk.Button(root, text="ln", font=("times new roman", 18),
                           bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                           command=fraction_func)
btn_naturallog.grid(row=7, column=2,
                    padx=10, pady=10, sticky="nsew")
btn_exponent = tk.Button(root, text="eⁿ", font=("times new roman", 18),
                         bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                         command=lambda: add_to_display("eⁿ"))
btn_exponent.grid(row=7, column=3,
                  padx=10, pady=10, sticky="nsew")
btn_log = tk.Button(root, text="log", font=("times new roman", 18),
                    bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                    command=evaluate)
btn_log.grid(row=7, column=4,
             padx=10, pady=10, sticky="nsew")

# """ nataka kufanya experiment"""
btn_7 = tk.Button(root, text="7", font=("times new roman", 18),
                  bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                  command=lambda: add_to_display("7"))
btn_7.grid(row=8, column=0,
           padx=10, pady=10, sticky="nsew")
btn_8 = tk.Button(root, text="8", font=("times new roman", 18),
                  bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                  command=lambda: add_to_display("8"))
btn_8.grid(row=8, column=1,
           padx=10, pady=10, sticky="nsew")
btn_9 = tk.Button(root, text="9", font=("times new roman", 18),
                  bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                  command=lambda: add_to_display("9"))
btn_9.grid(row=8, column=2,
           padx=10, pady=10, sticky="nsew")
btn_delete = tk.Button(root, text="del", font=("times new roman", 18),
                       bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                       command=lambda: display.delete(len(display.get())-1))
btn_delete.grid(row=8, column=3,
                padx=10, pady=10, sticky="nsew")
btn_ac = tk.Button(root, text="Ac", font=("times new roman", 18),
                   bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                   command=lambda: display.delete(0, tk.END) or display.insert(0, "0"))
btn_ac.grid(row=8, column=4,
            padx=10, pady=10, sticky="nsew")
btn_4 = tk.Button(root, text="4", font=("times new roman", 18),
                  bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                  command=lambda: add_to_display("4"))
btn_4.grid(row=9, column=0,
           padx=10, pady=10, sticky="nsew")
btn_5 = tk.Button(root, text="5", font=("times new roman", 18),
                  bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                  command=lambda: add_to_display("5"))
btn_5.grid(row=9, column=1,
           padx=10, pady=10, sticky="nsew")
btn_6 = tk.Button(root, text="6", font=("times new roman", 18),
                  bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                  command=lambda: add_to_display("6"))
btn_6.grid(row=9, column=2,
           padx=10, pady=10, sticky="nsew")
btn_multiply = tk.Button(root, text="x", font=("times new roman", 18),
                         bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                         command=lambda: add_to_display("x"))
btn_multiply.grid(row=9, column=3,
                  padx=10, pady=10, sticky="nsew")
btn_divide = tk.Button(root, text="÷", font=("times new roman", 18),
                       bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                       command=lambda: add_to_display("÷"))
btn_divide.grid(row=9, column=4,
                padx=10, pady=10, sticky="nsew")

# may thee experiment go on
btn_1 = tk.Button(root, text="1", font=("times new roman", 18),
                  bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                  command=lambda: add_to_display("1"))
btn_1.grid(row=10, column=0,
           padx=10, pady=10, sticky="nsew")
btn_2 = tk.Button(root, text="2", font=("times new roman", 18),
                  bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                  command=lambda: add_to_display("2"))
btn_2.grid(row=10, column=1,
           padx=10, pady=10, sticky="nsew")
btn_3 = tk.Button(root, text="3", font=("times new roman", 18),
                  bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                  command=lambda: add_to_display("3"))
btn_3.grid(row=10, column=2,
           padx=10, pady=10, sticky="nsew")
btn_subtract = tk.Button(root, text="-", font=("times new roman", 18),
                         bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                         command=lambda: add_to_display("-"))
btn_subtract.grid(row=10, column=3,
                  padx=10, pady=10, sticky="nsew")
btn_add = tk.Button(root, text="+", font=("times new roman", 18),
                    bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                    command=lambda: add_to_display("+"))
btn_add.grid(row=10, column=4,
             padx=10, pady=10, sticky="nsew")
btn_0 = tk.Button(root, text="0", font=("times new roman", 18),
                  bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                  command=lambda: add_to_display("0"))
btn_0.grid(row=11, column=0,
           padx=10, pady=10, sticky="nsew")
btn_decimal = tk.Button(root, text=".", font=("times new roman", 18),
                        bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                        command=lambda: add_to_display("."))
btn_decimal.grid(row=11, column=1,
                 padx=10, pady=10, sticky="nsew")
btn_pie = tk.Button(root, text="π", font=("times new roman", 18),
                    bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                    command=lambda: add_to_display("π"))
btn_pie.grid(row=11, column=2,
             padx=10, pady=10, sticky="nsew")
btn_answer = tk.Button(root, text="ans", font=("times new roman", 18),
                       bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                       command=lambda: add_to_display("ans"))
btn_answer.grid(row=11, column=3,
                padx=10, pady=10, sticky="nsew")
btn_equall = tk.Button(root, text="=", font=("times new roman", 18),
                       bg="#AD0808", fg="white", borderwidth=0, height=1, width=1,
                       command=evaluate)
btn_equall.grid(row=11, column=4,
                padx=10, pady=10, sticky="nsew")


# wow just wow

# Configure grid weights for proper resizing
for i in range(7):  # 7 rows (0-6)
    root.grid_rowconfigure(i, weight=1)
# makes the button expand to fill its grid cell in all directions(north, south, east, west).
for i in range(5):  # 5 columns (0-4)
    root.grid_columnconfigure(i, weight=1)

# 3. Start the application loop
root.mainloop()  # tells the computer to stay open and wait for keyins
