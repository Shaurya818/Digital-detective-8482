# Mission 04 — How programs run

## 1. Task / objective

Create and run a simple Python program, then compare a compiler with an interpreter.

## 2. Work completed

Created `hello.py` with a one-line Python statement:

```python
print("Hello from Python")
```

Run it from the repository root with:

```bash
python3 mission-04-programs/hello.py
```

Expected output:

```text
Hello from Python
```

### Task 4.2 — Compiler and interpreter comparison

| Point | Compiler | Interpreter |
|---|---|---|
| When translation / execution happens | Usually translates the source program before it is run. | Executes instructions at runtime, often while reading or processing the program. |
| Typical output | May produce machine code or an executable file. | Usually runs the program through the interpreter; it may not create a standalone executable. |
| One example | Clang compiling a C program. | Python run using CPython. |
| One advantage | The compiled program can run without translating the source on every run. | It is convenient for trying code and getting feedback while developing. |

A compiler and an interpreter both help a computer run a program, but they handle translation differently. A compiler usually translates the source code before execution and can create an executable. An interpreter runs the program through an execution environment. Python's CPython implementation also compiles source code to bytecode internally, so real language implementations can use a mixture of both approaches.

## 3. Commands / tools used

- Text editor — created `hello.py`.
- `python3` — runs the Python program from Terminal.

## 4. My understanding

The `print()` function displays text in the Terminal. Running the file with `python3` asks the Python runtime to execute the program. A compiler and an interpreter are two common ways to translate or execute source code, although modern languages do not always fit into only one category.

## 5. Difficulties faced

[Write what happened when you ran the file. If it printed the expected message on the first try, write: No major difficulties.]

## 6. How I resolved them

[If there was an error, record the correction. If there was no error, write: Not applicable.]

## 7. Evidence / files

- `hello.py`
- This README
- Optional screenshot showing the command and output, with private paths cropped or redacted

## 8. Commit details

Suggested commit message: `Compare compilers and interpreters`

**GitHub status:** [Add the actual commit ID or link after pushing this mission.]
