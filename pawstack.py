import sys
import shlex
def run(code, debug):
    stack = []
    words = shlex.split(code)
    VALID_OPS = ["%", ">", "<", "==", "+", "-", "*", "/", "repeat", "lower", "int", "str", "float", "in", "yip", "eat", "paw-at", "dup", "pop-all", "rev"]
    for word in words:
        if word.replace('.', '', 1).isdigit():          # checks if number, if not, checks if operator
            stack.append(float(word))                   # the replace also removes the decimal for float so it can be seen as a number
        elif word in VALID_OPS:                         # operations / keywords
            if word == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif word == "-":                           # do I really need to explain basic math? 
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif word == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif word == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(a / b)
            elif word == "==":
                b = stack.pop()
                a = stack.pop()
                stack.append(a == b)                    # compare for equality, push True/False
            elif word == ">":
                b = stack.pop()
                a = stack.pop()
                stack.append(a > b)                     # compare for greater than, push True/False
            elif word == "<":
                b = stack.pop()
                a = stack.pop()
                stack.append(a < b)                     # compare for less than, push True/False
            elif word == "%":
                b = stack.pop()
                a = stack.pop()
                a = int(a)
                b = int(b)
                stack.append(a % b)                     # modulus, gets the remainder
            elif word == "in":                          # user input
                user_input = input()
                if user_input.isdigit(): user_input = int(user_input)                           # check if it's an integer 
                elif user_input.replace('.', '', 1).isdigit(): 
                    user_input = float(user_input)      # check if it's a float
                stack.append(user_input)
            elif word == "int":                         # convert top of stack to int
                value = stack.pop()
                stack.append(int(value))
            elif word == "str":                         # convert top of stack to string
                value = stack.pop()
                stack.append(str(value))
            elif word == "float":                       # convert top of stack to float
                value = stack.pop()
                stack.append(float(value))
            elif word == "lower":                       # convert top of stack to lowercase string
                value = stack.pop()
                stack.append(str(value).lower())
            elif word == "yip": print(stack.pop())      # print top of stack and pop it
            elif word == "eat": stack.pop()             # pop top of stack and discard it
            elif word == "paw-at": print(stack[-1])     # print top of stack without popping it
            elif word == "dup": stack.append(stack[-1]) # duplicate top of stack
            elif word == "pop-all":                     # dig up pops all values and prints them
                print("Popping all values:")
                while stack: print(stack.pop())
            elif word == "rev":
                s = stack.pop()                         # pop string off
                temp = []                               # temp stack to hold chars in reverse order
                reversed = ""
                for ch in s: temp.append(ch)            # put chars in temp stack
                while temp: reversed += temp.pop()      # pop chars from temp, put in reversed string
                stack.append(reversed)                  # push reversed string back onto stack
            elif word == "repeat":                      # repeat the previous value a certain number of times
                count = int(stack.pop())
                value = stack.pop()
                stack.append(value * count)             # repeat the value 'count' times and push the result back onto the stack
        else: stack.append(word)
        if debug: print(f"{word:>10} -> {stack}")
if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, "r") as f: code = f.read()
    run(code, False)