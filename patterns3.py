#Norma
#patterns3.py

def checkerboard(N):
    print("Checkerboard: ", '\n')
    m = N//2
    for count in range(N):
        if count%2==0:
            print('*-' * m)
        else:
            print('-*'*m)

def vee(N):
    print("V: ", '\n')

    for count in range(N):
        for i in range(count+1):
            print(end=' ')
        print('*', end='')
        if count is not N-1:
            s = ' '*(((N-1)*2-1)-count*2)
            print(s, end='')
            print('*')
        else:
            print('')



def x(N):
    print("X: ", '\n')

    for row in range(N*2-1):
        for col in range(N*2-1):
            if (row == col) or (((N*2-1) - col - 1) == row):
                print('*', end='')
            else:
                print(' ', end='')
        print('')

def solid_diamond(N):
    print("Solid diamond: \n")

    for rows in range(((2*N+1) + 1) // 2 + 1):
        for count in range(((2*N+1) + 1) // 2 - rows):
            print(" ", end="")
        for i in range((rows * 2) - 1):
            print("*", end="")
        print()
    for rows in range(((2*N+1) + 1) // 2 + 1, 2*N+1 + 1):
        for count in range(rows - ((2*N+1) + 1) // 2):
            print(" ", end="")
        for i in range(((2*N+1) + 1 - rows) * 2 - 1):
            print("*", end="")
        print()

def hollow_diamond(N):
    print("hollow diamond: ")

    for rows in range(((2*N+1) + 1) // 2):
        for count in range(((2*N+1) - 1) // 2 - rows):
            print(" ", end="")
        print('*', end="")
        if rows is not 0:
            for i in range((rows * 2) - 1):
                print(" ", end="")
            print('*')
        else:
            print("")
    for rows in range(((2*N+1) + 1) // 2, 2*N+1):
        for count in range(rows - ((2*N+1) + 1) // 2+1):
            print(" ", end="")
        print('*', end="")
        if rows is not (2*N):
            for i in range(((2*N-1) - (2*(rows-N)))):
                print(" ", end="")
            print('*')
        else:
            print("")


def nested_squares(N):
    print("nested squares: ")
    for row in range(2*N+1):
        for col in range(2*N+1):
            if row in [0, (2 * N + 1) - 1] or col in [0, (2 * N + 1) - 1]:
                print('*', end='')
            elif row==N and col ==N:
                print('*', end='')
            elif row in [2, (2 * N + 1)-3] or col in [2, (2 * N +1)-3]:
                if row != 1 and row!= (2*N+1)-2 and col !=1 and col != (2*N+1)-2:
                    print('*', end='')
                else:
                    print(' ', end='')

            else:
                print(' ', end='')
        print()


def nested_triangles(N):
    print("nested triangles: ")
    for row in range(2*N+1):
        for col in range(2*N+1):
            if row in [col, 2*N] or col == 0:
                print('*', end='')
            elif row==N+2 and col ==N-2:
                print('*', end='')
            elif row in [col+2, 2*N-2] and col!=1 and col!=(2*N) and col!=(2*N-1) and col!=(2*N-3):
                print('*', end='')
            elif col == 2 and row !=0 and row!=1 and row!=2 and row !=3 and row!=(2*N-1):
                print('*', end='')
            else:
                print(' ', end='')

        print()

def main():
    N = int(input("Enter a positive integer: "))
    checkerboard(N)
    vee(N)
    x(N)
    solid_diamond(N)
    hollow_diamond(N)
    nested_squares(N)
    nested_triangles(N)

main()