# a functon to make function
#

def parm_taker():
    parameter = input("Enter a parameter name: ")
    print("Parameter successfully set!")
    return parameter


def basicfn():


def functioner():
    is_parametarized = input("Will this function be paremarized?y/n: ")
    is_p = is_parametarized.upper()
    if (is_p == "Y"):
        #print('make a parametarized function')
        int nop = int(input("Enter the number of parameters: "))
        parameters = []
        for i in range(nop):
            
    elif (is_p == "N"):
        print("make a nonprematerixed fuction.")
    else:
        print("Hello World!")


functioner()