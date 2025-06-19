#!/usr/bin/python3

def brainfuck_interpreter(code):
    code = ''.join(filter(lambda x: x in ['>', '<', '+', '-', '.', ',', '[', ']'], code))
    tape, ptr, output, i = [0] * 30000, 0, '', 0

    def jump_forward(pc):
        open_brackets = 1
        while open_brackets:
            pc += 1
            if code[pc] == '[': open_brackets += 1
            elif code[pc] == ']': open_brackets -= 1
        return pc

    def jump_backward(pc):
        open_brackets = 1
        while open_brackets:
            pc -= 1
            if code[pc] == ']': open_brackets += 1
            elif code[pc] == '[': open_brackets -= 1
        return pc

    while i < len(code):
        cmd = code[i]
        if cmd == '>':
            ptr += 1
        elif cmd == '<':
            ptr -= 1
        elif cmd == '+':
            tape[ptr] = (tape[ptr] + 1) % 256
        elif cmd == '-':
            tape[ptr] = (tape[ptr] - 1) % 256
        elif cmd == '.':
            output += chr(tape[ptr])
        elif cmd == ',':
            pass  # Input not required for this example
        elif cmd == '[' and tape[ptr] == 0:
            i = jump_forward(i)
        elif cmd == ']' and tape[ptr] != 0:
            i = jump_backward(i)
        i += 1
    return output

# Example usage
code = "++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>++++.>--.>+++++.+++++.---.++++++++++++++.<<--.>++++++++++++++.+++++++++++++++++++.----.+++++++++++.<+++++++++++++.>>-----.<---.++++.--------.<-------------.>----------------------------------.>-----.--.+++.+++++.-.-----------.+++++.-------.<<.>+++++++++++++.>+++++.-----------.+++++++++++++++++++.--------------.+++++++++.+++.-----.<<++.--.++.>----------.>++.+++.-----------.++++++++.+++++.<<--.>++++++++++.+++++++++++++++++.>-..++++.--------.+++.<+++.<++."
result = brainfuck_interpreter(code)
print(f"Decoded output: {result}")