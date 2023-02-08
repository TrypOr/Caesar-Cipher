# Caesar-Cipher
Caesar Cipher encryption,decryption and cryptanalysis

This code is an implementation of a simple command-line interface that can perform encryption, decryption, and cryptanalysis on text files.
For encryption and decryption, the script replaces the whitespaces in the text with an empty string and then loops through the characters in the file. If the character 
is an uppercase letter, it performs an encryption/decryption using a Caesar cipher, with the shift value specified as the argument. If the character is a lowercase 
letter, the script performs a similar encryption/decryption operation. The script does not encrypt/decrypt special characters.

For cryptanalysis, the script decrypts the ciphertext for all possible shift values (0 to 25), and for each shift, it counts the number of words in the decrypted text 
that match a word in a provided dictionary (dictionary_1000.txt). The shift value with the highest number of matching words is considered the most likely shift used in 
the encryption process. The script then outputs the most likely shift and the number of matching words.
