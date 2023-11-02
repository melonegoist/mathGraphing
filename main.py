from tkinter import *

sc = Tk()
sc.geometry("500x500")
sc.configure(bg = 'white')



def calculate(func):
    # li = []
    # for i in range(0, 10):
    #     li.append(func[func.find('{')+1:func.find('}')])
    #     func = func[func.find('}')+1:]
    #     if func == '':
    #         break
    li = []
    
    for x in range(-10, 10):
        try:
            li.append(eval(func)*25)
        except:
            li.append(0)
    return li


# def calculate2(func2):
#     li2 = []

#     for y in range(-10, 10):
#         try:
#             li2.append(eval(func2)*25)
#         except:
#             li2.append(0)
#     return li2
    


def start():
    global func
    func = function_entry.get()[2:]

    
    dots = calculate(func)
    print(dots)

    ind = 0
    
    for i in range(0, 500, 25):
        try:
            c.create_oval(i-2, -dots[ind]+248, i+3, -dots[ind]+253, fill='red')
        except:
            pass
        print(i, ind, dots[ind])
        ind+=1


# def start2():
#     global func2
#     func2 = function_entry2.get()[2:]

#     dots2 = calculate2(func2)
#     print(dots2)

#     ind2 = 0

#     for i in range(0, 500, 25):
#         try:
#             c.create_oval(-dots2[ind2]+248, i-2, -dots2[ind2]+253, i+3, fill='red')
#         except:
#             pass
#         print(i, ind2, dots2[ind2])
#         ind2+=1


def window():
    global function_entry
    sc2 = Toplevel()
    sc2.geometry("250x100")
    sc2.configure(bg = 'white')

    function_entry = Entry(sc2, bg = 'white', justify = 'center')
    function_entry.insert(0, 'y=')
    function_entry.place(x = 70, y = 40)

    button_start = Button(sc2,
        text = 'start',
        bg = 'white',
        relief = 'flat',
        overrelief = 'solid',
        command = start
    )

    button_start.place(x = 115, y = 70)


# def window2():
#     global function_entry2
#     sc3 = Toplevel()
#     sc3.geometry("250x100")
#     sc3.configure(bg = 'white')

#     function_entry2 = Entry(sc3, bg = 'white', justify = 'center')
#     function_entry2.insert(0, 'x=')
#     function_entry2.place(x = 70, y = 40)

#     button_start2 = Button(sc3,
#         text = 'start',
#         bg = 'white',
#         relief = 'flat',
#         overrelief = 'solid',
#         command = start2
#     )

    # button_start2.place(x = 115, y = 70)



c = Canvas(bg = 'white', highlightthickness=0, width=500, height=500)

c.create_line(0, 250, 500, 250)
c.create_line(250, 500, 250, 0)

# zero_label = Label(text = '0', bg = 'white').place(x = 235, y = 255)

c.place(x = 0, y = 0)

j = -9
m = 9
for i in range(15, 490, 25):
    if i > 250:
        i+=5
    elif i ==240:
        i = 1000
    Label(
        text = f'{j}',
        bg = 'white',
    ).place(x = i, y = 255)

    Label(
        text = f'{m}',
        bg = 'white'
    ).place(x = 230, y = i)

    j+=1
    m-=1

for i in range(0, 525, 25):
    c.create_line(i, 245, i, 255)
    c.create_line(245, i, 255, i)


bttn_create = Button(
    text = 'function',
    bg = 'white',
    relief = 'flat',
    overrelief = 'solid',
    command = window
)

bttn_create.place(x = 420, y = 30)


# bttn_extra = Button(
#     text = 'extra',
#     bg = 'white',
#     relief = 'flat',
#     overrelief = 'solid',
#     command = window2
# )

# bttn_extra.place(x = 420, y = 70)


sc.mainloop()