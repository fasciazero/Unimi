'''Esame 4/06/2012 es.2

An alternade is a word in which its letters, taken alternatively in a strict sequence, and used in the same order as the original word, make up as many real words as the alternade length. All letters must be used, but the smaller words are not necessarily of the same length. For example, a word with seven letters where every second letter is used will produce a four-letter word and a three-letter word.

In the majority of alternades, every second letter is used to make two smaller words, but in some cases, every third letter is used to make three smaller words and so on. Theoretically, a very long word could use every fourth/fifth/... letter to make four/five/... smaller words; e.g., ?partitioned? is an alternade for ?pin?, ?ate?, ?rid?, and ?to?.

In this exercise is required to implement a generator, named alternade_generator, parametric on a dictionary filename and on the number of the alternades you need for each word. At each step the generator has to generate an alternade, i.e., a couple word and a list of its spawns (spawned as for the rules above) checked into the dictionary that the all the spawns are real words. As a dictionary please use the following file (it is already sorted do not change it).

'''
def alternade_generator(dict_file,i):

    d = open(dict_file,'r').read().rsplit()

    set_d = set(d)
    for w in d:
        if len(w)>=2*i:
            spawns = set([''.join([w[k] for k in range(len(w)) if (k-j)%i==0]) for j in range(i)])

            if len(spawns)==i and spawns.issubset(set_d):
                yield (w,list(spawns))

if __name__ == '__main__':

    for i in range(2,5):
        tot = 0
        var_format = "<<{0}>> is an alternade for "+\
        ("<<{{{}}}>>, "*(i-1)).format(*range(1,i))+"and <<{{{}}}>>".format(i)

        for w, a in alternade_generator("dictionary.txt", i):
            tot+=1
            print(var_format.format(w,*a))
        print("There are {0} alternade of lenght {1} in this dictionary\n"
            .format(tot, i))
