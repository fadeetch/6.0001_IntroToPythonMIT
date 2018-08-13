
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