#WARMUP
def animal_crackers(twowords):
     l = twowords.split()
     if l[0][0]==l[1][0]:
         return True
     else:
         return False
print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))

def makes_twenty(n,a):
    if n+a==20:
        return True
    elif n==20 or a==20:
        return True
    else:
        return False
print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))

#LEVEL1
def old_macdonald(word):
    st = ''
    for i in range(len(word)):
        if i==0 or i==3:
            st = st + word[i].upper()
        else:
            st = st + word[i]
    return st
print(old_macdonald('macdonald'))

def master_yoda(st):
    out = st.split()[::-1]
    out = out[::-1]
    return ' '.join(out) #une os strings de uma lista
print(master_yoda('I am home'))
print(master_yoda('We are ready'))

def almost_there(n):
    if abs(n-100)<=10:
        return True
    elif abs(n-200)<=10:
        return True
    else:
        return False
print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

#LEVEL2
def has_33(lints):
    for i in range(len(lints)-1):
        if lints[i]==3:
            if lints[i+1]==3:
                return True
    return False
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

def paper_doll(st):
    letters = [3*x for x in st]
    return "".join(letters)
print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

def blackjack(a,b,c):
    if a+b+c<=21:
        return a+b+c
    elif a==11 or b==11 or c==11:
        ajuste = a+b+c-10
        if ajuste>21:
            return 'BUST'
        else:
            return ajuste
    else:
        return 'BUST'
print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))

def summer_69(l):
    soma = 0
    n=0
    while n<len(l):
        if l[n]==6:
            index = l.index(9,n)
            n = index + 1
        else: 
            soma += l[n]
            print(l[n])
            n += 1
    return soma
print(summer_69([1, 3, 5]),'\n')
print(summer_69([4, 5, 6, 7, 8, 9]),'\n')
print(summer_69([2, 1, 6, 9, 11]),'\n')  

#CHALLENGING    
def spy_game(li):
    for fir in li:
        if fir==0 and not li.index(fir)==len(li)-2:
            print(li.index(fir))
            for n in range(li.index(fir)+1,len(li)):
                if li[n]==0:
                    for x in range(li.index(li[n])+1,len(li)):
                        if li[x]==7:
                            return True
    return False
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

def count_primes(a):
    #primes = []
    cont=0
    for n in range(2,a+1):
        div = 0
        for x in range(1,n+1):
            if n%x==0:
                div += 1
        if div==2:
            #primes.append(n)
            cont += 1
    #return primes
    return cont
print(count_primes(100))

#JUST FOR FUN
def print_big(letter):
    a ='  *  \n * *\n*****\n*   *\n*   * '
    b = '*****\n*   *\n****\n*   *\n*****'
    c = ' ****\n*\n*\n*\n ****'
    d = '****\n*   *\n*   *\n*   *\n****'
    e = '*****\n*\n*****\n*\n*****'
    letras = {'a':a,'b':b,'c':c,'d':d,'e':e}
    return letras[letter]
print(print_big('e'))

