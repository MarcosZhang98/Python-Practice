# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: strin
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()
secret_word=choose_word(wordlist)
letters_guessed=[]

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    m=0
    for letter in secret_word:
        if letter in letters_guessed:
            m+=1
    if m==len(secret_word):
        return True 
    else:
        return False 

    
        
        

    
        
    
        
        
    
    



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    start='_ '*len(secret_word)
    for guess in letters_guessed:
        if guess in secret_word:
            for z in range(len(secret_word)):
                if secret_word[z]==guess:
                    start=start[0:2*z]+secret_word[z]+start[2*z+1:len(start)]
    return start
            

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters=''
    alphabet='abcdefghijklmnopqrstuvwxyz'
    for char in range(len(alphabet)):
        if alphabet[char] not in letters_guessed:
            available_letters+=alphabet[char]+' '
    return available_letters
            
            
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print('Hello! Welcome to my Hangman Program! I am thinking of a word that is',len(secret_word),'letters long!You have 6 guesses!')
    print('lowercases letters only!')
    print('available letters=abcdefghijklmnopqrstuvwxyz')
    letters_guessed=[]
    alphabet='abcdefghijklmnopqrstuvwxyz'
    vowels='aeiou'
    
    print(get_guessed_word(secret_word,letters_guessed))
    numGuesses=6
    warnings=0
    unique_letter=0
    while numGuesses!=0:
        x=str(input('what is your guess?:'))
        if x in alphabet:
            letters_guessed+=[x]
            if x in secret_word and x!='':
                unique_letter+=1
                if is_word_guessed(secret_word,letters_guessed)==True:
                    break
                print('good guess!!')
                print('you have',numGuesses,'guesses available!')
                print('available letters=',get_available_letters(letters_guessed))
                print(get_guessed_word(secret_word,letters_guessed))
            if x not in secret_word and x in vowels:
                numGuesses-=2
                if numGuesses<=0:
                    break
                print('Sorry!That vowel is not in my word! 2 guesses for a vowel!')
                print('you have',numGuesses,'guesses available!')
                print('available letters=',get_available_letters(letters_guessed))
                print(get_guessed_word(secret_word,letters_guessed))
            if x not in secret_word and x not in vowels:
                numGuesses-=1
                if numGuesses==0:
                    break
                print('Try again!')
                print('you have',numGuesses,'guesses available!')
                print('available letters=',get_available_letters(letters_guessed))
                print(get_guessed_word(secret_word,letters_guessed))
        if x not in alphabet or x=='':
            warnings+=1
            if warnings%3!=0:
                print('warning given for not following rules. Please type a LOWERCASE letter!')
                print('warnings left:',3-warnings)
            if warnings%3==0 and warnings>0:
                numGuesses-=1
                print('3rd warning given! You have lost a guess')
                print('you have',numGuesses,'guesses left')
                warnings=0
        if letters_guessed.count(x)>1:
            warnings+=1
            unique_letter-=1
            if warnings%3!=0:
                print("you've already guessed that letter!This is a warning!")
                print("warnings left:",3-warnings)
            if warnings%3==0 and warnings>0:
                numGuesses-=1
                print('3rd warning given! You have lost a guess')
                print('you have',numGuesses,'guesses left')
                warnings=0
        if numGuesses<=0:
            break
        print('-------------------------------------------------------------------------')
    if numGuesses<=0:
        print('Sorry! You lost! the secret word was',secret_word)
    else:
        print('YOU WON!!!!')
        print('your score is:',numGuesses*unique_letter)
        
    
            
    
    
    
    
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    alphabet='abcdefghijklmnopqrstuvwxyz'
    d=0
    z=0
    my_list=list(my_word)
    while my_list.count(' ')!=0:
        my_list.remove(' ')
    if len(my_list)!=len(other_word):
        return False
    for f in range(len(my_list)):
        if my_list[f] in alphabet:
            z+=1
            if my_list[f]==other_word[f]:
                d+=1
    if z==d:
        return True
   




def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    #counts number of letters guessed so far in hangman(including repeated letters)
    #loop through the wordlist to find words of equal length
    #loop through letters of each word of equal length to check for matching indices and multiplicity of letters
    my_word=my_word.replace(' ','')
    word_listing=list(my_word)
    alphabet='abcdefghijklmnopqrstuvwxyz'
    count=0
    zum=0
    t=0
    for zed in range(len(my_word)):
        if my_word[zed] in alphabet:
            count+=1
    for word in wordlist:
        if len(word)==len(my_word):
            for i in range(len(word)):
                if word[i]==my_word[i] and word.count(word[i])==word_listing.count(my_word[i]):
                    t+=1
                if t==count:
                    zum+=1
                    print(word)
                    break
            t=0
    if zum==0:
        print('No matches found')
            

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to My Hangman Program with HINTS! Maybe you'll win this time!!")
    print('I am thinking of a word that has',len(secret_word), 'letters')
    print('lower case letters only!!')
    letters_guessed=[]
    alphabet='abcdefghijklmnoprstuvwxyz'
    print('available letters:',alphabet)
    vowels='aeiou'
    
    print(get_guessed_word(secret_word,letters_guessed))
    numGuesses=6
    warnings=0
    unique_letter=0
    while numGuesses!=0:
        x=str(input('what is your guess?:'))
        if x in alphabet:
            letters_guessed+=[x]
            if x in secret_word and x!='':
                unique_letter+=1
                if is_word_guessed(secret_word,letters_guessed)==True:
                    break
                print('good guess!!')
                print('you have',numGuesses,'guesses available!')
                print('available letters=',get_available_letters(letters_guessed))
                print(get_guessed_word(secret_word,letters_guessed))
            if x not in secret_word and x in vowels:
                numGuesses-=2
                if numGuesses<=0:
                    break
                print('Sorry!That vowel is not in my word! 2 guesses for a vowel!')
                print('you have',numGuesses,'guesses available!')
                print('available letters=',get_available_letters(letters_guessed))
                print(get_guessed_word(secret_word,letters_guessed))
            if x not in secret_word and x not in vowels:
                numGuesses-=1
                if numGuesses==0:
                    break
                print('Try again!')
                print('you have',numGuesses,'guesses available!')
                print('available letters=',get_available_letters(letters_guessed))
                print(get_guessed_word(secret_word,letters_guessed))
        if x=='*':
            show_possible_matches(get_guessed_word(secret_word,letters_guessed))
        if x!='*' and x not in alphabet or x=="":
            warnings+=1
            if warnings%3!=0:
                print('warning given for not following rules. Please type a LOWERCASE letter!')
                print('warnings left:',3-warnings)
            if warnings%3==0 and warnings>0:
                numGuesses-=1
                print('3rd warning given! You have lost a guess')
                print('you have',numGuesses,'guesses left')
                warnings=0
        if letters_guessed.count(x)>1:
            warnings+=1
            unique_letter-=1
            if warnings%3!=0:
                print("you've already guessed that letter!This is a warning!")
                print("warnings left:",3-warnings)
            if warnings%3==0 and warnings>0:
                numGuesses-=1
                print('3rd warning given! You have lost a guess')
                print('you have',numGuesses,'guesses left')
                warnings=0
        if numGuesses<=0:
            break
        print('-------------------------------------------------------------------------')
    if numGuesses<=0:
        print('Sorry! You lost! the secret word was',secret_word)
    else:
        print('YOU WON!!!!')
        print('your score is:',numGuesses*unique_letter)
    



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

    ###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
