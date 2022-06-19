import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfile
from gtts import gTTS
import os
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")



global tagged
tagged = ""
keyword = ""



def about():
    filewin = Toplevel(root)
    string = """
System Software Project by:
1DS19CS013 - ADVITIYA C S
1DS19CS014 - AHMED MOHTESHAMUDDIN
1DS19CS015 - AKANSHA SINGH
1DS19CS016 - AKASH
        """
    aboutlabel = Label(filewin, text=string)
    aboutlabel.pack(anchor=tkinter.CENTER)


def open_file():
    global text, save_file_id
    open_file_loc = askopenfilename()
    open_file = open(open_file_loc, 'r')
    text.delete(1.0, END)
    text.insert(END, open_file.read())
    save_file_id = open_file_loc


def save_as_file():
    global text, save_file_id
    name = asksaveasfile(mode='w', defaultextension=".txt")
    text2save = str(text.get(0.0, END))
    name.write(text2save)
    name = str(name)[(str(name).find("name='") + 6):str(name).find("'", (str(name).find("name='") + 6))]
    save_file_id = name


def save_file():
    global text, save_file_id
    if save_file_id == "":
        save_as_file()
    else:
        with open(save_file_id, 'w') as f:
            f.write(text.get(0.0, END))


def New_file():
    text.delete(1.0, END)
    save_file_id = ' '


def find_destroy():
    text.tag_remove(keyword, 0.0, END)
    search_box.destroy()
    button1.destroy()
    button2.destroy()


def find_button():
    global search_box, label1, button1, button2
    search_box = Text(root, height=1, width=20)
    search_box.pack(side=LEFT)

    button1 = customtkinter.CTkButton(master=root, text="Find",width=32,height=16,command=Find)
    button1.pack(side=LEFT)
    button2 = customtkinter.CTkButton(master=root,width=16,height=16,text="X", command=find_destroy)
    button2.pack(side=RIGHT)

    # button1 = Button(root, text="find", command=Find)
    # button1.pack(side=LEFT)
    # button2 = Button(root, text="X", command=find_destroy)
    # button2.pack(side=LEFT)


def Find():
    global keyword
    global tagged
    text.tag_remove(tagged,0.0,END)
    keyword = search_box.get(0.0, END)
    text_box = text.get(0.0, END)
    text.tag_config(keyword, background='lightblue')
    tagged = keyword
    i = j = i_p = 0
    row = 1
    n = 0
    while i < len(text_box):
        if (text_box[i] == keyword[j]):
            i_p = i - n
            while (text_box[i] == keyword[j]) and (j < len(keyword) - 1):
                j += 1
                i += 1
            i -= 1
            if j == len(keyword) - 1:
                i -= 1
        if j == len(keyword) - 1:
            pos_start = str(row) + "." + str(i_p)
            pos_end = '{}+{}c'.format(pos_start, len(keyword) - 1)
            # print(pos_start,pos_end)
            text.tag_add(keyword, pos_start, pos_end)

        if text_box[i] == '\n':
            n = i + 1
            row += 1
            i_p = 0
        j = 0
        i += 1


def replace_button():
    global search_box, button2, replace_box, label1, label2
    #label1 = Label(text="Find")
    label1 = customtkinter.CTkLabel(master=root, text="Find:",width=10)
    label1.pack(side=LEFT)
    search_box = Text(root, height=1, width=20)
    search_box.pack(side=LEFT)
    label2 = customtkinter.CTkLabel(master=root, text="Replace:",width=12)
    label2.pack(side=LEFT)
    replace_box = Text(root, height=1, width=20)
    replace_box.pack(side=LEFT)
    button2 = customtkinter.CTkButton(master=root, text="Replace", command=Replace)
    button2.pack(side=LEFT)


