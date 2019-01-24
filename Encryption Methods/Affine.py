#Code to encrypt and decrypt using a Affine cipher


class Affine_crypt(object):
    """class which is used for affine encryption"""


    def __init__(self):
        """Intialize data needed to do Affine encryption"""
        self.z_26 = list(range(0,26)) #Initalizing list with all values of z 26
        self.letters = ['A','B','C','D','E','F','G','H','I','J','K','L',
        'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] #List holding the alphabet
        self.choice = 1 #Inital varible choice
        self.plain_text = '' #Initlaizing plain text to empty string
        self.cipher_text = '' #Intializing cipher text to empty string
        self.b = -1 #Initalizing vaiable to hold b
        self.a = 0  #Intializing variable to hold a
        self.invertible = [1,3,5,7,9,11,15,17,19,21,23,25] #List of invertible elements in z26
        self.inverses = [1,9,21,15,3,19,7,23,11,5,17,25] #Inverse of all invertible elements in z 26


    def get_encrypted_letters(self):
        """Creates list of the encrypted letters"""
        self.encrypted_letters = [0]*26 #Intializing empty list to hold cipher alphabet
        self.encrypted_letters = [self.letters[(i*self.a + self.b) % 26] for i in range(len(self.letters) - 1)]
        #Getting the cipher alphabet


    def encrypt(self):
        """General encryption function handles a sentence of words"""
        self.encrypt_count = 0 #Intializing encyption count
        words = self.plain_text.split() #Spliting plain text into words
        for word in words: #Looping through words
            self.cipher_text += self.encrypt_word(word) #Encrypting word and adding to cipher text


    def encrypt_word(self, word):
        """Encrypts given plain text"""
        self.get_encrypted_letters() #Gettign cipehr alphabet
        cipher_word = '' #Intializing variable to hold enciphered word
        for i in range(len(word)): #Looping through word
            index = self.letters.index(word[i]) #Getting encrypted letter
            cipher_word += self.encrypted_letters[index] #Adding encrypted letter to cipehr word
            #print("Encryption step {0} cipher text so far: {1}{2}".format(self.encrypt_count, self.cipher_text, cipher_word))
            self.encrypt_count += 1 #Incrementing encryption count
        return cipher_word #Returning encrypted word


    def brute_decrypt(self):
        """Brute force method of decryption"""
        decrypted = [] #Intializing list to hold all possible decryptions
        a_b = [] #Intializing list to hold key
        self.decrypt_count = 0 #Intializing decryption count
        words = self.cipher_text.split() #Spliting cipher text into a list of words
        for b in self.z_26: #Looping thorugh possbile vaules of b
            for a in self.invertible: #Looping through possible values of a
                plain_text = '' #Plain text variable
                a_index = self.invertible.index(a) #Getting index to gain inverse
                a_inv = self.inverses[a_index] #Getting inverse of a
                for word in words: #Looping thorugh words
                    for j in range(len(word)): #Looping through letters in word
                        index = self.letters.index(word[j]) #Getting index of letter
                        decrypt_index = (a_inv*(index - b)) % 26 #Getting index of letter
                        plain_text += str(self.letters[decrypt_index]) #Adding letter to plain text
                        self.decrypt_count += 1 #Incrementing decryption count
                decrypted.append(plain_text) #Appending plain text list of all decryptions
                a_b.append((a,b)) #Adding key to llist of all keys
        """
        #Uncomment if using without GUI
        for index, text in enumerate(decrypted): #Looping through all decryptions to output
            nums = a_b[index] #Getting key
            a = nums[0] #Getting a value
            b = nums[1] #Getting b value
            print("a of {0} and b of {1} decrypts to {2}".format(a, b, text))
        """

        return decrypted, a_b #Returning all decryptions and keys


def main():
    """runs the encryption/decryption"""
    cipher = Affine_crypt()
    if cipher.choice == 1:
        a_valid = False
        cipher.a = int(input("Enter value of a: "))
        while not a_valid:
            if cipher.a in cipher.invertible:
                a_valid = True
            else:
                cipher.a = int(input("Enter new value of a: "))
        cipher.b =  int(input("Enter value of b: "))
        original_text = raw_input("Enter plain text: ")
        cipher.plain_text = original_text.upper()
        cipher.encrypt()
        print("{0} encrypts to {1} using a key of {2}, {3} steps were taken to encrypt the text".format(original_text,
        cipher.cipher_text, cipher.b, cipher.encrypt_count))
        print('----------------------------------')
    elif cipher.choice == 0:
        cipher.cipher_text = raw_input("Enter cipher text: ").upper()
        decrypted, a_b = cipher.brute_decrypt()
        a = int(input('Select correct a: '))
        b = int(input('Select correct b: '))
        index = a_b.index((a,b))
        plain_text = decrypted[index]
        print("{0} dencrypts to {1} encryption key was ({2},{3}), {4} steps were taken to decode the text".format(cipher.cipher_text.lower(),
        plain_text.lower(), a, b, cipher.decrypt_count))
