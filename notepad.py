# TODO: 
# Add Key bindings + Keys shortcuts to the menu
# Add new window tab
# Add word wrap
# Add font customization
# Look for zoom
# Status bar

from tkinter import *
import os
import  tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import webbrowser

class Notepad:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.file = None

        # main window
        self.root = Tk()
        self.root.geometry(f'{self.width}x{self.height}')
        self.root.title('Untitled - Notepad')
        
        # notepad icon
        img = PhotoImage(file = 'notepad.gif')
        self.root.tk.call('wm', 'iconphoto', self.root._w, img)

        # menu bar and text area
        self.menu_bar = Menu(self.root)
        self.text_area = Text(self.root, font = "Lucida 13", undo = True)
   
    
    #creating status bar at the bottom
    def status_bar(self):
        self.statusvar = StringVar()
        self.statusvar.set("Created By A")
        self.sbar = Label(self.root,textvariable=statusvar,relief=SUNKEN,font=("cursive",10,"bold"),anchor="e",background="darkolivegreen")
        self.sbar.pack(side=BOTTOM,fill=X)
        
    def create_menu_bar(self):
        
        # File Submenu
        self.file_submenu = Menu(self.menu_bar, tearoff = 0)
        self.file_submenu.add_command(label = 'New', command = self.new)
        self.file_submenu.add_command(label = 'Open...', command = self.open_file)
        self.file_submenu.add_separator()
        self.file_submenu.add_command(label = 'Save', command = self.save)
        self.file_submenu.add_command(label = 'Save As...', command = self.save_as)
        self.file_submenu.add_separator()
        self.file_submenu.add_command(label = 'Exit', command = self.close)
        self.menu_bar.add_cascade(label = 'File', menu = self.file_submenu)

        # Edit menu
        self.edit_submenu = Menu(self.menu_bar, tearoff = 0)
        self.edit_submenu.add_command(label = 'Undo', command = self.text_area.edit_undo)
        self.edit_submenu.add_command(label = 'Redo', command = self.text_area.edit_redo)
        self.edit_submenu.add_separator()
        self.edit_submenu.add_command(label = 'Cut', command = self.cut)
        self.edit_submenu.add_command(label = 'Copy', command = self.copy)
        self.edit_submenu.add_command(label = 'Paste', command = self.paste)
        self.edit_submenu.add_command(label="Select All", command=self.selectall)
        self.edit_submenu.add_separator()
        self.edit_submenu.add_command(label = 'Delete', command = self.delete)
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
        self.text_area.pack(expand = True, fill = BOTH)

        # scroll bar
        self.scroll_bar = Scrollbar(self.text_area)
        self.scroll_bar.pack(side = RIGHT, fill = Y)
        self.scroll_bar.config(command = self.text_area.yview)
        
        self.text_area.config(yscrollcommand = self.scroll_bar.set)

    def selectall(self):
        self.text.tag_add(SEL,"1.0",END)
        self.text.mark_set(INSERT,"1.0")
        self.text.see(INSERT)
        return 'break'

    def new(self):
        text_area_content = self.text_area.get(1.0, 'end-1c')

        if self.file != None:
            reader = open(self.file, 'r')
            file_content = reader.read()

            if file_content != text_area_content:

                answer = tmsg.askyesnocancel('Notepad', f'Do you want to save changes to {self.file}?')
                if answer == True:
                    self.save()

                elif answer == False:
                    self.file = None
                    self.root.title('Untitled - Notepad')
                    self.text_area.delete(1.0, 'end-1c')

                else:
                    pass

            else:
                self.file = None
                self.root.title('Untitled - Notepad')
                self.text_area.delete(1.0, 'end-1c')

        else:
            if len(text_area_content) > 0:
                answer = tmsg.askyesnocancel('Notepad', 'Do you want to save changes to Untitlied?')
                if answer == True:
                    self.save_as()

                elif answer == False:
                    self.file = None
                    self.root.title('Untitled - Notepad')
                    self.text_area.delete(1.0, 'end-1c')

                else:
                    pass

            else:
                self.file = None
                self.root.title('Untitled - Notepad')
                self.text_area.delete(1.0, 'end-1c')
        

    def open_file(self):
        self.file = askopenfilename(defaultextension = '.txt', filetypes = [('All Files', '*.*'), ('Text Documents', '*.txt')])

        if self.file == "":
            # no file choosen
            self.file = None

        else:
            # file chosen
            self.root.title(os.path.basename(self.file) + ' - Notepad')
            self.text_area.delete(1.0, 'end-1c')
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
            writer.write(self.text_area.get(1.0, 'end-1c'))
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
            writer.write(self.text_area.get(1.0, 'end-1c'))
            writer.close()

    
    def close(self):
        text_area_content = self.text_area.get(1.0, 'end-1c')

        if self.file == None:
            if len(text_area_content) > 0:
                answer = tmsg.askyesnocancel('Notepad', f'Do you want to save changes to Untitled?')
                if answer == True:
                    self.save_as()

                elif answer == False:
                    self.root.destroy()

                else:
                    pass

            else:
                self.root.destroy()
                
        else:
            reader = open(self.file, 'r')
            file_content = reader.read()

            if file_content != text_area_content:

                answer = tmsg.askyesnocancel('Notepad', f'Do you want to save changes to {self.file}?')
                if answer == True:
                    self.save()

                elif answer == False:
                    self.root.destroy()

                else:
                    pass

            else:
                self.root.destroy()



    def cut(self):
        self.text_area.event_generate("<<Cut>>")


    def copy(self):
        self.text_area.event_generate(('<<Copy>>'))


    def paste(self):
        self.text_area.event_generate(('<<Paste>>'))

    
    def delete(self):
        self.text_area.event_generate(('<Delete>'))


    def about_notepad(self):
        tmsg.showinfo('About Notepad', 'Developed by Ayan Kumar Saha')


    def send_feedback(self):
        answer = tmsg.askyesno('Feedback', 'Do you like my project?')
        if answer == True:
            if tmsg.askyesno('Give Rating', 'Would you take a moment to give a star to my GitHub repository?'):
                webbrowser.open_new('https://github.com/Ayan-Kumar-Saha/tkinter-Notepad')
            else:
                tmsg.showinfo(message = 'Thank you for your feedback!')

        else:
            tmsg.showinfo(message = 'Thank you for your feedback!')


    def view_help(self):
        webbrowser.open_new('https://github.com/Ayan-Kumar-Saha/tkinter-Notepad/blob/master/README.md')


    def configure(self):
        self.create_menu_bar()
        self.create_text_area()

    
    def run(self):
        self.root.mainloop()


notepad = Notepad(700, 500)
notepad.configure()
notepad.run()
