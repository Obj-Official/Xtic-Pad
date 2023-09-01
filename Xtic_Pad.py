from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename 
import os.path 
import tkinter.messagebox
import tkinter.font


class XticFileEditor:
    def __init__(self):
        window = Tk()
        self.window = window
        window.title("Xtic Pad")
        window.geometry("520x520")
        window.configure(bg = "maroon")
        self.fileX = ""

        #menu bar
        menubarX = Menu(window)
        window.config(menu = menubarX)
        #menu option1
        filemenu = Menu(menubarX, tearoff = 0)
        menubarX.add_cascade(label = "File", menu = filemenu)
        filemenu.add_command(label = "New", command = self.createNewFile)
        filemenu.add_command(label = "Open", command = self.openFile)
        filemenu.add_command(label = "Save", command = self.saveFile)
        #menu option2
        appmenu = Menu(menubarX, tearoff = 0)
        menubarX.add_cascade(label = "App", menu = appmenu)
        appmenu.add_command(label = "Switch theme to classic", command = self.classicTheme)
        appmenu.add_command(label = "Switch theme to default", command = self.defaultTheme)
        appmenu.add_command(label = "About Xtic Pad", command = self.aboutInfo)
        appmenu.add_command(label = "Close this window", command = window.quit)
        #popup menus
        self.popupmenu1 = Menu(window, tearoff=0)
        self.popupmenu1.add_command(label = "Copy", command = self.copyClipboard)
        self.popupmenu1.add_command(label = "Paste", command = self.pasteClipboard)
        self.popupmenu1.add_command(label = "Save", command = self.saveFile)

        #Create widgets
        xticImg = PhotoImage(file="Xtic2.png")
        self.labelXtic = Label(window, height = 50, width = 20, image = xticImg, bg="maroon", text = "Xtic")
        self.labelFileName = Label(window, text = self.fileX, width = 62, bg = "white")
        self.labelFileName.configure(font=(tkinter.font.Font(family ="courier", size = 10, weight="bold")))
        self.txtFrame = Frame(window)
        self.scrollbar = Scrollbar(self.txtFrame)
        self.text = Text(self.txtFrame, height = 25, width = 60, wrap = WORD, relief = GROOVE, yscrollcommand = self.scrollbar.set)
        self.text.configure(font=(tkinter.font.Font(family ="Verdana", size = 10, weight="normal")))
        self.labelXtic.pack(fill=BOTH)
        self.labelFileName.place(x=7, y=60)
        self.txtFrame.place(x=7, y=85)
        self.scrollbar.pack(side = RIGHT, fill = Y)
        self.scrollbar.config(command = self.text.yview)
        self.text.pack()
        self.text.bind("<Button-3>", self.popup1)
        window.mainloop()

    def openFile(self):
        try:
            self.createNewFile()
            self.fileX = askopenfilename() 
            self.labelFileName.config(text= self.fileX.replace("/", ">"))
            inputFile = open(self.fileX , "r")
            self.text.insert(END, inputFile.read())
            self.initialRead = inputFile.read()
            inputFile.close()   
        except UnicodeDecodeError:
            tkinter.messagebox.showerror("Xtic Pad", "This file type cannot be opened with Xtic pad\nXtic pad V1.0.1 opens only textual file formats")
            self.labelFileName.config(text= "")
        except FileNotFoundError:
            pass
        except:
            tkinter.messagebox.showerror("Xtic Pad", "There was an issue")


    def saveFile(self):
        fileText = self.text.get("1.0",END)
        if os.path.isfile(self.fileX): 
            existingFile = open(self.fileX, "w")  
            existingFile.write(fileText)
            existingFile.close()
        else:
            fileNameToSave = asksaveasfilename()
            self.labelFileName.config(text= fileNameToSave.replace("/", ">"))
            self.fileX = fileNameToSave 
            newFile = open(fileNameToSave, "w")  
            newFile.write(fileText)
            newFile.close()

    def clearAll(self):
        self.text.delete("1.0","end")
        self.labelFileName.config(text="")
        self.fileX = ""

    def createNewFile(self):
        textCheck = self.text.get("1.0","end")
        LengthTC = len(textCheck)
        if LengthTC > 4:
            yesOrNo = tkinter.messagebox.askyesno("Exiting current File", "You're about to exit Current File, do you wish to save")
            if yesOrNo == True:
                self.saveFile()
            self.clearAll()
        else:
            self.clearAll()

    def popup1(self, event):
        self.popupmenu1.post(event.x_root, event.y_root)
        
    def copyClipboard(self):
        self.copiedData = self.text.selection_get() 
        self.window.clipboard_clear()
        self.window.clipboard_append(self.copiedData)

    def pasteClipboard(self):
        data = self.window.clipboard_get()
        self.text.insert(END, data)

    def aboutInfo(self):
        tkinter.messagebox.showinfo("Xtic Pad","Xtic File Editor\nVersion 1.0.1\nDesigned by OBJ\n\
        ©OBJ PRIME\n\nXtic can be used to read textual files like .txt \nIt doesn't read binary file like .docx .jpg .png\
        \nFuture versions will be equipped with these capabilities")

    def classicTheme(self):
        self.window.config(bg = "light gray")
        self.labelXtic.config(bg = "light gray")

    def defaultTheme(self):
        self.window.config(bg = "maroon")
        self.labelXtic.config(bg = "maroon")

XticFileEditor()       

