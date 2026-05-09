# C7 Notes: Python for Security Analysts

---

## Why Python in Cybersecurity

Python is a general-purpose, interpreted programming language widely used in security for **automation** — reducing manual effort on repetitive tasks.

**Common cybersecurity applications:**
- Log analysis
- Malware analysis
- Access control list management
- Intrusion detection
- Compliance checks
- Network scanning

**How it works**: Python code is processed line-by-line by an **interpreter**, which translates it into binary instructions the CPU can execute. Python 3 is the current standard.

**Python environments:**
- **Notebooks** (Jupyter, Google Colab) — Interactive; code cells run code, markdown cells document it
- **IDEs** — Graphical editors with error correction tools (e.g., VS Code, JetBrains)
- **Command line** — Run `.py` files directly from the terminal

---

## Data Types

| Data Type | Description | Example |
|-----------|-------------|---------|
| `str` | Ordered sequence of characters in quotes | `"192.168.1.1"` |
| `int` | Whole number, no decimal | `5`, `-100` |
| `float` | Number with decimal point | `3.14`, `-2.2` |
| `bool` | Only `True` or `False` | `True` |
| `list` | Ordered, mutable collection in `[]` | `["user1", "user2"]` |
| `tuple` | Ordered, immutable collection in `()` | `("admin", "guest")` |
| `dict` | Key-value pairs in `{}` | `{1: "East", 2: "West"}` |
| `set` | Unordered collection of unique values | `{"user1", "user2"}` |

```python
# String
username = "jdoe"

# Integer
login_attempts = 5

# Float
success_rate = 0.85

# Boolean
is_locked = False

# List
ip_addresses = ["192.168.1.1", "10.0.0.2"]

# Tuple (immutable — good for fixed access control lists)
blocked_software = ("malware.exe", "spyware.dll")

# Dictionary
building_map = {1: "East", 2: "West", 3: "North"}

# Set (unique values only)
active_users = {"jdoe", "bmoreno", "tshah"}

# Check data type
print(type(login_attempts))   # <class 'int'>
```

**Division notes:**
```python
print(1 / 4)    # 0.25  (float result)
print(1 // 4)   # 0     (integer — rounds down)
```

---

## Variables

A variable is a named container that stores data. Python automatically assigns the data type.

```python
# Assign
username = "nzhao"

# Reassign
username = "zhao2"

# Assign one variable to another
old_username = username   # old_username = "zhao2"
```

**Naming rules:**
- Only letters, numbers, and underscores: `login_attempts`, `device_id`
- Case-sensitive: `time`, `Time`, and `TIME` are different variables
- No Python reserved keywords: avoid `True`, `False`, `if`, `for`, etc.
- Use underscores for multi-word names: `failed_login_count`
- Make names descriptive: `num_login_attempts` not `x`

---

## Conditional Statements

Conditional statements evaluate whether a condition is `True` or `False` and act accordingly.

**Comparison operators:**

| Operator | Meaning |
|----------|---------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

### if / elif / else

```python
status = 200

if status == 200:
    print("OK")
elif status == 400:
    print("Bad Request")
elif status == 500:
    print("Internal Server Error")
else:
    print("Check other status")
```

> Note: Python checks `elif` in order and stops at the first `True`. Multiple `elif` blocks will not all run, unlike multiple `if` blocks which all get evaluated independently.

### Logical Operators

```python
# and — both conditions must be True
if status >= 200 and status <= 226:
    print("Successful response")

# or — at least one condition must be True
if status == 100 or status == 102:
    print("Informational response")

# not — inverts the condition
if not(status >= 200 and status <= 226):
    print("Check status")   # prints if status is outside 200–226
```

---

## Iterative Statements (Loops)

### for loops — iterate over a sequence

```python
computer_assets = ["laptop1", "desktop20", "smartphone03"]

for asset in computer_assets:
    print(asset)
# Output: laptop1 / desktop20 / smartphone03

# Iterate over a string (one character at a time)
for char in "security":
    print(char)

# range(start, stop, increment) — stop is excluded
for i in range(0, 5, 1):
    print(i)   # 0, 1, 2, 3, 4

# Simplified with defaults (start=0, increment=1)
for i in range(5):
    print(i)
```

### while loops — iterate based on a condition

