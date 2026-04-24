# 🐾 PawStack

A stack-based, concatenative programming language with a cat-themed twist. Push values, chain operations, and let the stack do the thinking.

---

## Getting Started

```bash
python pawstack.py your_program.paw
```

Enable debug mode to print the stack after every operation:

```bash
# Set is_debug = True in pawstack.py, then run normally
python pawstack.py your_program.paw
```

---

## How It Works

PawStack is a **stack-based language** — all data lives on a stack. Words (tokens) are processed left to right. Numbers and strings are pushed onto the stack; operations consume values from the top and push results back.

```
3 4 +   →  pushes 3, pushes 4, pops both and pushes 7
```

Strings are written with quotes:

```
"hello" " world" +   →  pushes "hello world"
```

---

## Operations

### Arithmetic

| Word | Description                                |
| ---- | ------------------------------------------ |
| `+`  | Add top two values                         |
| `-`  | Subtract: `a b -` → `a - b`                |
| `*`  | Multiply top two values                    |
| `/`  | Divide: `a b /` → `a / b`                  |
| `%`  | Modulus: `a b %` → `a % b` (integers only) |

### Comparison

| Word | Description                             |
| ---- | --------------------------------------- |
| `==` | Push `True` if top two values are equal |
| `>`  | Push `True` if second-from-top > top    |
| `<`  | Push `True` if second-from-top < top    |

### Stack Manipulation

| Word      | Description                           |
| --------- | ------------------------------------- |
| `dup`     | Duplicate the top of the stack        |
| `eat`     | Pop and discard the top value         |
| `pop-all` | Pop and print all values on the stack |

### Output & Input

| Word     | Description                                                          |
| -------- | -------------------------------------------------------------------- |
| `yip`    | Pop and print the top value                                          |
| `paw-at` | Print the top value without removing it                              |
| `in`     | Read a line of user input; auto-converts to int or float if possible |

### Type Conversion

| Word    | Description                              |
| ------- | ---------------------------------------- |
| `int`   | Convert top of stack to integer          |
| `float` | Convert top of stack to float            |
| `str`   | Convert top of stack to string           |
| `lower` | Convert top of stack to lowercase string |

### String Operations

| Word     | Description                                                                 |
| -------- | --------------------------------------------------------------------------- |
| `repeat` | `value count repeat` — repeat a string (or multiply a number) `count` times |
| `rev`    | Reverse the string on top of the stack                                      |

---

## Examples

### Hello, World

```
"Hello, World!" yip
```

### Basic Math

```
10 3 % yip
```

Output: `1`

### String Repeat

```
"meow " 3 repeat yip
```

Output: `meow meow meow `

### Reverse a String

```
"paws" rev yip
```

Output: `swap`

### User Input & Echo

```
in yip
```

Reads a line from stdin and prints it back.

### Duplicate & Operate

```
5 dup * yip
```

Output: `25.0`  
_(duplicates 5, then multiplies 5 × 5)_

---

## Debug Mode

Set `is_debug = True` in `pawstack.py` to trace every operation:

```
      5 -> [5]
    dup -> [5, 5]
      * -> [25.0]
    yip -> []
```

Each line shows the word just processed and the resulting stack state.

---

## Notes

- All numbers are stored internally as **floats**. Use `int` to convert when needed.
- `shlex.split` is used for tokenizing, so **quoted strings with spaces** work correctly.
- There are no variables, loops, or conditionals in the current version — PawStack is intentionally minimal.

---

_Stack responsibly. 🐾_
