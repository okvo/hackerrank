#https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(st):
    # your code goes here
    vowels = ['A', 'E', 'I', 'O', 'U']
    stuart = 0
    kevin = 0
    for i in range(len(st)):
        if st[i] in vowels:
            kevin = kevin + (len(st)-i)          
        else:
            stuart = stuart + (len(st)-i)     

    if kevin > stuart:
        print ('Kevin', kevin)
    elif kevin < stuart:
        print ('Stuart', stuart)
    else:
        print ('Draw')
    return

if __name__ == '__main__':
    s = input()
    minion_game(s)