```python
i = 1
while i < 5:
    print(i)
    i += 1   # must update the variable or the loop runs forever
# Output: 1, 2, 3, 4

# Track login attempts
login_attempts = 0
while login_attempts < 5:
    print("Login attempt:", login_attempts)
    login_attempts += 1

# Using a Boolean condition
login_status = True
count = 0

while login_status == True:
    print("Try again.")
    count += 1
    if count == 4:
        login_status = False
```

### Loop control: break and continue

```python
assets = ["laptop1", "desktop20", "smartphone03"]

# break — exit the loop when condition is met
for asset in assets:
    if asset == "desktop20":
        break
    print(asset)
# Output: laptop1

# continue — skip current iteration, continue with the next
for asset in assets:
    if asset == "desktop20":
        continue
    print(asset)
# Output: laptop1 / smartphone03
```

> **Infinite loops**: If a `while` loop's condition never becomes `False`, press `CTRL-C` or `CTRL-Z` to stop it.

---

## Functions

A function is a reusable section of code. Functions reduce repetition and are essential for automation.

### Defining and calling

```python
# Define with the def keyword
def display_investigation_message():
    print("Investigate activity")

# Call it anywhere in your code
display_investigation_message()
# Output: Investigate activity
```

### Parameters and arguments

```python
# Parameters = placeholders in the function definition
def remaining_login_attempts(maximum_attempts, total_attempts):
    print(maximum_attempts - total_attempts)

# Arguments = actual values passed when calling
remaining_login_attempts(3, 2)   # Output: 1
```

### Return statements

```python
def remaining_login_attempts(maximum_attempts, total_attempts):
    return maximum_attempts - total_attempts   # returns result to caller

remaining = remaining_login_attempts(3, 3)

if remaining <= 0:
    print("Your account is locked")
# Output: Your account is locked
```

> `return` exits the function immediately. Any code after it inside the function will not run.

### Global vs. local variables

```python
username = "elarson"   # global — accessible throughout the program

def identify_user():
    username = "bmoreno"   # local — only exists inside this function
    print(username)        # prints "bmoreno"

identify_user()
print(username)   # prints "elarson" — global is unchanged
```

> Best practice: pass values via **parameters** rather than relying on global variables inside functions. Reusing the same name globally and locally in the same function creates two separate variables and is a common source of bugs.

---

## Built-in Functions

```python
# print() — output to screen
print("Security alert", 42, True)

# type() — return the data type
print(type("security"))   # <class 'str'>
print(type(7))            # <class 'int'>

# type() inside print() — a common pattern
print(type("security"))   # str

# len() — number of elements in a string or list
print(len("h32rb17"))         # 7
print(len(["a", "b", "c"]))   # 3

# str() — convert to string (useful for IDs you need to slice)
string_id = str(19329302)
print(string_id[0:3])   # 193

# max() and min() — largest/smallest value
session_times = [12, 45, 3, 89, 27]
print(max(session_times))   # 89
print(min(session_times))   # 3

# sorted() — returns a sorted list in ascending order; original unchanged
time_list = [12, 45, 3, 89, 27]
print(sorted(time_list))   # [3, 12, 27, 45, 89]
print(time_list)           # [12, 45, 3, 89, 27] — unchanged
```

---

## Importing Modules and Libraries

### Python Standard Library

```python
# Import entire module
import statistics

monthly_failures = [15, 20, 25, 178, 12, 18, 24, 19, 22, 16, 31, 20]
print(statistics.mean(monthly_failures))     # 35.25
print(statistics.median(monthly_failures))   # 20.5

# Import only specific functions (no module prefix needed)
from statistics import mean, median
print(mean(monthly_failures))
print(median(monthly_failures))
```

**Useful Standard Library modules for security:**

| Module | Purpose |
|--------|---------|
| `re` | Regular expressions — search patterns in logs |
| `csv` | Read and write CSV files |
| `os`, `glob` | Interact with the file system and command line |
| `datetime`, `time` | Work with timestamps |
| `statistics` | Statistical calculations on numeric data |

### External libraries

```python
# Install first (run in Jupyter or Google Colab)
%pip install numpy

# Then import
import numpy
```

---

## Strings

### Indexing and slicing

