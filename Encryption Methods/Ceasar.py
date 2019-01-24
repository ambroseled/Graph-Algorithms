#Code to encrypt and decrypt using a Ceaser cipher
import enchant

class Caesar_crypt(object):
    """class which is used for caesar encryption"""


    def __init__(self):
        """intialize data needed to do ceasar encryption"""
        self.z_26 = list(range(0,26)) #Defining numbers in z26
        self.letters = ['A','B','C','D','E','F','G','H','I','J','K','L',
        'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] #Defining letters of the alphabet
        self.choice = '' #Initalizing choice variable
        self.plain_text = '' #Initalizing variable for plain text
        self.cipher_text = '' #Initalizing variable for cipher text
        self.b = -1 #Setting inital value of b


    def get_encrypted_letters(self):
        """creates list of the encrypted letters"""
        self.encrypted_letters = [0]*26 #Initalizing empty list to hold encrypted letters
        #for i in range(len(self.letters) - 1): #looping through letters to be encrypted
        #    index = (i + self.b) % 26 #Finding new index for encrypted letter
        #    self.encrypted_letters[i] = self.letters[index] #Adding encrypted leeter to list
        self.encrypted_letters = [self.letters[(i+self.b)%26] for i in range(len(self.letters) - 1)]


    def encrypt(self):
        """general encryption function handles a sentence of words"""
        self.encrypt_count = 0 #Initalizing encryption count
        words = self.plain_text.split() #Splitting plain text into words
        for word in words: #Looping through words in plain text to encrypt
            self.cipher_text += self.encrypt_word(word) #Calling encrypt word then adding to cipher text


    def encrypt_word(self, word):
        """encrypts given plain text"""
        self.get_encrypted_letters() #Encrypting letters
        cipher_word = '' #Varibale to hold encrypted word
        for i in range(len(word)): #Looping through each letter of word
            index = self.letters.index(word[i]) #Get index of letter in alphabet
            cipher_word += str(self.encrypted_letters[index]) #Get encrypted letter and add to cipher word
            self.encrypt_count += 1 #Incrementing encryption count

        return cipher_word #Returning encrypted word


    def decrypt(self, remove_b=None):
        """genral decryption function handles sentence of encrypted words"""
        self.decrypt_count = 0 #Intializing decryption count
        words = self.cipher_text.split() #Splitting cipher text into words
        if len(words) == 1: #Handling edge case if cipher text is only one word
            self.plain_text = self.decrypt_word(self.cipher_text) #Encrypting word

        else: #Handling case where cipher text is more than one word long
            first_word = words[0] #Gathering first word to be encrypted
            self.plain_text = self.decrypt_word(first_word, remove_b) + ' ' #Adding decrypted word to plain text
            test_b = self.b #Gathering b to be tested
            if self.test_decrypt(test_b): #Current b is accpeted and the rest of the cipher text is decrypted
                for word in words[1:]: #Looping through words to be decrypted
                    self.plain_text += self.decrypt_known_b(word, test_b) + ' ' #Decrypting each word

                return self.plain_text #Returning plain text

            else: #Current b failed and a new one must be found
                remove_b = test_b #Marking current b as wrong
                self.plain_text = '' #Resting plain text
                return self.decrypt(remove_b) #Redoing decryption function

        return self.plain_text #Returning plain text


    def test_decrypt(self, test_b):
        """test a found b on all other words given to decrypt"""
        plain_text = '' #Initalizing plain text to be used for test
        dic = enchant.Dict("en_GB") #Getting dictionary to test words
        words = self.cipher_text.split() #Splitting cipher text into words
        words = words[1:] #Removing first word as it has already been decrypted
        passed = True #Initalizing boolean variable for test
        for word in words: #Looping through words in cipher text
            word = word.upper() #Setting word to upper case
            for j in range(len(word)): #Looping through letters in word
                index = (self.letters.index(word[j]) - test_b) % 26 #Decrypting letter
                plain_text += str(self.letters[index]) #Adding decrypted letter to plain text

            if not dic.check(plain_text): #Checking word is English
                passed = False #Word is not in English fo passed set to false

        return passed #Returning result of test


    def decrypt_known_b(self, word, known_b):
        """decrypting a word when the b is known"""
        plain_text = '' #Intializing temp plain text to hold decryption
        for j in range(len(word)): #Looping through word
            index = (self.letters.index(word[j]) - known_b) % 26 #Decrypting letter
            plain_text += str(self.letters[index]) #Adding decrypted letter to plain text

        return plain_text #Returning plain text


    def decrypt_word(self, word, remove_b=None):
        """decrypts the givven cipher text"""
        dic = enchant.Dict("en_GB") #Setting english dictionary
        test_bs = self.z_26 #Creating list of possible b values
        if remove_b in test_bs: #Checking if a b needs to be removed
            test_bs = test_bs.remove(remove_b) #Removing failed be from list of possible b's

        if test_bs is None: #Checking if list of possible b's is empty
            return None #Returning none as there is no more b's to test

        for b in test_bs: #Looping through each b
            plain_text = '' #Setting plain text variable
            for j in range(len(word)): #Looping through word
                index = (self.letters.index(word[j]) - b) % 26 #Decrypting letter
                plain_text += str(self.letters[index]) #Adding letter to plain text
                self.decrypt_count += 1 #Incrementing decrypt count

            if dic.check(plain_text): #Checking plain text decrypting to a word in english
                break #Breaking out of loop as the word is english and correct b has been found

        self.b = b #Assigning the correct b to self.b
        return plain_text #Returning plain text


    def brute_decrypt(self):
        """Function whihc takes brute force approach to decryption"""
        decrypted = [] #Listed of the all different plain texts
        self.decrypt_count = 0 #Initalizing decryption count
        words = self.cipher_text.split() #Splitting words
        for b in self.z_26: #Looping through all possible b's
            plain_text = '' #Intializing plain text variable
            for word in words: #Looping through all words
                for j in range(len(word)): #Looping through all letters in word
                    index = (self.letters.index(word[j]) - b) % 26 #Decrypting letter
                    plain_text += str(self.letters[index]) #Adding decrypted letter to plain text
                    self.decrypt_count += 1 #Incrementing plain text

                plain_text += ' ' #Adding space after word to plain text
            decrypted.append(plain_text) #Appending plain text to list

        return decrypted #Returning list of all possible decryptions


def main():
    """runs the encryption/decryption"""
    cipher = Ceasar_crypt() #Creating instance of the Ceasar_crypt class
    cipher.choice = int(input("Enter choice for encryption(1)/decryption(0): ")) #Getting choice input
    if cipher.choice == 1: #Choice is encryption
        cipher.b =  int(input("Enter value of key: ")) #Getting choice of b
        original_text = input("Enter plain text: ") #Getting plain text
        cipher.plain_text = original_text.upper() #Changing plain text to upper case
        cipher.encrypt() #Encrypting plain text
        print("{0} encrypts to {1} using a key of {2}, {3} steps were taken to encrypt the text".format(original_text,
        cipher.cipher_text, cipher.b, cipher.encrypt_count)) #Outputing data from encyption
        print('----------------------------------') #Padding for output

    elif cipher.choice == 0: #Choice is decryption
        cipher.cipher_text = input("Enter cipher text: ").upper() #Getting cipher text
        brute = int(input("Brute force method?(Must use brute force if there are no spaces in cipher text)(1,yes): ")) #Checking for brute decryption method
        if brute == 0: #Choice was not brute decryption
            plain_text = cipher.decrypt() #Decrypting cipher text
            print("{0} decrypts to {1} encryption key was {2}, {3} steps were taken to decode the text".format(cipher.cipher_text.lower(),
            plain_text.lower(), cipher.b, cipher.decrypt_count)) #Outputing data from deccryption
            print('----------------------------------') #Padding for output

        elif brute == 1: #Choice is brute decryption
            decrypted = cipher.brute_decrypt() #Decryptingplain text

            """
            #Uncomment to use without GUI
            #for index, plain in enumerate(decrypted):
            #    print((index, plain))
            """
            b = int(input('Select correct b: ')) #Selecting which b was correct
            plain_text = decrypted[b] #Assigning plain text variable to correct decrypted plain text
            print("{0} decrypts to {1} encryption key was {2}, {3} steps were taken to decode the text".format(cipher.cipher_text.lower(),
            plain_text.lower(), b, cipher.decrypt_count)) #Outputing data from decrypt
            print('----------------------------------') #Padding for output
