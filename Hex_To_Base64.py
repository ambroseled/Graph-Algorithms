#Converting Hexidecimal to Base 64


class Hex_to_64(object):
    """Convert Hex to Base 64"""


    def __init__(self):
        """Intial data input"""
        self.hex = input("Enter Hexidecimal: ")
        self.Base64 = ''
        self.hex_val = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6,
        '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15,
        'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
        self.bin_val = {0:'0000', 1:'0001', 2:'0010', 3:'0011', 4:'0100', 5:'0101', 6:'0110',
        7:'0111', 8:'1000', 9:'1001', 10:'1010', 11:'1011', 12:'1100', 13:'1101', 14:'1110', 15:'1111'}
        self.bin = ''
        self.Base_val = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L',
        12:'M', 13:'N', 14:'O', 15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X', 24:'Y',
        25:'Z', 26:'a', 27:'b', 28:'c', 29:'d', 30:'e', 31:'f', 32:'g', 33:'h', 34:'i', 35:'j', 36:'k', 37:'l',
        38:'m', 39:'n', 40:'o', 41:'p', 42:'q', 43:'r', 44:'s', 45:'t', 46:'u', 47:'v', 48:'w', 49:'x', 50:'y',
        51:'z', 52:'0', 53:'1', 54:'2', 55:'3', 56:'4', 57:'5', 58:'6', 59:'7', 60:'8', 61:'9', 62:'+', 63:'/'}
        self.bin_conversions = {5:1, 4:2, 3:4, 2:8, 1:16, 0:32}


    def hex_to_bin(self):
        """Converting Hexidecimal to Binary"""
        for char in self.hex:
            base_10 = self.hex_val[char]
            bin_val = self.bin_val[base_10]
            self.bin += bin_val


    def bin_decimal(self, bin_str):
        """Converting binary to decimal"""
        total = 0
        for index, char in enumerate(bin_str):
            if char == '1':
                total += self.bin_conversions[index]
        return total


    def bin_to_64(self):
        """converting Binary to Base 64"""
        temp_bin = ''
        for char in self.bin:
            temp_bin += char
            if len(temp_bin) == 6:
                decimal = self.bin_decimal(temp_bin)
                temp_bin = ''
                self.Base64 += self.Base_val[decimal]


    def hex_64(self):
        """Converting Hexidecimal to Base 64"""
        self.hex_to_bin()
        self.bin_to_64()


def main():
    """Runing converter"""

    convert = Hex_to_64()
    convert.hex_64()
    print(convert.Base64)

main()
