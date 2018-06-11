'''
when you run this program, it will ask you what's the numbers
of starts rows you want to print, the bigger is your number the
bigger the triangle will be!

'''



question = input('How many rows of stars you want to print?')
lineStars = int(question)

def triangle(x):
     
    space = 2*x - 2
    for i in range(0, x):
        for j in range(0, space):
            print(end=" ")
            
        space = space - 1
     
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
        

triangle(lineStars)
