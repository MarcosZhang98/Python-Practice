# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*':0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    assert n-len(word)>=0 #so we don't have erronoeus output 
    word=word.lower() 
    letter_sum=0
    if len(word)==0:
        return 0
    for letter in word: 
        if letter in CONSONANTS or VOWELS:
            letter_sum+=SCRABBLE_LETTER_VALUES[letter]
    if 7*len(word)-3*(n-len(word))<=1:
        return letter_sum
    else:
        return letter_sum*(7*len(word)-3*(n-len(word)))

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function work and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))
    hand['*']=1
    #pick out num_vowels-1 vowels after wildcard
    for i in range(num_vowels-1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
        
     #pick consonants       
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    unique_letters=[]
    new_hand=hand.copy()
    word=word.lower()
    for letter in word:
        if letter not in unique_letters:
            unique_letters+=letter
    for i in unique_letters: #should I turn this into a global variable?
        if i in hand:
            if word.count(i)>new_hand[i]:
                new_hand[i]=0
            else:
                new_hand[i]-=word.count(i)
    return new_hand
        

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    #modify to support wildcards
    z=0
    word=word.lower()
    wildcard_words=[]
    unique_letters=[]
    indicator_variable=0
    
    #to check for every unique letter and put them in a list
    for letter in word:
        if letter not in unique_letters:
            unique_letters+=letter
            
    #looping over unique letters to make sure word is entirely composed from letters in hand        
    for i in unique_letters:
        if hand.get(i,0)!=0:
            if word.count(i)>hand[i]:
                break
            else:
                z+=1
        else:
            break
        
    #check if legitimate use of wildcard using indicator variable
    if "*" in word:
        m=word.find('*')
        for vowel in 'aeiou':
            if word[0:m]+vowel+word[m+1:len(word)] in word_list:
                wildcard_words+=[word[0:m]+vowel+word[m+1:len(word)]]
                indicator_variable=1
                
    #lines 240-249: if word is composed of letters from hand, check if word is in the wordlist
    if z==len(unique_letters) and '*' not in word:
        if word in word_list:
            return True
        else:
            return False
    
    if z==len(unique_letters) and '*' in word:
        if indicator_variable==1:
            return True
        else:
            return False
        
    #word is not composed of letters from hand 
    if z!=len(unique_letters):
        return False


#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    handlen=0
    for letter in hand:
        handlen+=hand[letter]
    return handlen


def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    ID=0
    t=0
    total_score=0
    assert HAND_SIZE>0
        
    
    while True:
        print('Current Hand:',end=' ')
        display_hand(hand)
        word=str(input('Enter a word, or "!!" to indicate you are finished: '))
        if word=='!!':
            ID=1
            break
        if is_valid_word(word,hand,word_list):
            total_score+=get_word_score(word,HAND_SIZE)
            print(word,'Earned',get_word_score(word,HAND_SIZE),'points. Total Score: ',total_score)
            print()
        else:
            print('That is not a valid word.')
            print()
        hand=update_hand(hand,word)
        t=0
        for entry in hand:
            if hand[entry]==0:
                t+=1
        if t==len(hand):
            break
                
    
    
    if ID==1:
        print('Total Score For This Hand: ',total_score)
        print()
    else:
        print('Ran out of letters. Total Score For This Hand: ',total_score)
        print()
    return total_score

        
        
        




#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    
    new_hand=hand.copy()
    x=''
    if letter in hand:
        a=new_hand[letter]
        del(new_hand[letter])
        x=random.choice(CONSONANTS+VOWELS)
        while x in hand:
            x=random.choice(CONSONANTS+VOWELS)
        new_hand[x]=a
        return new_hand
    else:
        return hand

    

def play_game4(word_list):
    
    """Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
     #try-except to get number of hands from the user
    while True:
        try:
            total_hands=int(input('Enter Total Number of Hands: '))
            break
        except ValueError:
            print('please input an integer')
    
    #initialize some variables 
    n=''#avoid UnboundLocalError
    m=''
    score=0
    z=total_hands
    round_score=0
    replays_left=1
    substitutions_left=1
    replay_score=0
    replay={}
    
    
    while total_hands!=0:
            print('Hand #:',z-total_hands)
            hand=deal_hand(HAND_SIZE)
            replay=hand.copy()
            if n!=' ':
                print('Current Hand:',end='')
                display_hand(hand)
            if substitutions_left==1:
                while True:
                    n=input('would you like to substitute a letter?:')
                    if n=='yes' or n=='YES' or n=='Yes':
                        break
                    if n=='NO' or n=='No' or n=='no':
                        break
                    else:
                        print('please input appropriate answer to yes or no question')
                if n=='yes' or n=='YES' or n=='Yes':
                    while True:
                        letter_to_substitute=input('which letter would you like to substitute?: ')
                        if letter_to_substitute not in hand:
                            print('You can only substitute a letter you already have.')
                        if letter_to_substitute=='*':
                            print('you cannot substitute your wildcard')
                        if letter_to_substitute in hand and letter_to_substitute!='*':
                            break
                    hand=substitute_hand(hand,letter_to_substitute)
                    replay=hand.copy()
                    substitutions_left-=1
                    n=' '
            round_score=play_hand(hand,word_list)
            score+=round_score
            if replays_left==1:
                while True:
                    m=input('would you like to replay the hand?:')
                    if m=='yes' or m=='YES' or m=='Yes':
                        break
                    if m=='no' or m=='NO' or m=='No':
                        break
                    else:
                        print('please input an appropriate statement to a yes or no question')
                if m=='yes' or m=='YES' or m=='Yes':
                    hand=replay
                    score-=round_score
                    replays_left-=1
                    replay_score=play_hand(hand,word_list)
                    if replay_score>round_score:
                        score+=replay_score
                        print('Highest score after replaying:',replay_score)
                        print()
                    else:
                        score+=round_score
                        print('Highest score after replaying:',round_score)
                        print()
                    m=' '
                    
                if m=='no' or m=='NO' or m=='No':
                    pass 
            total_hands-=1
    print('Total score for all hands:',score)
    return score
            
                    
    
                
                    
                
            

    
    
            
        
        

                        
    

#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game4(word_list)
