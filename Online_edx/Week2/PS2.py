def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    my_set = set(secretWord)
    guessed_set = set(lettersGuessed)
    if all(x in guessed_set for x in my_set):  
        return True
    else:
        return False
    





def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string with guessed letters from the secretWord
    '''
    new_s = []
    
    for i in secretWord:
        if i in lettersGuessed:
            new_s.append(i)
        else:
            new_s.append("_ ")
        
    return ''.join(str(e) for e in new_s)


print(getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's']))
print(getGuessedWord('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u']))
print(getGuessedWord('lettuce', ['e', 'h', 'a', 'y', 'b', 'u', 't', 'g', 'x', 'k']))







def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase_letters = [x.lower() for x in letters]


    l = []
    for element in lowercase_letters:
        if element not in lettersGuessed:
            l.append(element)
    return ''.join(str(e) for e in l)



print(getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']))
print(getAvailableLetters(['n', 'v', 'r', 'y', 'x', 'i', 'c', 'z', 'q', 's', 't', 'k']))

