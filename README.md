![banner image](https://www.subplotstudio.com/resources/images/headers/header-145.jpg)

# Save Romeo
### Your mission
Capulet and Montague are sworn enemies, but their children, Romeo of the Montague house and Juliet of the Capulet house, are in love. Romeo spoke with Father Laurence and convinced him to marry him to Juliet. He wants to send her a message about her father's consent to their marriage, but he's afraid that if the message is intercepted by the Capulet family, they will want to kill him, thus preventing Juliet from being with him.

Romeo had an idea: he would develop software that would encrypt the message. This way, he can send Juliet an encrypted message, and she will also have the software to decipher the message.

Romeo's good friend, Mercutio, suggested using a [Scytale](https://en.wikipedia.org/wiki/Scytale), but Romeo mocked him, saying, "Even the Roman Empire has long since fallen, and you're suggesting using a cipher that was in use long before its time. There's no chance we'll find a cylinder of an unknown diameter."

Blatantly, one of Romeo's servants suggested using the [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher), but Romeo rejected the proposal, arguing that it's unlikely anyone in Verona would use a cipher invented by the Romans. After all, it's even named after the emperor Julius, who used this cipher with a key of 3.

Another servant of Romeo's, Abram, who had a rare gift for persuasion and eloquence, said, "Perhaps we should use a less common cipher." Immediately, silence fell in the room, and everyone leaned in to listen.

Since Romeo doesn't know how to program, he turned to you to develop the software for him.

### The software requirements
The software will have two options (via command-line arguments using sys.argv):

##### encrypt - Encryption
- The program will request the user to enter a message.
- The program will encrypt the message and save it in a file named "encrypted_msg.txt" in the directory from which the program is run.

##### decrypt - Decryption
- The program will decrypt the encrypted message from the "encrypted_msg.txt" file and print its contents to the screen.

#### Edge Cases:
- the software will have to know to deal with an empty message.

#### Encryption:
- Each character will be replaced by a number (according to the table).
- A comma will separate each pair of characters (assume that all characters are present in the table).


##### Convertion table
| letter | cipher | letter | cipher | letter | cipher | letter | cipher |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| a | 12 | A |  56 | b | 13 | B |  57 |
| c | 14 | C |  58 | d | 15 | D |  59 |
| e | 16 | E |  40 | f | 17 | F |  41 |
| g | 18 | G |  42 | h | 19 | H |  43 |
| i | 30 | I |  44 | j | 31 | J |  45 |
| k | 32 | K |  46 | l | 33 | L |  47 |
| m | 34 | M |  48 | n | 35 | N |  49 |
| o | 36 | O |  60 | p | 37 | P |  61 |
| q | 38 | Q |  62 | r | 39 | R |  63 |
| s | 90 | S |  64 | t | 91 | T |  65 |
| u | 92 | U |  66 | v | 93 | V |  67 |
| w | 94 | W |  68 | x | 95 | X |  69 |
| y | 96 | Y |  10 | z | 97 | Z |  11 |
| (space) | 98 | (dot) |  100 | (comma) | 99 | ; | 101 |
| (apostrophe) |  102 | ? | 103 | ! | 104 | : | 105 |


### Examples
##### One:
- message: ```My bounty is as boundless as the sea, My love as deep; the more I give to thee, The more I have, for both are infinite.```

- cipher: ```48,96,98,13,36,92,35,91,96,98,30,90,98,12,90,98,13,36,92,35,15,33,16,90,90,98,12,90,98,91,19,16,98,90,16,12,99,98,48,96,98,33,36,93,16,98,12,90,98,15,16,16,37,101,98,91,19,16,98,34,36,39,16,98,44,98,18,30,93,16,98,91,36,98,91,19,16,16,99,98,65,19,16,98,34,36,39,16,98,44,98,19,12,93,16,99,98,17,36,39,98,13,36,91,19,98,12,39,16,98,30,35,17,30,35,30,91,16,100```

##### Two:
- message: ```Don't waste your love on somebody, who doesn't value it.```

- cipher: ```59,36,35,102,91,98,94,12,90,91,16,98,96,36,92,39,98,33,36,93,16,98,36,35,98,90,36,34,16,13,36,15,96,99,98,94,19,36,98,15,36,16,90,35,102,91,98,93,12,33,92,16,98,30,91,100```

##### Three:
- message: ```Love is a smoke raised with the fume of sighs; Being purged, a fire sparkling in lovers' eyes; Being vexed a sea nourish'd with loving tears: What is it else? a madness most discreet, A choking gall, and a preserving sweet.```

- cipher: ```47,36,93,16,98,30,90,98,12,98,90,34,36,32,16,98,39,12,30,90,16,15,98,94,30,91,19,98,91,19,16,98,17,92,34,16,98,36,17,98,90,30,18,19,90,101,98,57,16,30,35,18,98,37,92,39,18,16,15,99,98,12,98,17,30,39,16,98,90,37,12,39,32,33,30,35,18,98,30,35,98,33,36,93,16,39,90,102,98,16,96,16,90,101,98,57,16,30,35,18,98,93,16,95,16,15,98,12,98,90,16,12,98,35,36,92,39,30,90,19,102,15,98,94,30,91,19,98,33,36,93,30,35,18,98,91,16,12,39,90,105,98,68,19,12,91,98,30,90,98,30,91,98,16,33,90,16,103,98,12,98,34,12,15,35,16,90,90,98,34,36,90,91,98,15,30,90,14,39,16,16,91,99,98,56,98,14,19,36,32,30,35,18,98,18,12,33,33,99,98,12,35,15,98,12,98,37,39,16,90,16,39,93,30,35,18,98,90,94,16,16,91,100```

##### Four:
- message: ```My only love sprung from my only hate! Too early seen unknown, and known too late! Prodigious birth of love it is to me That I must love a loathed enemy.```

- cipher: ```48,96,98,36,35,33,96,98,33,36,93,16,98,90,37,39,92,35,18,98,17,39,36,34,98,34,96,98,36,35,33,96,98,19,12,91,16,104,98,65,36,36,98,16,12,39,33,96,98,90,16,16,35,98,92,35,32,35,36,94,35,99,98,12,35,15,98,32,35,36,94,35,98,91,36,36,98,33,12,91,16,104,98,61,39,36,15,30,18,30,36,92,90,98,13,30,39,91,19,98,36,17,98,33,36,93,16,98,30,91,98,30,90,98,91,36,98,34,16,98,65,19,12,91,98,44,98,34,92,90,91,98,33,36,93,16,98,12,98,33,36,12,91,19,16,15,98,16,35,16,34,96,100```