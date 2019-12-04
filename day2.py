def read_opcode(noun, verb):
    codes = [int(i) for i in open('input2.txt', 'r').read().strip().split(',')]
    codes[1] = noun
    codes[2] = verb

    curr = 0
    while True:
        opcode = codes[curr]
        if opcode == 1:
            codes[codes[curr + 3]] = codes[codes[curr + 1]] + codes[codes[curr + 2]]
        elif opcode == 2:
            codes[codes[curr + 3]] = codes[codes[curr + 1]] * codes[codes[curr + 2]]
        elif opcode == 99:
            break
        else:
            print("\n\n")
            print(curr)
            print(codes[curr])
            print(codes)
            raise ValueError("Fejl")
        curr += 4
    
    return codes[0]

if __name__ == "__main__":
    i=0
    for noun in range(100):
        for verb in range(100):
            print("\r i = " + str(i + 1), flush = True, end = "")
            i += 1
            try:
                output = read_opcode(noun, verb)
            except:
                pass
            if output == 19690720:
                print(f"\n\nNoun:\t{noun}\nVerb:\t{verb}")
                break
        if output == 19690720: break