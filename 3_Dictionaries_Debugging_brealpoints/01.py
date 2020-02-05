import ipdb as pdb

def functionWithBreakpoint():
    number = 4
    number += 3
    pdb.set_trace()
    number += 2
    return number


print functionWithBreakpoint()