def path(w):
    paths = [(0,0)]
    for instr in w:
        prev = paths[-1]
        d = instr[0]
        delta = int(instr[1:]) + 1
        if d == 'R': lst = [(prev[0] + i, prev[1]) for i in range(1, delta)]
        if d == 'L': lst = [(prev[0] - i, prev[1]) for i in range(1, delta)]
        if d == 'D': lst = [(prev[0], prev[1] - i) for i in range(1, delta)]
        if d == 'U': lst = [(prev[0], prev[1] + i) for i in range(1, delta)]
        paths += lst
    
    return paths

def man_distance(P, Q):
    return sum(abs(p-q) for p, q in zip(P, Q))

if __name__ == "__main__":
    w1, w2 = open('input3.txt', 'r').read()[:-1].split('\n')
    #w1 = "U7,R6,D4,L4"
    #w2 = "R8,U5,L5,D3"
    w1 = w1.split(',')
    w2 = w2.split(',')
    w1_paths = path(w1)
    w2_paths = path(w2)

    w1_upaths = set(w1_paths)
    w2_upaths = set(w2_paths)

    intersections = w1_upaths.intersection(w2_upaths)
    intersections.remove((0,0))

    closest = min(man_distance((0,0), i) for i in intersections)
    fewest_steps = min(w1_paths.index(i) + w2_paths.index(i) for i in intersections)

    print(f"Distance: {closest}")
    print(f"Steps: {fewest_steps}")