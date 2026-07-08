import sys

class VirtualMachine:
    def __init__(self):
        self.stack = []
        self.register = 0
        self.pc = 0  # Program counter

    def execute(self, instructions):
        self.pc = 0
        while self.pc < len(instructions):
            line = instructions[self.pc].strip()
            
            # Skip empty lines and comments
            if not line or line.startswith('#'):
                self.pc += 1
                continue

            parts = line.split()
            command = parts[0].upper()
            args = parts[1:]

            if command == "LOAD":
                self.register = int(args[0])
            elif command == "PUSH":
                self.stack.append(self.register)
            elif command == "POP":
                if not self.stack:
                    print("VM Error: Stack underflow on POP")
                    return
                self.register = self.stack.pop()
            elif command == "ADD":
                val = int(args[0]) if args else None
                if val is not None:
                    self.register += val
                else:
                    if len(self.stack) < 1:
                        print("VM Error: Stack underflow on ADD")
                        return
                    self.register += self.stack.pop()
            elif command == "SUB":
                val = int(args[0]) if args else None
                if val is not None:
                    self.register -= val
                else:
                    if len(self.stack) < 1:
                        print("VM Error: Stack underflow on SUB")
                        return
                    self.register -= self.stack.pop()
            elif command == "PRINT":
                print(f"[REG]: {self.register}")
            elif command == "PRINT_STACK":
                print(f"[STACK]: {self.stack}")
            else:
                print(f"VM Error: Unknown instruction '{command}'")
                return

            self.pc += 1

def run_program_from_file(filename):
    vm = VirtualMachine()
    try:
        with open(filename, 'r') as f:
            instructions = f.readlines()
        vm.execute(instructions)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if __name__ == "__main__":
    # Example inline assembly logic to test it out directly
    sample_program = [
        "LOAD 10",
        "PUSH",
        "LOAD 5",
        "ADD",         # Adds top of stack (10) to register (5) -> register is 15
        "PRINT",
        "SUB 3",       # Subtracts 3 from register -> register is 12
        "PRINT",
        "PUSH",
        "PRINT_STACK"
    ]

    print("Running internal sample program:")
    vm = VirtualMachine()
    vm.execute(sample_program)
