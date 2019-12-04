def required_fuel(mass):
    fuel = mass//3 - 2
    if fuel <= 0:
        return 0 
    return fuel + required_fuel(fuel)

if __name__ == "__main__":
#Part one
    modules = open('input1.txt', 'r').read().split('\n')[:-1]
    print(f"Sum = {sum(int(mass)//3 - 2 for mass in modules)}")

#Part two
    print(f"Sum = {sum(required_fuel(int(mass)) for mass in modules)}")
