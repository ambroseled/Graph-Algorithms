#GUI menu combining all ciphers


#importing all required librays
from tkinter import *
from PIL import Image, ImageTk
import subprocess
import os
from os import system as cmd


#importing crypto methods from other files
from Ceasar import *
from Affine import *
from RSA import *


class Window(Frame):


    def __init__(self, master=None):
        """GUI Intialization"""
        Frame.__init__(self, master)
        self.master = master
        self.init_window()


    def init_window(self):
        """Setting up window"""
        self.master.title("Crypto ciphers")
        self.pack(fill=BOTH, expand=1)


        #Seting up menu
        menu = Menu(self.master)
        self.master.config(menu=menu)
        #Adding file tab to menu
        file = Menu(menu)
        #Adding exit to file tab
        file.add_command(label="Exit", command=self.quit)
        menu.add_cascade(label="File", menu=file)
        #Adding edit tab to menu
        edit = Menu(menu)
        #Adding show image to edit tab
        edit.add_command(label="Show Img", command=self.showPepe)
        menu.add_cascade(label="Edit", menu=edit)


        #Adding Drop Menu for Encrypt/Decrypt option
        self.Drop_var = StringVar()
        self.Drop_Menu = OptionMenu(self.master, self.Drop_var, "Encrypt", "Decrypt")
        self.Drop_Menu.place(x=65, y=70, width=100)
        #Adding label for drop down menu
        Drop_Lab = Label(self.master, text='Select Encryption or Decryption')
        Drop_Lab.place(x=20, y=50)


        #Adding title
        title = Label(self.master, text='Cryptography Ciphers GUI')
        title.place(x=200, y=20)


        #Adding drop menu for selection of cipher
        self.Drop_var_2 = StringVar()
        self.Drop_Menu_2 = OptionMenu(self.master, self.Drop_var_2, "Caesar", "Affine", "RSA", "KeyWord")
        self.Drop_Menu_2.place(x=400, y=70, width=100)
        #Adding label for drop down menu
        Drop_Lab_2 = Label(self.master, text='Select Cipher')
        Drop_Lab_2.place(x=403, y=50)


        #Adding Enter/Selection Button
        select_button = Button(self.master, text='Enter Selection', command=self.handle_drops)
        select_button.place(x=225, y=70)



    def handle_drops(self):
        """Handle info from drop menus"""
        #Gathering info from both drop menus
        self.cipher = self.Drop_var_2.get()
        self.crypt = self.Drop_var.get()


        #Handle when encryption method is Caesar
        if self.cipher == 'Caesar':
            self.Handle_Caesar()


        #Handle when encryption method is Affine
        elif self.cipher == 'Affine':
            self.Handle_Affine()


        #Handle when encryption method is RSA
        elif self.cipher == 'RSA':
            self.Handle_RSA()


        #Handle when encryption method is Keyword
        elif self.cipher == 'keyWord':
            self.Handle_KeyWord()


    def Handle_Caesar(self):
        """Handling Caesar cipher"""
        #Creating instance of Caesar_crypt class
        self.cipher = Caesar_crypt()

        #Handling when choice is encryption
        if self.crypt == 'Encrypt':
            #Text entry to gain plain text
            self.Caesar_text_entry = Entry(self.master)
            self.Caesar_text_entry.pack()
            self.Caesar_text_entry.place(x=65, y=150, width=150)
            #Label for text entry to gain plain text
            self.Caesar_text_entry_label = Label(self.master, text='Enter plain text')
            self.Caesar_text_entry_label.place(x=73, y=130)


            #Text entry to gain key
            self.Caesar_key_entry = Entry(self.master)
            self.Caesar_key_entry.insert(END, 1)
            self.Caesar_key_entry.pack()
            self.Caesar_key_entry.place(x=365, y=150, width=150)
            #Label for text entry to gain key
            self.Caesar_key_entry_label = Label(self.master, text='Enter key value')
            self.Caesar_key_entry_label.place(x=365, y=130)


            #Button to encrypt
            self.Caesar_encrypt_button = Button(self.master, text='Encrypt', command=self.Encrypt_caesar)
            self.Caesar_encrypt_button.place(x=250, y=150)


        #Handling when choice is decryption
        else:
            #Text entry to gain cipher text
            self.Caesar_text_entry = Entry(self.master)
            self.Caesar_text_entry.pack()
            self.Caesar_text_entry.place(x=65, y=150, width=150)
            #Label for text entry to gain cipher text
            self.Caesar_text_entry_label = Label(self.master, text='Enter cipher text')
            self.Caesar_text_entry_label.place(x=73, y=130)


            #Text entry to gain key
            self.Caesar_key_entry = Entry(self.master)
            self.Caesar_key_entry.insert(END, '-')
            self.Caesar_key_entry.pack()
            self.Caesar_key_entry.place(x=365, y=150, width=150)
            #Label for text entry to gain key
            self.Caesar_key_entry_label = Label(self.master, text="Enter key value('-' if not known)")
            self.Caesar_key_entry_label.place(x=365, y=130)


            #Button to decrypt
            self.Caesar_decrypt_button = Button(self.master, text='Decrypt', command=self.Decrypt_caesar)
            self.Caesar_decrypt_button.place(x=250, y=150)


    def Encrypt_caesar(self):
        """Encrypting given plain text"""
        #Gathering data from drop menus
        self.cipher.plain_text = self.Caesar_text_entry.get().upper()
        self.cipher.b = int(self.Caesar_key_entry.get())


        #Encrypting plain text
        self.cipher.encrypt()
        #Outputing data from encryption
        self.Caesar_output = Text(self.master, height=5)
        self.Caesar_output.insert(1.0, "{0} encrypts to {1} using a key of {2}, {3} steps were taken to encrypt the text".format(self.cipher.plain_text.lower(),
        self.cipher.cipher_text, self.cipher.b, self.cipher.encrypt_count))
        self.Caesar_output.place(x=10,y=220)


        #Making button to claer window after encryption
        self.Caesar_clear_button = Button(self.master, text='Reset', command=self.Clear_encrypt_Cea)
        self.Caesar_clear_button.place(x=255, y=175)


    def Clear_encrypt_Cea(self):
        """Reseting Widget after Encrypt"""
        #Removing all widgets used in the encryption to reset GUI
        self.Caesar_text_entry.destroy()
        self.Caesar_text_entry_label.destroy()
        self.Caesar_key_entry.destroy()
        self.Caesar_key_entry_label.destroy()
        self.Caesar_encrypt_button.destroy()
        self.Caesar_clear_button.destroy()
        self.Caesar_output.destroy()


    def Decrypt_caesar(self):
        """Decrypting given cipher text"""
        #Gathering data from text entries
        self.cipher.cipher_text = self.Caesar_text_entry.get().upper()
        self.cipher.b = self.Caesar_key_entry.get()


        #Checking if the key for decrpytion is known
        #Goes into this statement if b is not known
        if self.cipher.b == '-':
            """Using brute force decryption method"""
            try:
                #Key for decryption is not known
                #Decrypting cipher text
                plain_text = self.cipher.decrypt()


                #Outputing result of decryption
                self.Caesar_output = Text(self.master, height=5)
                self.Caesar_output.insert(1.0, "{0} decrypts to {1}, encryption key was {2}, {3} steps were taken to decode the text".format(self.cipher.cipher_text.lower(),
                plain_text.lower(), self.cipher.b, self.cipher.decrypt_count))
                self.Caesar_output.place(x=10,y=220)


            except TypeError:
                """Catching bug in decryption"""
                #Current dictioanry library finds some words as english which actually aren't english
                #This causes errors, using a try, except until bug is fixed


                """Need to fix dis shit reeeeeee"""


                #Gathering all possible decryptions
                self.Decryp_list = self.cipher.brute_decrypt()


                #Adding button to enter selection of correct plain text
                self.Caesar_Menu_enter = Button(self.master, text='Enter', command=self.Enter_brute_Ce)
                self.Caesar_Menu_enter.place(x=260, y=200)


                #adding drop menu holding all possible decryptions
                self.Caesar_Brute_var = StringVar()
                self.Caesar_Brute_Menu = OptionMenu(self.master, self.Caesar_Brute_var, *self.Decryp_list)
                self.Caesar_Brute_Menu.place(x=220, y=225, width=140)


        #b is known so decryption is simple
        else:
            """B is known so the cipher can be easily decrypted"""
            #ket for encryption is known
            #Convering key to an interger
            self.cipher.b = int(self.cipher.b)


            #Splitting plain text into a list of words
            words = self.cipher.cipher_text.split()

            #Intializing plain text variable
            plain_text = ''
            for word in words:
                #Decrytping each word
                plain_text += self.cipher.decrypt_known_b(word, self.cipher.b) + ' '


            #Outputing result of decryption
            self.Caesar_output = Text(self.master, height=5)
            self.Caesar_output.insert(1.0, "{0} decrypts to {1}, encryption key was {2}, {3} steps were taken to decode the text".format(self.cipher.cipher_text.lower(),
            plain_text.lower(), self.cipher.b, len(words)))
            self.Caesar_output.place(x=10,y=220)


        #adding button to clear widgets and reset GUI
        self.Caesar_finish_button = Button(self.master, text='Clear Widgets', command=self.Clear_widgets)
        self.Caesar_finish_button.place(x=232, y=175)


    def Enter_brute_Ce(self):
        """Getting value from menu for a brute force decryption"""
        #Getting correct plain text
        plain_text = self.Brute_var.get()


        #Outputing data from brute force decryption
        self.Caesar_output = Text(self.master, height=5)
        self.Caesar_output.insert(1.0, "{0} decrypts to {1}, encryption key was {2}".format(self.cipher.cipher_text.lower(), plain_text.lower(), self.Decryp_list.index(plain_text)))
        self.Caesar_output.place(x=10,y=260)


    def Clear_widgets(self):
        """Clearing widgets after decryption"""
        #Clearing all eidgets from GUI
        self.Caesar_text_entry.destroy()
        self.Caesar_text_entry_label.destroy()
        self.Caesar_key_entry.destroy()
        self.Caesar_key_entry_label.destroy()
        self.Caesar_encrypt_button.destroy()
        self.Caesar_finish_button.destroy()
        self.Caesar_output.destroy()
        self.Caesar_decrypt_button.destroy()



    def Handle_Affine(self):
        """Handling Affine cipher"""
        #Creating new instance of the Affine_crypt class
        self.cipher = Affine_crypt()


        #Checking if choice was encryption or decryption
        if self.crypt == 'Encrypt':


            #Text entry to gain plain text
            self.text_entry = Entry(self.master)
            self.text_entry.pack()
            self.text_entry.place(x=65, y=150, width=150)


            #Label for text entry to gain plain text
            self.text_entry_label = Label(self.master, text='Enter plain text')
            self.text_entry_label.place(x=73, y=130)


            #Text entry to gain key
            self.key_a_entry = Entry(self.master)
            self.key_a_entry.insert(END, '1')
            self.key_a_entry.pack()
            self.key_a_entry.place(x=365, y=150, width=150)
            #Label for text entry to gain key
            self.key_a_entry_label = Label(self.master, text='Enter value of a')
            self.key_a_entry_label.place(x=365, y=130)


            #Text entry to gain key
            self.key_b_entry = Entry(self.master)
            self.key_b_entry.insert(END, '1')
            self.key_b_entry.pack()
            self.key_b_entry.place(x=215, y=150, width=150)
            #Label for text entry to gain key
            self.key_b_entry_label = Label(self.master, text='Enter value of b')
            self.key_b_entry_label.place(x=215, y=130)


            #Button to check a and b are invertible
            self.invert_button = Button(self.master, text='Check invertible', command=self.Check_invert)
            self.invert_button.place(x=225, y=205)


            #Button to start affine encryption
            self.encrypt_button = Button(self.master, text='Encrypt', command=self.Encrypt_Affine)
            self.encrypt_button.place(x=250, y=180)


        #Choice is decryption
        else:
            #Text entry to gain cipher text
            self.text_entry_aff = Entry(self.master)
            self.text_entry_aff.pack()
            self.text_entry_aff.place(x=65, y=150, width=130)
            #Label for text entry to gain cipher text
            self.text_entry_aff_label = Label(self.master, text='Enter cipher text')
            self.text_entry_aff_label.place(x=73, y=130)


            #Text entry to gain a
            self.key_entry_a = Entry(self.master)
            self.key_entry_a.insert(END, '-')
            self.key_entry_a.pack()
            self.key_entry_a.place(x=231, y=150, width=110)
            #Label for text entry to gain a
            self.key_entry_a_label = Label(self.master, text="Enter value of a\n('-' if not known)")
            self.key_entry_a_label.place(x=230, y=110)


            #Text entry to gain b
            self.key_entry_b = Entry(self.master)
            self.key_entry_b.insert(END, '-')
            self.key_entry_b.pack()
            self.key_entry_b.place(x=400, y=150, width=110)
            #Label for text entry to gain b
            self.key_entry_b_label = Label(self.master, text="Enter valueof b\n('-' if not known)")
            self.key_entry_b_label.place(x=400, y=110)


            #Button to decrypt
            self.decrypt_button = Button(self.master, text='Decrypt', command=self.Decrypt_affine)
            self.decrypt_button.place(x=250, y=180)


    def Check_invert(self):
        """Cheching that the a and b entered will cause a permutaion"""
        #Gathering value of a to check if it is invertible
        self.cipher.a = self.key_a_entry.get()



        """
        DO THIS SHIT
        """



    def Encrypt_Affine(self):
        """Encrypting given plain text"""
        #Gathering data from text entries
        self.invert_button.destroy()
        self.cipher.plain_text = self.text_entry.get().upper()
        self.cipher.a = int(self.key_a_entry.get())
        self.cipher.b = int(self.key_b_entry.get())


        #Encrypting plain text
        self.cipher.encrypt()


        #Outputing data from encryption
        self.output = Text(self.master, height=5)
        self.output.insert(1.0, "{0} encrypts to {1} encryption key was ({2},{3}".format(
        self.cipher.plain_text.lower(), self.cipher.cipher_text, self.cipher.a, self.cipher.b))
        self.output.place(x=10,y=250)


        #Making button to claer window after encryption
        self.clear_button = Button(self.master, text='Reset', command=self.Clear_encrypt_aff)
        self.clear_button.place(x=255, y=205)



    def Clear_encrypt_aff(self):
        """Clearing widgets"""
        #Clearing widgets to reset GUI
        self.clear_button.destroy()
        self.output.destroy()
        self.encrypt_button.destroy()
        self.invert_button.destroy()
        self.key_b_entry.destroy()
        self.key_b_entry_label.destroy()
        self.key_a_entry.destroy()
        self.key_a_entry_label.destroy()
        self.text_entry.destroy()
        self.text_entry_label.destroy()


    def Decrypt_affine(self):
        """Handling decryption of an affine cipher"""
        #Getting input values
        self.cipher.cipher_text = self.text_entry_aff.get()
        self.a = self.key_entry_a.get()
        self.b = self.key_entry_b.get()
        if self.a == '-' or self.b == '-':
            self.decrypted, self.a_b = self.cipher.brute_decrypt()
            #Adding button to enter selection of correct plain text
            self.Aff_Menu_enter = Button(self.master, text='Enter', command=self.Enter_brute_aff)
            self.Aff_Menu_enter.place(x=257, y=205)


            #adding drop menu holding all possible decryptions
            self.Aff_Brute_var = StringVar()
            self.Aff_Brute_Menu = OptionMenu(self.master, self.Aff_Brute_var, *self.decrypted)
            self.Aff_Brute_Menu.place(x=228, y=230, width=120)

