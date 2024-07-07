# PRODIGY_CS_01
# Caesar Cipher: A Simple Encryption Technique

The Caesar Cipher is a basic encryption technique that replaces each letter in a message with a letter a fixed number of positions down the alphabet. This fixed number is called the shift or key.

# How it works:

# Encryption
To encrypt a message, each letter is shifted down the alphabet by the specified number of positions. For example, if the shift is 3, the letter 'a' becomes 'd', 'b' becomes 'e', and so on.

# Decryption
 To decrypt an encrypted message, each letter is shifted back up the alphabet by the same number of positions. In our example, 'd' becomes 'a', 'e' becomes 'b', and so on.

# Example:

Suppose we want to encrypt the message "HELLO" with a shift of 3.

H -> K (H + 3 positions down the alphabet)
E -> H
L -> O
L -> O
O -> R
The encrypted message is "KHOOR".

To decrypt "KHOOR" with a shift of 3, we shift each letter back up the alphabet:

K -> H
H -> E
O -> L
O -> L
R -> O
The decrypted message is "HELLO".

The Caesar Cipher is a simple and easy-to-implement encryption technique, but it's not very secure, as it can be easily broken by frequency analysis or brute force attacks. Nevertheless, it's a great introduction to the world of cryptography!
 
