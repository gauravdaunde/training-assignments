'''
4.  One classic method for composing secret messages is called a square code.  The spaces are 
removed from the english text and the characters are written into a square (or rectangle).  
For example, the sentence "If man was meant to stay on the ground god would have given us 
roots" is 54 characters long, so it is written into a rectangle with 7 rows and 8 columns.

                ifmanwas
                meanttos        
                tayonthe
                groundgo
                dwouldha
                vegivenu
                sroots

The coded message is obtained by reading down the columns going left to right.   For example, 
the message above is coded as:

imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn  sseoau
no spaces between th
In your program, have the user enter a message in english with e words.  Have the maximum message length be 81
characters.  Display the encoded message. (Watch out that no "garbage" characters are printed.)    Here are some more examples:

 Input                                           Output
haveaniceday                                    hae and via ecy
feedthedog                                      fto ehg ee  dd
chillout                                        clu hlt io
'''

message = input("Enter message without spaces: ")
length = len(message)
col = 0
row = 0

# finding suitable column and row size for encoding
while True:
    if row*col >= length:
        break
    col += 1
    row += 1
i = 0
new_message = []
while len(new_message) < row:
    # adding sliced string to list for further encoding
    new_message.append(message[i:i+col])
    i += col
encoded_string = []
for item in new_message:  # iterrating thrugh all sliced string
    for i in range(len(item)):  # iterrating loop for sting length times
        # at each iteration string of n length divided in n different encoded message,taking only one character
        # checking if encoded list is empty or not.
        if len(encoded_string) == col:
            # if not empty then add every i'th of item string to each element of encoded_string
            encoded_string[i] += item[i]
        else:  # executes if encoded_string list is empty
            # then creating elements equal to length of item ,and adding i'th element as i'th character of item string
            encoded_string.append(item[i])


print(f"Encoded string: {encoded_string}")