#NKRRU
    def Enter_brute_aff(self):
        """Handling output for result of a brute force decryption of an Affine cipher"""
        plain_text = self.Aff_Brute_var.get()
        index = self.decrypted.index(plain_text)
        key = self.a_b[index]
        #Outputing data from encryption
        self.output_aff = Text(self.master, height=5)
        self.output_aff.insert(1.0, "{0} encrypts to {1} encryption key was {2}".format(
        plain_text, self.cipher.cipher_text, key))
        self.output_aff.place(x=10,y=275)


        #Making button to claer window after encryption
        self.clear_decrypt_aff = Button(self.master, text='Reset', command=self.Clear_decrypt_aff)
        self.clear_decrypt_aff.place(x=257, y=255)


    def Clear_decrypt_aff(self):
        """Reseting window"""
        self.clear_decrypt_aff.destroy()
        self.output_aff.destroy()
        self.Aff_Brute_Menu.destroy()
        self.Aff_Menu_enter.destroy()
        self.key_entry_a.destroy()
        self.key_entry_b.destroy()
        self.key_entry_a_label.destroy()
        self.key_entry_b_label.destroy()
        self.decrypt_button.destroy()
        self.text_entry_aff.destroy()
        self.text_entry_aff_label.destroy()

    def Handle_RSA(self):
        """Handling RSA cipher"""




    def Handle_KeyWord(self):
        """Handling KeyWord cipher"""




    def showPepe(self):
        """Event handling for show image tab"""


        #Loading image
        load = Image.open("980x.jpg")
        render = ImageTk.PhotoImage(load)

        #Labeling image
        img = Label(self, image=render)
        img.image = render
        img.place(x=80, y=0)


    def quit(self):
        """Event handling for quit tab"""
        exit()

root = Tk()
root.geometry("600x400")
app = Window(root)
root.mainloop()
