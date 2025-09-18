
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
    accumulator = 0
    counter = 0
    while True:
        instruction = memory[counter]
        operation = instruction // 100
        memLocation = instruction % 100
        if operation == 10: #READ OPERATION
            memory[memLocation] = int(input(f"Enter a value [{memLocation}]: "))
        elif operation == 11: #WRITE TO SCREEN OPERATION
            print(memory[memLocation]) 
         elif operation == 20: #LOAD OPERATION
            #Loads value from specified memory location into accumulator
            accumulator = memory[memLocation]
        elif operation == 21: #STORE OPERATION
            #Stores value currently held by accumulator into specified memory location
            memory[memLocation] = accumulator
         elif operation == 30: #ADD OPERATION
            accumulator += memory[operand]
        elif operation == 31: #SUBTRACT OPERATION
            accumulator -= memory[memLocation]
        elif operation == 32: #DIVIDE OPERATION
            if memory[memLocation] == 0:
                print("can't divide by zero")
                break
            accumulator //= memory[memLocation]
        elif operation == 33: #MULTIPLY OPERATION
            accumulator *= memory[memLocation]
        elif operation == 43:
            break
        else:
            break
        counter += 1


def main():
    filename = input("Enter the Basic ML file name: ")
    memory = load_program(filename)
    run_program(memory)

main()
