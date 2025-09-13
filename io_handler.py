#io.py

memorySize = 100
def load_program(filename):
    memory = [0] * memorySize
    with open(filename, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        clean = line.split("//")[0].strip()
        if clean:
            memory[i] = int(clean)
    return memory


def run_program(memory):
    counter = 0
    while True:
        instruction = memory[counter]
        operation = instruction // 100
        memLocation = instruction % 100
        if operation == 10:
            memory[memLocation] = int(input(f"Type a word: [{memLocation}]: "))
        elif operation == 11:
            print(memory[memLocation]) #Write to screen
        else:
            break
        counter += 1
