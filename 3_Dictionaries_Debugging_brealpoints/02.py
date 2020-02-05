import ipdb as pdb

def functionWithBreakpoint():
    number = 0
    for i in range(10):
        number += i
        
        pdb.set_trace()
    
    return number


if __name__ == "__main__":
    print functionWithBreakpoint()