```python
device_id = "h32rb17"

# Indices start at 0
print(device_id[0])      # h
print(device_id[3])      # r

# Negative indices count from the end
print(device_id[-1])     # 7

# Slicing — start is inclusive, end is exclusive
print(device_id[0:3])    # h32  (indices 0, 1, 2)
```

**Index table for** `"h32rb17"`:

| Char | + Index | - Index |
|------|---------|---------|
| h | 0 | -7 |
| 3 | 1 | -6 |
| 2 | 2 | -5 |
| r | 3 | -4 |
| b | 4 | -3 |
| 1 | 5 | -2 |
| 7 | 6 | -1 |

### String methods

```python
dept = "Information Technology"

print(dept.upper())          # INFORMATION TECHNOLOGY
print(dept.lower())          # information technology
print(len(dept))             # 22

# .index() — returns index of first occurrence
print("h32rb17".index("r"))  # 3

# Only returns the FIRST match
print("r45rt46".index("r"))  # 0  (not 3)

# Find a substring's starting index
log = "tsnow, tshah, bmoreno"
print(log.index("tshah"))    # 7

# str() — convert integer to string for slicing
string_id = str(19329302)
print(string_id[0:3])        # 193

# len() — verify string length
device_id = "h32rb17"
if len(device_id) == 7:
    print("Valid device ID format")
```

---

## Lists

### Indexing, slicing, and modifying

```python
username_list = ["elarson", "fgarcia", "tshah", "sgilmore"]

# Access by index
print(username_list[2])       # tshah

# Slice — returns a new sublist
print(username_list[0:2])     # ["elarson", "fgarcia"]

# Modify an element (lists are mutable; strings are not)
username_list[1] = "bmoreno"
print(username_list)          # ["elarson", "bmoreno", "tshah", "sgilmore"]
```

### List methods

```python
username_list = ["elarson", "fgarcia", "tshah", "sgilmore"]

# .insert(index, element) — insert at specific position; shifts others right
username_list.insert(2, "wjaffrey")
print(username_list)
# ["elarson", "fgarcia", "wjaffrey", "tshah", "sgilmore"]

# .remove(element) — removes first occurrence only
username_list.remove("elarson")
print(username_list)

# .append(element) — add to end
username_list.append("btang")
print(username_list)

# .index(element) — find index of first occurrence
print(username_list.index("tshah"))   # returns the index number

# Build a list dynamically using .append() in a loop
numbers_list = []
for i in range(5):
    numbers_list.append(i)
print(numbers_list)   # [0, 1, 2, 3, 4]
```

---

## Regular Expressions

Used to search for complex patterns (IP addresses, device IDs, usernames) in strings.

```python
import re   # must import before use
```

### Character type symbols

| Symbol | Matches |
|--------|---------|
| `\w` | Any alphanumeric character or underscore (`A-Z`, `a-z`, `0-9`, `_`) |
| `\d` | Any single digit `0–9` |
| `\s` | Any whitespace (space, tab, newline) |
| `.` | Any single character except newline |
| `\.` | A literal period (backslash escapes the special meaning) |

### Quantifier symbols

| Symbol | Meaning | Example |
|--------|---------|---------|
| `+` | One or more occurrences | `\d+` matches `1`, `12`, `12345` |
| `*` | Zero or more occurrences | |
| `{n}` | Exactly n occurrences | `\d{4}` matches `1234` |
| `{m,n}` | Between m and n occurrences | `\d{1,3}` matches `1`, `12`, `123` |

### re.findall() — returns a list of all matches

```python
import re

device_id = "h32rb17"

# Match all alphanumeric characters one at a time
print(re.findall("\w", device_id))
# ['h', '3', '2', 'r', 'b', '1', '7']

# Match all single digits
print(re.findall("\d", device_id))
# ['3', '2', '1', '7']

# Match one or more consecutive digits (groups them)
print(re.findall("\d+", device_id))
# ['32', '17']

# Match exactly two consecutive digits
ids = "ID01 ID123 ID9 ID45"
print(re.findall("\d{2}", ids))
# ['01', '12', '45']

# Match between 1 and 3 digits
print(re.findall("\d{1,3}", "ID0 ID32 ID825"))
# ['0', '32', '825']

# Extract username + login count from a log
employee_logins = "1001 bmoreno: 12 Marketing 1002 tshah: 7 Human Resources"
print(re.findall("\w+:\s\d+", employee_logins))
# ['bmoreno: 12', 'tshah: 7']
```

