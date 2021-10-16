import tkinter as tk
import sys 

window = tk.Tk()
window.title('Easy Calculator (Python ver.)')
window.geometry('550x400')
window.configure(background='white')

op_array=[]

def Cal(a, b, op):
    if op == '+':
        output = a + b
    elif op == '-':
        output = a - b
    elif op == '*':
        output = a * b
    elif op == '/':
        try:
            output = a / b
        except ZeroDivisionError:
            output = sys.float_info.min
    return output

def Cal_P():
    n1 = op_array[0]
    opt = op_array[1]
    n2 = op_array[2]
    N = Cal((float)(n1), (float)(n2), opt)
    print(N)

top_frame = tk.Frame(window)
top_frame.pack()
bottom_frame = tk.Frame(window)
bottom_frame.pack(side=tk.BOTTOM)

header_label = tk.Label(window, text='Enter a two-number operation (Enter 0 and 0 to end)', bg='white', fg='black')
header_label.pack()

op_frame = tk.Frame(window)
op_frame.pack(side=tk.TOP)
op_entry = tk.Entry(op_frame, bg='white')
op_entry.pack(side=tk.LEFT)

calculate_btn = tk.Button(window, text='Run', command=Cal_P(), bg='white', fg='black')
calculate_btn.pack()

result_label = tk.Label(window)
result_label.pack()

window.mainloop()