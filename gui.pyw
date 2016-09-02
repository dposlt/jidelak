# -*- coding: cp1250 -*-

from Tkinter import *
import time as time
import win32clipboard, win32con, os
class App:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()
        
        self.text = StringVar()
        self.lbl = Label(frame,textvariable=self.text, fg="black", width=21, height=1, anchor=W)
        self.text.set(u"Vyberte jedno z tlačítek")
        self.lbl.pack(side=BOTTOM,padx=5, pady=5)
        
        self.pdf = Button(frame, text="PDF", fg="blue",width=10, command=self.pdf)
        self.pdf.pack(side=LEFT,padx=5, pady=5)
        
        self.export = Button(frame, text="Export HTML",width=10, fg="blue",command=self.export)
        self.export.pack(side=LEFT,padx=5, pady=5)

        
        self.end = Button(frame, text="KONEC", fg="red",width=10,command=master.destroy)
        self.end.pack(side=LEFT,padx=5, pady=5)

    def export(self):
        import export
        
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_TEXT, export.prevodHtml())
        win32clipboard.CloseClipboard()
        time.sleep(.5)
        self.text.set(u"Převod do HTML dokončen")
        
        import webbrowser
        new = 2
        url="http://www.uziznivehojelena.cz/nahrani-dat"
        webbrowser.open(url,new=new)
        

    def pdf(self):
        try:
            import word
            word.createPdf()
            self.text.set(u"PDF exportováno a připraveno")
            os.startfile(word.name())
        except:
            self.text.set(u'PDF soubor je již otevřen')
        

if __name__ == "__main__":
    root = Tk()
    root.option_add('*Font','Vernada 10')
    root.resizable(width=False, height=False)
    root.title("Jídelak")
    app = App(root)
    root.mainloop()