> Test your regex carefully — it can return unintended matches. For example, searching for `"ts"` in `"tsnow, tshah"` would return two matches, not just `"tshah"`.

---

## Working with Files

Security logs are commonly stored as `.txt` or `.csv` files. Both contain plain text.

### Opening, reading, and writing

```python
# Read a file — "r" mode
with open("update_log.txt", "r") as file:
    updates = file.read()   # .read() converts file to a string
print(updates)

# Read using an absolute file path
with open("/home/analyst/logs/access_log.txt", "r") as file:
    logs = file.read()

# Write to a file — "w" overwrites existing content
with open("update_log.txt", "w") as file:
    file.write("new log content")

# Create a new file with "w"
with open("new_log.txt", "w") as file:
    file.write("initial content")

# Append to a file — "a" adds to end without overwriting
line = "jrafael,192.168.243.140,4:56:27,True"
with open("access_log.txt", "a") as file:
    file.write(line)
```

**File open modes:**

| Mode | Description |
|------|-------------|
| `"r"` | Read — opens existing file |
| `"w"` | Write — overwrites existing or creates new |
| `"a"` | Append — adds to the end of an existing file |

### Parsing: .split() and .join()

```python
# .split(separator) — converts a string into a list
approved_users = "elarson,bmoreno,tshah,sgilmore"
users_list = approved_users.split(",")
print(users_list)
# ['elarson', 'bmoreno', 'tshah', 'sgilmore']

# No argument = split on whitespace
removed = "elarson bmoreno tshah"
print(removed.split())
# ['elarson', 'bmoreno', 'tshah']

# Read a file and parse into a list for iteration
with open("update_log.txt", "r") as file:
    updates = file.read()
updates = updates.split()   # file is closed before this line runs

# .join(list) — converts a list back into a string
rejoined = ",".join(users_list)
print(rejoined)   # elarson,bmoreno,tshah,sgilmore

# Join with newlines
print("\n".join(users_list))

# Write a modified list back to a file
with open("update_log.txt", "w") as file:
    file.write(" ".join(updates))
```

---

## Python in CI/CD Security Automation (DevSecOps)

**DevSecOps** = Development + Security + Operations. Security is built into every pipeline stage, not added afterward.

**Why automate CI/CD security with Python:**
- Fast and consistent — same checks on every build
- Catches issues early when they're cheaper to fix
- Reduces manual effort for security teams
- Enforces security policies automatically

**Security tasks Python can automate in CI/CD:**

| Task | Description |
|------|-------------|
| SAST | Static code analysis before build; fail pipeline on critical findings |
| DAST | Dynamic testing on running staging environments |
| SCA | Check dependencies for known CVEs |
| Secrets scanning | Detect hardcoded credentials in commits |
| Compliance checks | Verify code follows secure coding standards |
| Vulnerability scanning | Scan containers and infrastructure configurations |
| Policy enforcement | Block releases that violate defined security rules |

```python
# Example: simple secrets scanner — flags lines with hardcoded passwords
import re

def scan_for_secrets(filepath):
    with open(filepath, "r") as file:
        content = file.read()
    matches = re.findall(r"password\s*=\s*\S+", content, re.IGNORECASE)
    if matches:
        print(f"WARNING: Possible hardcoded secret found: {matches}")
    else:
        print("No secrets detected.")

scan_for_secrets("config.py")
```

**How Python integrates with CI/CD tools** (Jenkins, GitLab CI, CircleCI):
- Pipeline steps that execute Python scripts directly
- Python API calls to trigger scans and retrieve results
- Integration with secrets management tools (e.g., HashiCorp Vault)

---

## Code Style and Readability (PEP 8)

### Comments

```python
# Single-line comment — keep under 79 characters per line
# This loop prints each asset in the computer_assets list
for asset in computer_assets:
    print(asset)

# Multi-line comment using hashtags
# remaining_login_attempts() takes two integer parameters:
# maximum_attempts and total_attempts
# and returns the number of remaining login attempts

# Multi-line docstring
"""
remaining_login_attempts() takes two integer parameters,
the maximum login attempts allowed and the total attempts made,
and returns an integer representing remaining login attempts.
"""
```

