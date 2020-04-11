from tkinter import *
import os
import  tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename

class Notepad:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.file = None

        self.root = Tk()
        self.root.geometry(f'{self.width}x{self.height}')
        self.root.title('Untitled - Notepad')

        # notepad icon
        img = PhotoImage(file = 'notepad.gif')
        self.root.tk.call('wm', 'iconphoto', self.root._w, img)

    def create_menu_bar(self):
        # menu bar
        self.menu_bar = Menu(self.root)

        # File Submenu
        self.file_submenu = Menu(self.menu_bar, tearoff = 0)
        self.file_submenu.add_command(label = 'New', command = self.new)
        self.file_submenu.add_command(label = 'Open...', command = self.open_file)
        self.file_submenu.add_separator()
        self.file_submenu.add_command(label = 'Save', command = self.save)
        self.file_submenu.add_command(label = 'Save As...', command = self.save_as)
        self.file_submenu.add_separator()
        self.file_submenu.add_command(label = 'Exit', command = quit)
        self.menu_bar.add_cascade(label = 'File', menu = self.file_submenu)

        # Edit menu
        self.edit_submenu = Menu(self.menu_bar, tearoff = 0)
        self.edit_submenu.add_command(label = 'Cut', command = self.cut)
        self.edit_submenu.add_command(label = 'Copy', command = self.copy)
        self.edit_submenu.add_command(label = 'Paste', command = self.paste)
        self.menu_bar.add_cascade(label = 'Edit', menu = self.edit_submenu)

        # Help menu
        self.help_submenu = Menu(self.menu_bar, tearoff = 0)
        self.help_submenu.add_command(label = 'View Help', command = self.view_help)
        self.help_submenu.add_command(label = 'Send Feedback', command = self.send_feedback)
        self.help_submenu.add_separator()
        self.help_submenu.add_command(label = 'About Notepad', command = self.about_notepad)
        self.menu_bar.add_cascade(label = 'Help', menu = self.help_submenu)

        self.root.config(menu = self.menu_bar)


    def create_text_area(self):
        # text area
        self.text_area = Text(self.root, font = "Lucida 13")
        self.text_area.pack(expand = True, fill = BOTH)

        # scroll bar
        self.scroll_bar = Scrollbar(self.text_area)
        self.scroll_bar.pack(side = RIGHT, fill = Y)
        self.scroll_bar.config(command = self.text_area.yview)
        
        self.text_area.config(yscrollcommand = self.scroll_bar.set)

    
    def new(self):
        self.file = None
        self.root.title('Untitled - Notepad')
        self.text_area.delete(1.0, END)

    
    def open_file(self):
        self.file = askopenfilename(defaultextension = '.txt', filetypes = [('All Files', '*.*'), ('Text Documents', '*.txt')])

        if self.file == "":
            # no file choosen
            self.file = None

        else:
            # file chosen
            self.root.title(os.path.basename(self.file) + ' - Notepad')
            self.text_area.delete(1.0, END)
            reader = open(self.file, 'r')
            self.text_area.insert(1.0, reader.read())
            reader.close()


    def save(self):
        if self.file == None:
            # writing and saving a new file
            self.save_as()
        
        else:
            # writing and saving to an existing file
            writer = open(self.file, 'w')
            writer.write(self.text_area.get(1.0, END))
            writer.close()

    def save_as(self):
        self.file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension = '.txt', filetypes = [('All Files', '*.*'), ('Text Documents', '*.txt')])

        if self.file == "":
            # no file chosen
            self.file = None

        else:
            # file choosen
            self.root.title(os.path.basename(self.file) + ' - Notepad')
            writer = open(self.file, 'w')
            writer.write(self.text_area.get(1.0, END))
            writer.close()


    def cut(self):
        self.text_area.event_generate("<<Cut>>")


    def copy(self):
        self.text_area.event_generate(('<<Copy>>'))


    def paste(self):
        self.text_area.event_generate(('<<Paste>>'))


    def about_notepad(self):
        tmsg.showinfo('About Notepad', 'Developed by Ayan Kumar Saha')


    def send_feedback(self):
        pass


    def view_help(self):
        pass

    def configure(self):
        self.create_menu_bar()
        self.create_text_area()

    
    def run(self):
        self.root.mainloop()

notepad = Notepad(700, 500)
notepad.configure()
notepad.run()