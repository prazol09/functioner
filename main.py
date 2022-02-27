# a functon to make function
#

def functioner():
    is_parametarized = input("Will this function be paremarized?y/n: ")
    is_p = is_parametarized.upper()
    if (is_p == "Y"):
        print('make a pparametarized function')
    elif (is_p == "N"):
        print("make a nonprematerixed fuction.")
    else:
        print("Hello World!")


functioner()