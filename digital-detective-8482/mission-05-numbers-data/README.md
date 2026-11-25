# Mission 05 — Numbers and data

## 1. Task / objective

Convert values between decimal, binary and hexadecimal, verify the conversions with Python, write a small number converter and explain basic text encoding.

## 2. Work completed

### Task 5.1 — Manual conversions

| Question | Working | Answer |
|---|---|---|
| Decimal 13 to binary | 13 = 8 + 4 + 1 = `1101` in base 2. | `1101` |
| Decimal 25 to binary | 25 = 16 + 8 + 1 = `11001` in base 2. | `11001` |
| Binary `1010` to decimal | (1 × 8) + (0 × 4) + (1 × 2) + (0 × 1) = 10. | `10` |
| Binary `1101` to decimal | (1 × 8) + (1 × 4) + (0 × 2) + (1 × 1) = 13. | `13` |
| Hexadecimal `A` to decimal | A represents 10 in hexadecimal. | `10` |
| Hexadecimal `1F` to decimal | (1 × 16) + 15 = 31. | `31` |
| Binary `1111` to hexadecimal | `1111` is 15 in decimal; 15 is `F` in hexadecimal. | `F` |

### Task 5.2 — Python verification

The following expressions use Python's built-in functions. The results shown are the expected results and can be checked in the Python interactive environment.

| Expression | Result | Matches manual calculation? |
|---|---|---|
| `bin(13)` | `'0b1101'` | Yes |
| `bin(25)` | `'0b11001'` | Yes |
| `int('1010', 2)` | `10` | Yes |
| `int('1101', 2)` | `13` | Yes |
| `hex(25)` | `'0x19'` | Yes; 25 is `19` in hexadecimal |
| `int('1F', 16)` | `31` | Yes |
| `int('1111', 2)` | `15` | Yes; 15 is `F` in hexadecimal |

`bin()` converts an integer to a binary string with the `0b` prefix. `hex()` converts an integer to hexadecimal with the `0x` prefix. `int(value, base)` reads a string using the given base and returns its decimal integer value.

### Task 5.3 — Number converter

The program is in `number_converter.py`. It asks for a non-negative whole number and prints the binary and hexadecimal forms. It handles text that cannot be converted to an integer and rejects negative input because the assignment asks for positive test values.

Test cases:

| Input | Binary output | Hexadecimal output |
|---:|---|---|
| 13 | `0b1101` | `0xd` |
| 25 | `0b11001` | `0x19` |
| 31 | `0b11111` | `0x1f` |

Run it with:

```bash
python3 mission-05-numbers-data/number_converter.py
```

### Task 5.4 — How text is stored

- Uppercase `A` has ASCII decimal code **65**.
- Lowercase `a` has ASCII decimal code **97**.
- A computer needs an encoding standard so that a byte sequence can be interpreted as particular characters in a consistent way. Without an agreed encoding, the same stored data could be displayed as different or incorrect characters.
- An example of a character outside basic ASCII is `₹` (Indian rupee sign). UTF-8 can represent it.

## 3. Commands / tools used

- Python interactive mode — checks conversion expressions.
- `bin()` — converts an integer to a binary string.
- `hex()` — converts an integer to a hexadecimal string.
- `int(value, base)` — converts a string from a specified base to an integer.
- `input()` — reads the user's number in the converter.
- `python3` — runs the converter from Terminal.

## 4. My understanding

Decimal uses ten digits, binary uses two digits and hexadecimal uses sixteen symbols (0–9 and A–F). The same number can be written in each system; only its representation changes. Python has built-in functions that make it easier to convert between these forms. Text also needs a character encoding so stored bytes can be mapped back to letters and symbols.

## 5. Difficulties faced

[Run the converter with the three test values. Record any issue that actually occurs. If it works as expected, write: No major difficulties.]

## 6. How I resolved them

[Record the correction, if any. If there was no issue, write: Not applicable.]

## 7. Evidence / files

- `number_converter.py`
- This README with manual calculations and Python checks
- Optional screenshot of three successful test runs in `evidence/`

## 8. Commit details

Suggested commit message: `Build number converter and practise data representation`

**GitHub status:** [Add the actual commit ID or link after pushing this mission.]
