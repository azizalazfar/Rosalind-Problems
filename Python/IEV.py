import argparse
from timeit import default_timer as timer

with open('rosalind_iev.txt') as file:
    p1, p2, p3, p4, p5, p6 = (file.read().split(' '))


# Probabilities
def offsprings(p1, p2, p3, p4, p5, p6):
    return (int(p1) + int(p2) + int(p3) + int(p4)*.75 + int(p5)*0.5 + int(p6)*0.0)*2

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'input the content of rosalind_iev.txt file here' )
    parser.add_argument('popul')
    start = timer()
    print(off)