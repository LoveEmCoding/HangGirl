
word = "lunch time"
hidden = []
used = []
lives = 8
stages = ["/O\\\n_|_\n | \n/ \\",
          "/O\\\n_|\n |\n/ \\",
          "/O\\\n |\n |\n/ \\",
          "/O\\\n |\n |\n/",
          "/O\\\n |\n |",
          "/O\\",
          "/O",
          " O",
          ""]

for i in range(0,len(word)):
    hidden.append("_")

name = raw_input("what is your name:?")
print "Welcome to my version of hang man! Here are the rules and things you will need to know for the game: \n - enter only lower cases,\n - your lives will be on the screen\n - There can be space's in the word so look out for that!\n So lets play hang man!"

#Game loop
while lives > 0:

    print stages[lives]

    print hidden
    guess = raw_input("Guess a letter for the game, chosse carefully: ")

    if not guess in used:
        used.append(guess)
    else:
       continue


    if guess in word:
    #replace underscores with that letter
        for j in range(0, len(word)):
            if word[j]  == guess:
                hidden[j] = word[j]
        print "You have ", lives, "lives"

    #if they were wrong
    else:
        lives-=1
        print "\nYour guess was incorrect try again"
        print "You have ", lives, "lives"

    if hidden.count('_') == 0:
        break
    
print stages[lives]
print "The word was:" ,word

if lives > 0:
      print "You win. Congrats! Would you like to play again?"
           
else:
    print "Unfortunetly you lost. Try again!I bet you you will win next time"

