def palin(aString):
    '''Calculate the mininum number of letters to be added to a word to become a palindrome'''
    #Prova entrambe le soluzioni sulla parola e sulla parola al contrario,
    #ritorna la soluzione che aggiunge meno lettere. Le lettere possono essere aggiunte in ogni posizione
    def from_left(aString):
        letters_to_add_from_left = []
        revString = aString[::-1]
        for i in range(len(aString)-1):
            if aString[i] != revString[i]:
                revString = revString[:i] + aString[i] + revString[i:]
                letters_to_add_from_left.append(aString[i])     
        return letters_to_add_from_left
        
    def from_right(aString):
        letters_to_add_from_right = []
        revString, aString = aString, aString[::-1]
        for i in range(len(aString)-1):
            if aString[i] != revString[i]:
                revString = revString[:i] + aString[i] + revString[i:]
                letters_to_add_from_right.append(aString[i])   
        return letters_to_add_from_right
        
    def decide():
        return from_left(aString) if len(from_left(aString))<len(from_right(aString)) else from_right(aString)
    
    ans = "The word «{0}» needs {1} insertions to become palindrome ".format(aString, len(decide()))
    ans += "" if len(decide())==0 else ": {0}".format(decide())
    return ans
            
        
        

if __name__ == "__main__":           
    print(palin("casa")) 
    print(palin("otto"))          
    print(palin("palindromo"))
    print(palin("posero")) #mi viene diverso da come vorrebbe lui...
    print(palin("coccinella"))
