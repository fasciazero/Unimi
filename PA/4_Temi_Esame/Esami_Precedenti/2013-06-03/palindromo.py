'''Exercise 1: Becoming a Palindrome.   (Esame del 3 giugno 2013)'''

def palin(stringa):
    def ricorsiva(parola): #parola e' una lista fatta cosi': [inizio, centro, fine, caratteri aggiunti]
        result = []
        if len(parola[1])>1:
            if parola[1][0] == parola[1][-1]: #la parola e' del tipo: orso
                orso = parola[1]
                o = orso[0]
                rs = orso[1:-1]
                result.extend(ricorsiva([parola[0] + o, rs, o + parola[2], parola[3]])) #[o,rs,o,]
            else: #la parola e' del tipo: cane
                cane = parola[1]
                c = cane[0]
                e = cane[-1]
                an = cane[1:-1]
                result.extend(ricorsiva([parola[0] + c, an + e, c + parola[2], parola[3] + c])) #[c,ane,c,c]
                result.extend(ricorsiva([parola[0] + e, c + an, e + parola[2], parola[3] + e])) #[e,can,e,e]
        else: #[ot,,to,] oppure [ra,d,ar,]
            result.append(parola)
        return result
    
    combinazioni = []
    for r in ricorsiva(['',stringa,'','']):
        combinazioni.append([''.join(r[:3]),r[3]]) #fonde le prime tre e lascia fuori i caratteri aggiunti
    minimo = len(min(combinazioni,key=len)[1]) #numero minimo di lettere aggiunte
    for com in combinazioni:
        if len(com[1]) == minimo:
            yield "The word «{0}» needs {1} insertions to become palindrome: {2}\n    and result is: {3}" \
                  .format(stringa,len(com[1]),[char for char in com[1]],com[0])
        

if __name__ == "__main__":
    for soluzione in palin('casa'):
        print(soluzione)
    for soluzione in palin('otto'):
        print(soluzione)
    for soluzione in palin('palindromo'):
        print(soluzione)
    for soluzione in palin('posero'):
        print(soluzione)