def Replace():
    keyword = search_box.get(0.0, END)
    replace_word = replace_box.get(0.0, END)
    text_box = text.get(0.0, END)
    q = 0
    while q < len(text_box):
        i = j = i_p = n = 0
        row = 1
        while i < len(text_box):
            if (text_box[i] == keyword[j]):
                i_p = i - n
                while (text_box[i] == keyword[j]) and (j < len(keyword) - 1):
                    j += 1
                    i += 1
                i -= 1
                if j == len(keyword) - 1:
                    i -= 1
            if j == len(keyword) - 1:
                pos_start = str(row) + "." + str(i_p)
                pos_end = '{}+{}c'.format(pos_start, len(keyword) - 1)
                replace_start = '{}+{}c'.format(pos_start, len(replace_word) - 1)
                replace_end = '{}+{}c'.format(pos_start, len(replace_word))
                text.delete(pos_start, pos_end)
                text.insert(pos_start, replace_word)
                text.delete(replace_start, replace_end)
                break

            if text_box[i] == '\n':
                n = i + 1
                row += 1
                i_p = 0
            j = 0
            i += 1
        q += 1
        text_box = text.get(0.0, END)

    aupdate()
    label1.destroy()
    label2.destroy()
    replace_box.destroy()
    button2.destroy()
    search_box.destroy()

def drop_style(*args):
    txt = text.get(0.0, END)
    text.delete(0.0, END)
    text.configure(font=(var.get(), text_size))
    text.insert(0.0, txt)
    w.destroy()


def font_style():
    global text, var, w
    var = StringVar(root)
    var.set(text_style)
    #match_list = ["Times New Roman", "Helvetica", "Ariel", "Courier", "Symbol"]
    var.trace('w', drop_style)
   # w = OptionMenu(root, var, *match_list)
    w = customtkinter.CTkOptionMenu(master=root, values=["Times New Roman", "Helvetica", "Ariel", "Courier", "Symbol"], variable=var)
    #w.pack()
    w.pack()


def drop_size(*args):
    txt = text.get(0.0, END)
    text.delete(0.0, END)
    text.configure(font=(text_style, var.get()))
    text.insert(0.0, txt)
    w.destroy()


def font_size():
    global var, w
    var = StringVar(root)
    var.set(text_size)
   # match_list = [8, 10, 11, 12, 14]
    var.trace('w', drop_size)
    #w = OptionMenu(root, var, *match_list)
    w=customtkinter.CTkOptionMenu(master=root,values=["8","10","11","12","14"],variable=var)
    w.pack()

def ttsrun():
    mytext = text.get(0.0, END)
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)

    myobj.save("welcome.mp3")
    os.system("welcome.mp3")

def update(event):
    text_box = text.get(0.0, END)
    chars = "No. of characters:{}"
    nc=len(text_box)-1
    labelc.set_text(chars.format(nc))

def aupdate():
    text_box = text.get(0.0, END)
    chars = "No. of characters:{}"
    nc = len(text_box) - 1
    labelc.set_text(chars.format(nc))




root = customtkinter.CTk()
root.title("Text Editor SS")


labelc = customtkinter.CTkLabel(master=root, text="No. of characters:",width=10)
labelc.pack(side=BOTTOM,anchor='w')


text = Text(root, width=100, undo=True)
text_size = 11
text_style = "Times New Roman"
text.configure(font=(text_style, text_size))
text.pack(expand=True, fill='both',side=BOTTOM)
#text.pack()
save_file_id = ""

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=New_file)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_command(label="Save as...", command=save_as_file)
filemenu.add_command(label="Exit", command=root.quit)

Editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Format", menu=Editmenu)
Editmenu.add_command(label="Font Style", command=font_style)
Editmenu.add_command(label="Font Size", command=font_size)

Searchmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=Searchmenu)
Searchmenu.add_command(label="Find", command=find_button)
Searchmenu.add_command(label="Find and Replace", command=replace_button)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=about)

image_size=60
mic_image = ImageTk.PhotoImage(Image.open(r"speaker.png").resize((image_size, image_size)))

button = customtkinter.CTkButton(master=root,width=64,height=64,border_width=0,corner_radius=0,command=ttsrun,image=mic_image,text="")
button.place(relx=1, rely=1, anchor=tkinter.SE)



text.bind("<KeyRelease>", update)

photo = PhotoImage(file = "appicon.png")
root.iconphoto(False,photo)

root.config(menu=menubar)
root.mainloop()
