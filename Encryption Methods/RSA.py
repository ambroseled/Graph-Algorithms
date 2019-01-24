#Code to encrypt using a RSA cipher


#Importing lib
import sympy
import random


class RSA_cipher(object):
    """class which is used for RSA encryption"""


    def __init__(self):
        """Intialize data needed to do Affine encryption"""
        self.z_26 = list(range(0,26)) #Vaible to hold value of z 26
        self.letters = ['A','B','C','D','E','F','G','H','I','J','K','L',
        'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] #Vaiable to hold plain alphabet
        self.plain_text = '' #Initalizing variable to hold plain text
        self.cipher_text = '' #Intializing varible to hold cipher text
        self.p = 0 #Intializing vairble to hold p
        self.q = 0 #Intializing variable to hold q
        self.phi = 0 #Intializing variable to hold phi
        self.d = 0 #Intializing variable to hold d
        self.e = 0 #Intializing variable to hold e


    def inputs(self):
        """Gathering input data"""
        self.plain_text = input("Enter plain text: ") #Inputing plain text
        self.plain_text.replace(' ', '') #Removing spaces from plain text
        self.p = int(input("Enter value of p: ")) #Inputing q
        self.q = int(input("Enter value of q: ")) #Inputing q
        self.phi = (self.p - 1) * (self.q - 1) #Calculating phi
        self.Check_Nums() #Checking numbers are acceptable
        self.n = self.p * self.q #Calulating n


    def Check_Nums(self):
        """Checking Numbers are correct"""
        if not sympy.isprime(self.p): #Checking p is prime
            self.p = int(input("Enter value of p: ")) #Re-inputting p
            self.Check_Nums() #Checking numbers


        if not sympy.isprime(self.q): #Checking q is prime
            self.q = int(input("Enter value of q: ")) #Re-inputting q
            self.Check_Nums() #Checking numbers


        if self.p == self.q: #Making sure p and q are not equal
            self.p = int(input("Enter value of p: ")) #Re-inputting p
            self.q = int(input("Enter value of q: ")) #Re-inputting q
            self.Check_Nums() #Checking numbers


    def gcd(self, a, b):
        """finding the greatest common demnomator"""
        while b != 0: #Looping until b is 0
            a, b = b, a % b #Getting new value of a and b
        return a #Returning a


    def get_inverse(self):
        """Getting inverse of e in z(phi)"""
        d = 0 #Intializing inverse variable
        x1 = 0 #Temp variable 1
        x2 = 1 #Temp variable 2
        y1 = 1 #Temp variable 3
        temp_phi = self.phi #Temp phi varaible
        temp_e = self.e #Temp e variable


        while temp_e > 0: #Looping while e is greater than 0
            temp1 = temp_phi/temp_e
            temp2 = temp_phi - temp1 * temp_e
            temp_phi = temp_e
            temp_e = temp2
            x = x2 - temp1* x1
            y = d - temp1 * y1
            x2 = x1
            x1 = x
            d = y1
            y1 = y


        if temp_phi == 1:
            return d + phi #Returning inverse


    def get_key(self):
        """Getting key"""
        self.e = random.randrange(1, self.phi) #Getting random value in Z_phi
        g = self.gcd(self.e, self.phi) #Gettign gcd of e and phi


        while g != 1: #Getting new e until the gcd is 1
            self.e = random.randrange(1, self.phi)
            g = self.gcd(self.e, self.phi)
        self.d = self.get_inverse() #Getting inverse


    def encrypt(self):
        """Convert each letter in the plaintext to numbers based on the character using a^b mod m"""
        """Need to convert whole text to numbers then split into groups"""
        #enciphered = [(ord(char) ** self.e) % self.n for char in self.plain_text] #Encrypting plain text
        #for num in enciphered: #Lopping through list of
        #    num_str = str(num)
        #    if len(num_str) == 1:
        #        num_str = '0' + num_str
        #    self.cipher_text += num_str


def main():
    """Running class"""
    cipher = RSA_cipher() #Creating instance of the RSA class
    cipher.inputs() #Getting inout values
    cipher.get_key() #Creating key
    cipher.encrypt() #Encrypting plain text

    
    print("{0} encrypted to {1} with a public key of {2}".format(cipher.plain_text, cipher.cipher_text, (cipher.n, cipher.e))) #Outputing data
