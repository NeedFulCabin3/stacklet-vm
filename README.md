# Stacklet VM

A minimal virtual machine implemented in Python that combines an internal data stack with a primary working register. It parses and executes simple text-based assembly commands out of a file or an array of strings. 

This project shows how instruction pointers, registers, and memory stacks interact under the hood without the bloat of real-world hardware architectures.

## Key Features

* **Hybrid Architecture:** Uses a single working register alongside an explicit stack structure.
* **Text Assembly Parser:** Directly processes uppercase textual instructions (`LOAD`, `PUSH`, `ADD`) instead of  binary opcodes.
* **Automatic Error Catching:** Includes stack underflow protection for mathematical and pop operations.
* **Zero Dependencies:** Runs entirely on standard Python libraries.

## Tech Stack Breakdown

* **Language:** Python 3.x
* **Runtime Components:** Program counter (`pc`), Data stack (`stack`), Working register (`register`).

## How It Works Under the Hood

The machine uses a basic read-evaluate-print loop style execution flow:



1.  The `program counter` points to the current line index.
2.  The text string is stripped, tokenized, and mapped to instruction branches.
3.  Mathematical execution occurs either directly on the primary register using literal values, or dynamically against the top value of the stack.

## Prerequisites & Web-Based Quick Start

You don't need a local development environment to play around with this.

### Option A: Use GitHub Codespaces (100% In-Browser)
1.  Click the green **Code** button at the top of this repository.
2.  Select the **Codespaces** tab and click **Create codespace on main**.
3.  Once the browser editor loads, run the code in the integrated terminal:
    ```bash
    python main.py
    ```

### Option B: Local Setup
If you prefer running it locally, make sure you have Python 3 installed.
```bash
# Clone the repository (or download the zip file from your browser)
git clone [https://github.com/YOUR_USERNAME/stacklet-vm.git](https://github.com/YOUR_USERNAME/stacklet-vm.git)
cd stacklet-vm

# Run the script directly
python main.py
```

## Instruction Set Architecture (ISA)
```
| Instruction | Argument | Description |
| :--- | :--- | :--- |
| **`LOAD`** | `value` | Loads an integer directly into the register. |
| **`PUSH`** | *None* | Pushes the current register value onto the stack. |
| **`POP`** | *None* | Pops the top value off the stack and copies it into the register. |
| **`ADD`** | `[value]` | Adds an argument (if provided) or pops the top stack item and adds it to the register. |
| **`SUB`** | `[value]` | Subtracts an argument (if provided) or pops the top stack item from the register. |
| **`PRINT`** | *None* | Outputs the current register status to stdout. |
| **`PRINT_STACK`** | *None* | Outputs the complete list array of the current stack state. |
```

## Project Structure
```
stacklet-vm/
├── .github/
│   └── workflows/
│       └── ci.yml      # Automated integration routine
├── .gitignore          # Keeps build trash out of the repo
├── main.py             # Single-file virtual machine implementation
└── README.md           # Documentation
```

## Roadmap
[ ] Add JUMP and JUMP_IF_ZERO commands to handle execution branching and conditional loops.

[ ] Implement a custom file reader to handle external script files via command-line flags.

[ ] Write a secondary script to compile a slightly higher-level pseudo-code into this VM's native syntax.
