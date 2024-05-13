Sequence = [13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,79, 83, 97] #This is the sequence of numbers that we will search through
Targets = 53 #This is the target number we are trying to find
def search_binary(sequence, target):
    lower_bound = 0
    upper_bound = len(sequence)
    probes = 0
    while lower_bound < upper_bound:
        index = (lower_bound + upper_bound )//2
        probes = probes + 1
        
        if sequence[index] == target:
            print(index + probes)
        if sequence[index] > target:
            upper_bound = index
        else:
            lower_bound = index + 1
        
    print(probes, sequence[index])

def main():
    search_binary(Sequence, Targets)


if __name__ == '__main__':
    main()