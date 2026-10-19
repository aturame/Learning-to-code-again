import numpy as np

#Numpy Arrays + Calculating 2x2 and 3x3 determinants

def twodet():
    show_det = ["a","b"],["c","d"]
    print("Please input a,b,c and d in this form")
    print(np.matrix(show_det))
    a = int(input("A: "))
    b = int(input("B: "))
    c = int(input("C: "))
    d = int(input("D: "))
    determinant = (a*d)-(b*c)
    print(f"The 2x2 determinant of {np.matrix([[a,b],[c,d]])} is {determinant}") 

def threedet():
    show_det = ["a","b","c"],["d","e","f"],["g","h","i"]
    print("Please input; a,b,c,d,e,f,g,h,i in this form")
    print(np.matrix(show_det))
    a = int(input("A: "))
    b = int(input("B: "))
    c = int(input("C: "))
    d = int(input("D: "))
    e = int(input("E: "))
    f = int(input("F: "))
    g = int(input("G: "))
    h = int(input("H: "))
    i = int(input("I: "))
    determinant = (a*(e*i-f*h)-b*(d*i-g*f)+c*(d*h-e*g))
    print(f"The 3x3 determinant of {np.matrix([[a,b,c],[d,e,f],[g,h,i]])} is {determinant})")
def main():
    print("Would you like to compute a 2x2 or 3x3 determinant?")
    user_inp = str(input("1 -> 2x2 or 2 -> 3x3: "))
    while user_inp != "1" or "2":
        if user_inp == "1":
            twodet()
            break
        if user_inp == "2":
            threedet()
            break
        else:
            "Please retry! :D"
main()
