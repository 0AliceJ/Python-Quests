## Quest Details
#I have intercepted a secret message intended for the Evil One.
#Rumor has it that this secret message contains the password for a lair that the Evil One will be at next Sunday.
#However, to my dismay, the message is encrypted.
#Your task is to use python to decrypt the message and send me the password.
#We must decrypt the password before next Sunday the 29th!

#Hint: rumor has it that the Evil one uses the same encryption method that Julius Caesar used back in the day.
#Hint: use ord() and shift the letters, remember to loop the sequence to the start of the alphabet again(?)

#CMD + K to clear terminal

#encrypted message
secretMsg = """N mjfw ymfy mj nx ywfnsnsl ymj dtzsl Fqnhj ns ymj fwy tk xtkybfwj ijajqturjsy. 
Bj rzxy ywd yt xytu ymjr. 
Ymtxj gqfxyji uwtlwfrrjwx fwj gjhtrnsl ytt utbjwkzq. 
Fsi bnym ymfy rnsi tk mjw'x, xmj htzqi gjhtrj ymj rtxy utbjwkzq uwtlwfrrjw djy. 
Qjy'x fwwfslj yt rjjy fy ymj sjb qfdjw ts Xzsifd, Xjuyjrgjw 29ym. 
Ymj ufxxbtwi ktw jsywd nx "twfhqj917", N'qq gj xzwj sty yt tujs ny ktw fsdtsj zsqjxx ymnx ufxxbtwi nx uwjxjsyji. """
upMsg = secretMsg.upper()

#set up vars
step = int()
key = []
arrMsg = []
newMsg = """"""


#list alphabet into array
lfbt = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


#append lfbt to key in correct order
for i in range(26):
    key.append(lfbt[i+step])


#add every character of secretMsg into array/list
if upMsg != "":
    for i in range(len(upMsg)):
        arrMsg.insert(0, upMsg[-1])
        upMsg = upMsg[:-1]

