from tkinter import *

class CalcEntry(Entry):
    # Constructs entry box object as part of CalcEntry object, *kwargs allows us to pass as many parameters to the entry box as we would like
    # Entry class variable is where values will be stored for addition
    def __init__(self, *args, **kwargs):
        Entry.__init__(self, *args, **kwargs)
        self.last_operator = None
        self.value_totalled = False
        self.current_value = None

    # Adds numbers to entry box
    def enter_numbers(self, number):
        if self.value_totalled == True:
            self.clear_entry()
            self.value_totalled = False
        self.insert(END, number)

    # Clears entry field
    def clear_entry(self):
        self.delete(0, END)
    
    # Function to check what value to return from entry box
    def return_entry_number(self):
        print(self.get())
        # Checks if value exists currently within entry box, defaults to 0.00 if value does not exist.
        if len(self.get()) == 0:
            value_to_return = 0.00
        else:
            value_to_return = float(self.get())
        return value_to_return

    # Functions to add: 
        # Button to clear stored values along with current values in entrybox
        # 1/X button to return 1/whatever number is entered in. For example 1/4 should return 0.25
        # X^2 button handle squaring numbers. Example 2^2 should return 4
        # Sqrt button to get the square root of a number. Example 4 should return 2
        # Backspace button to remove just the last value in entry box


    # Clear stored number and current text in entrybox
    def clear_all(self):
        self.clear_entry()
        self.value_totalled = False
        self.current_value = None
        self.last_operator = None

    # Percent function: Requires number stored in memory and a second number, function multiplies first and second numbers and then divides the result by 100 to get what percent num2 percent of num1
    # Uses last operator stored to decide if result should be added/subtracted etc. to first number
    def find_percent(self):
        value = self.return_entry_number()
        if self.current_value == None:
            self.clear_entry()
            self.insert(0, 0)
        else:
            percent_value = (value * self.current_value) / 100
            self.operation(self.last_operator, percent_value)
            
    # Function to perform addition/subtraction/multiplication/division
    def operation(self, operator, value=None):
        if value == None:
            value = self.return_entry_number()
        if self.current_value == None:
            self.current_value = value
        else:
            if operator == "+":
                self.current_value += value
            elif operator == "-":
                self.current_value -= value
            elif operator == "*":
                self.current_value *= value
            elif operator == "/":
                self.current_value /= value
        self.last_operator = operator
        self.clear_entry()

    # Performs calculations when equal button is pressed
    def calculate(self):
        self.operation(self.last_operator)
        self.insert(0, self.current_value)
        self.current_value = None
        self.value_totalled = True

class Calculator:
    def __init__(self):
        # Builds main window
        self.root = Tk()

        # Adds title to window
        self.root.title("Simple Calculator")

        # Creates entrybox
        self.entry = CalcEntry(self.root, width=55, borderwidth=5)

        # Places entry box on window
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Creates number pad buttons
        button_1 = Button(self.root, text="1", padx=40, pady=20, command=lambda: self.entry.enter_numbers(1))
        button_2 = Button(self.root, text="2", padx=40, pady=20, command=lambda: self.entry.enter_numbers(2))
        button_3 = Button(self.root, text="3", padx=40, pady=20, command=lambda: self.entry.enter_numbers(3))
        button_4 = Button(self.root, text="4", padx=40, pady=20, command=lambda: self.entry.enter_numbers(4))
        button_5 = Button(self.root, text="5", padx=40, pady=20, command=lambda: self.entry.enter_numbers(5))
        button_6 = Button(self.root, text="6", padx=40, pady=20, command=lambda: self.entry.enter_numbers(6))
        button_7 = Button(self.root, text="7", padx=40, pady=20, command=lambda: self.entry.enter_numbers(7))
        button_8 = Button(self.root, text="8", padx=40, pady=20, command=lambda: self.entry.enter_numbers(8))
        button_9 = Button(self.root, text="9", padx=40, pady=20, command=lambda: self.entry.enter_numbers(9))
        button_0 = Button(self.root, text="0", padx=40, pady=20, command=lambda: self.entry.enter_numbers(0))

        # Creates buttons holding calculation functions and clear function
        button_add = Button(self.root, text="+", padx=39, pady=20, command=lambda: self.entry.operation("+"))
        button_subtract = Button(self.root, text="-", padx=39, pady=20, command=lambda: self.entry.operation("-"))
        button_multiply = Button(self.root, text="*", padx=39, pady=20, command=lambda: self.entry.operation("*"))
        button_divide = Button(self.root, text="/", padx=39, pady=20, command=lambda: self.entry.operation("/"))
        button_percent = Button(self.root, text="%", padx=39, pady=20, command=self.entry.find_percent)
        button_equal = Button(self.root, text="=", padx=180, pady=20, command=self.entry.calculate)
        button_clear = Button(self.root, text="CE", padx=79, pady=20, command=self.entry.clear_entry)
        button_clear_all = Button(self.root, text="C", padx=39, pady=20, command=self.entry.clear_all)

        # Adds buttons to grid
        # First row of buttons after entry box
        button_7.grid(row=1, column=0)
        button_8.grid(row=1, column=1)
        button_9.grid(row=1, column=2)
        button_add.grid(row=1, column=3)

        # Second row of buttons
        button_4.grid(row=2, column=0)
        button_5.grid(row=2, column=1)
        button_6.grid(row=2, column=2)
        button_subtract.grid(row=2, column=3)

        # Third row of buttons
        button_1.grid(row=3, column=0)
        button_2.grid(row=3, column=1)
        button_3.grid(row=3, column=2)
        button_multiply.grid(row=3, column=3)

        # Fourth row of buttons
        button_0.grid(row=4, column=0)
        button_clear.grid(row=4, column=1, columnspan=2)
        button_divide.grid(row=4, column=3)
        button_percent.grid(row=4, column=4)
        button_clear_all.grid(row=4, column=5)

        # Last row
        button_equal.grid(row=5, column=0, columnspan=4)

        # Maintains application loop until retrieving input to close application
        self.root.mainloop()

new_calculator = Calculator()
