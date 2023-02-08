import argparse
import os
import sys
import array
from shlex import join

# Implement the functions for encryption decryption and cryptanalysis

def main(arguments):

    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-e", "--encrypt", help="Encrypt text file", type=argparse.FileType('r'))
    parser.add_argument("-d", "--decrypt", help="Decrypt ciphertext file", type=argparse.FileType('r'))
    parser.add_argument("-s", "--shift", help="Shift value used for encryption/decryption", default=14, type=int)
    parser.add_argument("-c", "--cryptanalysis", help="Perform cryptanalysis on the given ciphertext", type=argparse.FileType('r'))

    args = parser.parse_args(arguments)

    if args.encrypt:
        shift = int(args.shift)
        #Check if shift>25 to wrap around using modulo
        if shift>25:
            shift=shift%23
            print("Wrapped around shift =",shift)
        try:
            file_content = args.encrypt.read()
            file_content=file_content.replace(" ", "") #Removing whitespace
        except:
            print("Expected non-binary file")
            exit()
        encrypted_text = ""
        #Loop through the text file
        for i in range(len(file_content)):
            char = file_content[i]
            # Encryption for special characters
            if(ord(char) in range(0,64) or ord(char)>123 or ord(char) in range(91,96)):
                encrypted_text += char
            # Encryption for Uppercase letters
            elif (char.isupper()):
                encrypted_text += chr((ord(char) + shift-65) % 26 + 65)
            # Encryption for lowercase letters
            else:
                encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        #Print the resulting encrypted text       
        print(encrypted_text)
    if args.decrypt:
        shift = int(args.shift)
        #Check if shift>25 to wrap around using modulo
        if shift>25:
            shift=shift%23
            print("Wrapped around shift =",shift)
        try:
            file_content = args.decrypt.read()
        except:
            print("Expected non-binary file")
            exit()    
        decrypted_text = ""
         #Loop through the text file
        for i in range(len(file_content)):
            char = file_content[i]
            # Decryption for special characters
            if(ord(char) in range(0,64) or ord(char)>123 or ord(char) in range(91,96)):
                decrypted_text += file_content[i]
            # Decryption for Uppercase letters
            elif (char.isupper()):
                decrypted_text += chr((ord(char) + (26-shift)-65) % 26 + 65)
            # Decryption for lowercase letters
            else:
                decrypted_text += chr((ord(char) +(26-shift) - 97) % 26 + 97)
        print(decrypted_text)
    if args.cryptanalysis:
        file_content = args.cryptanalysis.read()
        decrypted_text = ""
        #Read dictionary and format it
        dict_reader = open("../dictionary_1000.txt", "r")
        dictionary=dict_reader.read().splitlines() 
        #Set counter for occurencies
        counter=0
        newlist=[]
        for shift in range(25):
            #Decrypt for each shift
            for i in range(len(file_content)):
                char=file_content[i]
                # Encrypt uppercase characters
                if (char.isupper()):
                     decrypted_text += chr((ord(char) + (26-shift)-65) % 26 + 65)        
                # Encrypt lowercase characters
                else:
                    decrypted_text += chr((ord(char) +(26-shift) - 97) % 26 + 97)
            #Count occurencies        
            for j in range(len(dictionary)):
                if dictionary[j] in decrypted_text:
                    counter=counter+1
            #Save result        
            result=[shift,counter]
            newlist.append(result)
            decrypted_text=""
            counter=0
        #Sort list to find most occurencies     
        newlist=sorted(newlist,key=lambda x: (x[1]),reverse=True)
        print("The most possible shift is ",newlist[0][0]," with ",newlist[0][1]," occurencies")

            

        
               

if __name__ == '__main__':
    main(sys.argv[1:])