#compare + decode characters of arrMsg
#add converted character to final message
#run through every step version (DOES NOT WORK)
for j in range(25):
    step = -5
    print(step)

    for i in range(len(arrMsg) - 1):
        
        #checks if character in front is ABCDEF
        if arrMsg[0] == 'A' or arrMsg[0] == 'B' or arrMsg[0] == 'C' or arrMsg[0] == 'D' or arrMsg[0] == 'E' or arrMsg[0] == 'F':
            
            #checks if character is ABC
            if arrMsg[0] == 'A' or arrMsg[0] == 'B' or arrMsg[0] == 'C':
                if arrMsg[0] == 'A':
                    newMsg = newMsg+arrMsg[0].replace(lfbt[0], lfbt[0+step])
                elif arrMsg[0] == 'B':
                    newMsg = newMsg+arrMsg[0].replace(lfbt[1], lfbt[1+step])
                else:
                    newMsg = newMsg+arrMsg[0].replace(lfbt[2], lfbt[2+step])
            else: #only when characters are ABCDEF but not ABC
                if arrMsg[0] == 'D':
                    newMsg = newMsg+arrMsg[0].replace(lfbt[3], lfbt[3+step])
                elif arrMsg[0] == 'E':
                    newMsg = newMsg+arrMsg[0].replace(lfbt[4], lfbt[4+step])
                else:
                    newMsg = newMsg+arrMsg[0].replace(lfbt[5], lfbt[5+step])
        elif arrMsg[0] == 'G' or arrMsg[0] == 'H' or arrMsg[0] == 'I' or arrMsg[0] == 'J' or arrMsg[0] == 'K' or arrMsg[0] == 'L' or arrMsg[0] =='M': #checks if character in front is GHIJKLM
            
            #checks if character is GHI
            if arrMsg[0] == 'G' or arrMsg[0] == 'H' or arrMsg[0] == 'I':
                if arrMsg[0] == 'G':
                    newMsg = newMsg+arrMsg[0].replace(lfbt[6], lfbt[6+step])
                elif arrMsg[0] == 'H':
                    newMsg = newMsg+arrMsg[0].replace(lfbt[7], lfbt[7+step])
                else:
                    newMsg = newMsg+arrMsg[0].replace(lfbt[8], lfbt[8+step])
            else: #only when characters are GHIJKLM but not GHI
                if arrMsg[0] == 'J':
                    newMsg = newMsg+arrMsg[0].replace(lfbt[9], lfbt[9+step])
                elif arrMsg[0] == 'K':
                    newMsg = newMsg+arrMsg[0].replace(lfbt[10], lfbt[10+step])
                elif arrMsg[0] == 'L':
                    newMsg = newMsg+arrMsg[0].replace(lfbt[11], lfbt[11+step])
                else:
                    newMsg = newMsg+arrMsg[0].replace(lfbt[12], lfbt[12+step])
        elif arrMsg[0] == 'N' or arrMsg[0] == 'O' or arrMsg[0] == 'P' or arrMsg[0] == 'Q' or arrMsg[0] == 'R' or arrMsg[0] == 'S': #checks if character in front is NOPQRS
            
            #checks if character is NOP
            if arrMsg[0] == 'N' or arrMsg[0] == 'O' or arrMsg[0] == 'P':
                if arrMsg[0] == 'N':
                    newMsg = newMsg+arrMsg[0].replace(lfbt[13], lfbt[13+step])
                elif arrMsg[0] == 'B':
                    newMsg = newMsg+arrMsg[0].replace(lfbt[14], lfbt[14+step])
                else:
                    newMsg = newMsg+arrMsg[0].replace(lfbt[15], lfbt[15+step])
            else: #only when characters are NOPQRS but not NOP
                if arrMsg[0] == 'Q':
                    newMsg = newMsg+arrMsg[0].replace(lfbt[16], lfbt[16+step])
                elif arrMsg[0] == 'R':
                    newMsg = newMsg+arrMsg[0].replace(lfbt[17], lfbt[17+step])
                else:
                    newMsg = newMsg+arrMsg[0].replace(lfbt[18], lfbt[18+step])
        elif arrMsg[0] == 'T' or arrMsg[0] == 'U' or arrMsg[0] == 'V' or arrMsg[0] == 'W' or arrMsg[0] == 'X' or arrMsg[0] == 'Y' or arrMsg[0] =='Z': #checks if character in front is TUVWXYZ
            
            #checks if character is TUV
            if arrMsg[0] == 'T' or arrMsg[0] == 'U' or arrMsg[0] == 'V':
                if arrMsg[0] == 'T':
                    newMsg = newMsg+arrMsg[0].replace(lfbt[19], lfbt[19+step])
                elif arrMsg[0] == 'U':
                    newMsg = newMsg+arrMsg[0].replace(lfbt[20], lfbt[20+step])
                else:
                    newMsg = newMsg+arrMsg[0].replace(lfbt[21], lfbt[21+step])
            else: #only when characters are TUVWXYZ but not TUV
                if arrMsg[0] == 'W':
                    newMsg = newMsg+arrMsg[0].replace(lfbt[22], lfbt[22+step])
                elif arrMsg[0] == 'X':
                    newMsg = newMsg+arrMsg[0].replace(lfbt[23], lfbt[23+step])
                elif arrMsg[0] == 'Y':
                    newMsg = newMsg+arrMsg[0].replace(lfbt[24], lfbt[24+step])
                else:
                    newMsg = newMsg+arrMsg[0].replace(lfbt[25], lfbt[25+step])
        else: #include all remaining misc characters
            newMsg = newMsg+arrMsg[0]

        arrMsg.pop(0)
    print(newMsg)
    newMsg = """"""
      







# using three quotation marks is a multiline string (can be single or double quotes)
'''
#check if a certain string is in another string
if "mjfw" in secretMsg:
    print("The \"in\" statement works correctly.")

#find the starting position of string (counting from first char)
indexString = secretMsg.find('mjfw')

if indexString != -1:
    print(f"The text \"mfjw\" is located from character position {indexString} in the secret message.") #figure out how to format var thingy: DONE! put f in front of quotation marks and put variable inside curly brackets
else:
    print("The text \"mfjw\" doesn't exist in the secret message.")

#ask Chris how to put the file into the right python folder so I can execute it from terminal: DONE! do it in VS Code terminal with python3 ___.py

#prints the length of the string, counting from 1
#includes spaces and line breaks
print(len(secretMsg))

#print range of string by formatting it as an array
#range inclusive of bottom num but not top num
print(secretMsg[2:5])

#this does not work
#print(secretMsg[5:2]) 

#splice until certain point not inclusive
print(secretMsg[:5])

#splice counting from end of string not inclusive of bottom num
print(secretMsg[-5:-1]) #seems like top num cannot be 0

#replace characters in string (characters must be exact)
print(secretMsg.replace(" ", "space"))
'''