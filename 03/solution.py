import os

PATH = os.path.dirname(os.path.realpath(__file__))

def parse_input(file="input"):
    res = []
    with open(PATH + "/" + file) as f:
        for line in f:
            res.append(line.split(','))
    return res

def calc_collisions(wire_one, wire_two):
    collisions = set()
    for point in wire_one:
        if point in wire_two:
            collisions.add(point)
    return collisions

def calc_distance(a, b):

    return abs(a) + abs(b)


moves = {
    'U':(1,0),
    'D':(-1,0),
    'L':(0,-1),
    'R':(0,1),
}

def generate_wire(steps):
    x = y = 0
    wire = []
    for step in steps:
        m_x, m_y = moves[step[0]]
        for i in range(int(step[1:])):
            x += m_x
            y += m_y
            wire.append((x,y))  
    return wire

def main():
    inputs = parse_input('test-input')
    inputs = parse_input()
    wire_one = generate_wire(inputs[0])
    wire_two = generate_wire(inputs[1])
    collisions = set(wire_one) & set(wire_two)
    distance = min(abs(a)+abs(b) for (a,b) in collisions)
    print(distance)
    print(2 + min(sum(wire.index(collision) for wire in (wire_one, wire_two)) for collision in collisions))

if __name__ == "__main__":
    main()
    