### Indentation and syntax rules

```python
# Use 4 spaces per indentation level
count = 0
login_status = True

while login_status == True:
    print("Try again.")           # 4 spaces
    count += 1
    if count == 4:
        login_status = False      # 8 spaces (nested)

# Strings must be in quotes
username = "bmoreno"

# Integers, floats, Booleans — no quotes
login_attempts = 5
success_rate = 0.8
is_active = True

# Lists — square brackets, comma-separated
users = ["bmoreno", "tshah"]

# All headers (if, elif, else, for, while, def) end with a colon (:)
def check_attempts(attempts):
    if attempts > 5:
        print("Too many attempts")
```

---

## Debugging

### Three types of errors

| Type | Description | Example |
|------|-------------|---------|
| **Syntax error** | Invalid Python syntax | Missing colon, unclosed quote |
| **Logic error** | Code runs but produces wrong result | Using `>=` instead of `>` |
| **Exception** | Syntactically valid but fails at runtime | Undefined variable, wrong index |

### Common exception messages

| Message | Cause |
|---------|-------|
| `SyntaxError` | Invalid syntax (missing quote, colon, bracket) |
| `IndentationError` | Incorrect indentation (subclass of SyntaxError) |
| `NameError` | Variable or function not defined |
| `IndexError` | Index doesn't exist in the list |
| `TypeError` | Wrong data type in an operation |
| `FileNotFoundError` | File path doesn't exist |

### Code examples

```python
# SyntaxError — missing closing quote
message = "Welcome to the security system   # fix: add closing "

# Logic error — wrong operator
login_attempts = 5
if login_attempts >= 5:   # bug: should be < 5
    print("User has not reached maximum number of login attempts.")
# This incorrectly prints even when attempts equals the maximum

# NameError — variable never assigned
username = "elarson"
if unusual_logins > 3:    # unusual_logins is undefined
    print("Alert: Unusual login activity")
```

### Debugging with print statements

```python
approved_users = ["elarson", "bmoreno"]
new_users = ["tshah", "bmoreno"]

for user in new_users:
    print("Checking user:", user)              # trace each iteration
    if user in approved_users:
        print(user, "already in list")
    approved_users.append(user)               # bug: runs even when user exists
    print("List after append:", approved_users)

# Fix: use else so .append() only runs when user is NOT already in the list
for user in new_users:
    if user in approved_users:
        print(user, "already in list")
    else:
        approved_users.append(user)
```

**Other debugging strategies:**
- **IDE debugger** — Set breakpoints to pause and step through code; inspect variable values at each step
- **AI tools** (e.g., Gemini Code Assist) — Integrated into IDEs; can explain errors, suggest fixes, and answer questions. Always review AI-generated code before running it.

---

## Essential Python Components for Automation — Summary

| Component | Role in Automation |
|-----------|--------------------|
| **Variables** | Store and reuse data without rewriting values |
| **Conditionals** | Apply logic — act only when certain conditions are met |
| **for loops** | Repeat an action for each item in a sequence |
| **while loops** | Repeat an action until a condition becomes `False` |
| **Functions** | Define reusable code blocks; call them anywhere |
| **Strings** | Work with log data, usernames, IPs, and file contents |
| **Lists** | Store and manipulate collections of security-related data |
| **Files** | Import, read, parse, and write security logs and reports |
| **Regex** | Search for complex patterns in large strings or logs |
| **Modules** | Access built-in and external tools (`re`, `csv`, `statistics`) |

### Full example: count logins for a flagged user

```python
def count_flagged_logins(flagged_user, login_list):
    """
    Counts how many times a flagged user appears in the login list.
    Parameters:
        flagged_user (str): the username to search for
        login_list (list): all login usernames recorded for the day
    Returns:
        int: number of logins made by the flagged user
    """
    count = 0
    for user in login_list:
        if user == flagged_user:
            count += 1
    return count

# Example usage
daily_logins = ["jdoe", "bmoreno", "jdoe", "tshah", "jdoe", "elarson"]
result = count_flagged_logins("jdoe", daily_logins)
print("Flagged user login count:", result)   # 3
```
