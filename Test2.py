#Nested Loops
def NestedLoopSquare():
    n_width = int(input('Enter Height: '))
    n_heigh = int(input('Enter With: '))
    c_symbol = input('Symbol: ')

    for x in range(n_width): #Collums
        for y in range(n_heigh): #Rows
            print(c_symbol, end=' ')
        print()



def NestedLoopTriangle():
    import time
    nn_height = int(input('Enter Heights:'))
    cc_symbol = input('Symbol:')
    for i in range(1, nn_height + 1):
        for j in range(i):
            print(cc_symbol, end=' ')
            time.sleep(1)
    print()

def NestedLoopTriangleInverse():
    import time
    nnn_height = int(input('Enter Heights:'))
    ccc_symbol = input('Symbol:')
    for i in range(nnn_height, 0, -1):
        for j in range(i):
            print(ccc_symbol, end=' ')
            time.sleep(1)
        print()

def BreakPassContinue():
    c_Name = 'iCe'
    while True:
        c_Name = input('Enter name: ')
        if(c_Name == 'iCE'):
            continue
            print('Sample')
        elif(c_Name == 'USLS'):
            pass
        elif(c_Name != ''):
            break
            print('Exit FROm CODE')

def TempName():
    import random
    import string

    # r_letter = random.choice(string.ascii_uppercase)
    # print(r_letter)

    # for i in range(5):
    #     tmp += random.choice(string.ascii_uppercase)

    for i in range(5):
        print(random.choice(string.ascii_uppercase), end='')

    print('\n-------------------------------')
    #version #2
    random_letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    print(random_letters)



TempName()