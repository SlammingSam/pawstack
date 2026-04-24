import sys
import shlex

def run(code, debug):
    stack = []
    words = shlex.split(code)
    VALID_OPS = ["%", ">", "<", "==", "+", "-", "*", "/", 
                 "repeat", "lower", 
                 "int", "str", "float", 
                 "in", "yip", "eat", "paw-at", "dup", 
                 "pop-all", "bury", "dig", "rev"]

    for word in words:
        # numbers
        if word.replace('.', '', 1).isdigit():
            stack.append(float(word))

        # operations / keywords
        elif word in VALID_OPS:
            # addition
            if word == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)

            elif word == "-":
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
                stack.append(a == b) # compare for equality, push True/False

            elif word == ">":
                b = stack.pop()
                a = stack.pop()
                stack.append(a > b) # compare for greater than, push True/False

            elif word == "<":
                b = stack.pop()
                a = stack.pop()
                stack.append(a < b) # compare for less than, push True/False
            
            elif word == "%":
                b = stack.pop()
                a = stack.pop()

                a = int(a)
                b = int(b)
                stack.append(a % b) # modulus operator

            elif word == "in": # user input
                user_input = input()

                if user_input.isdigit(): # check if it's an integer
                    user_input = int(user_input)
                elif user_input.replace('.', '', 1).isdigit(): # check if it's a float
                    user_input = float(user_input)
                stack.append(user_input)

            elif word == "int": # convert top of stack to int
                value = stack.pop()
                stack.append(int(value))

            elif word == "str": # convert top of stack to string
                value = stack.pop()
                stack.append(str(value))
            
            elif word == "float": # convert top of stack to float
                value = stack.pop()
                stack.append(float(value))

            elif word == "lower": # convert top of stack to lowercase string
                value = stack.pop()
                stack.append(str(value).lower())

            elif word == "yip": # print top of stack and pop it
                print(stack.pop())
            
            elif word == "eat": # pop top of stack and discard it
                stack.pop()

            elif word == "paw-at": # print top of stack without popping it
                print(stack[-1])
            
            elif word == "dup": # duplicate top of stack
                stack.append(stack[-1])

            elif word == "pop-all": # dig up pops all values and prints them
                print("Popping all values:")
                while stack:
                    print(stack.pop())

            elif word == "rev":
                s = stack.pop()  # pop string off
                temp = [] # temp stack to hold chars in reverse order
                reversed = ""

                for ch in s: temp.append(ch) # put chars in temp stack
                while temp: reversed += temp.pop() # pop chars from temp, put in reversed string
                stack.append(reversed) # push reversed string back onto stack
            
            elif word == "repeat": # repeat the previous value a certain number of times
                count = int(stack.pop())
                value = stack.pop()
                stack.append(value * count) # repeat the value 'count' times and push the result back onto the stack

        else:
            stack.append(word)
        if debug:
            print(f"{word:>10} -> {stack}")

if __name__ == "__main__":
    is_debug = False

    filename = sys.argv[1]
    with open(filename, "r") as f:
        code = f.read()
    run(code, is_debug)