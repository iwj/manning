print "just command 'e' to exit :)"
mydict = {
        "apple" : "Mac iPhone iPod safari",
        "Google" : "Android Google G-Mail Maps",
        "Twitter" : "a blue bird",
        "Facebook" : "a SNS site which is originally crated To pursue the right girl",
        "one" : "a number, example: one people, one apple",
        "a" : "measure word",
        }

#my opinion
google = 9
apple = 7
ms = 5

while google > ms:

    mode = raw_input("Add or look up a word(a/l)? ")
    if mode == "a":
        new_key = raw_input("Input new word: ")
        new_value = raw_input("Input new mean: ")
        mydict[new_key] = new_value
        print "new word added!"
    elif mode == "l":
        target_word = raw_input("Type the word: ")
        if target_word in mydict.keys():
            print mydict[target_word]
        else:
            print "That word isn't in the dictionary yet."
    elif mode == "e":
        break
    else:
        print "Look! What wrong command you inputted!"
