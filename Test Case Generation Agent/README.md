# Test Case Generation Agent

Uses AI to automatically generate test cases from your source code.

## Quick Start (5 Minutes)

### Step 1: Create Project Folder

```bash
mkdir test-case-generation-agent
cd test-case-generation-agent
touch source_code.py agent.py
```

### Step 2: Install OpenAI

```bash
pip install openai
```

### Step 3: Set API Key

```bash
export OPENAI_API_KEY="your-api-key"
```
(Get key from [platform.openai.com](https://platform.openai.com))

### Step 4: Add Your Code (source_code.py)

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b
```

### Step 5: Copy Code (agent.py)

Copy the entire code from the original script into `agent.py`.

### Step 6: Run

```bash
python agent.py
```

You get two files:
- `generated_tests.py` — ready-to-run test file
- `test_cases_report.json` — test case details

### Step 7: Run Your Tests

```bash
python -m unittest generated_tests.py -v
```

## What It Does

- Reads your Python source code
- Analyzes functions and logic
- Generates test cases (normal + edge cases)
- Creates a Python unittest file
- Exports test cases as JSON

## Input Format

In `source_code.py`, add any Python function:

```python
def your_function(param1, param2):
    # Your logic here
    return result
```

Works for:
- Simple functions
- Functions with errors/exceptions
- Functions with multiple parameters
- Functions with different return types

## Output Example

### generated_tests.py
```python
import unittest

from source_code import divide

class TestDivideFunction(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(divide(a=10, b=2), 5.0)

    def test_case_2(self):
        self.assertEqual(divide(a=0, b=5), 0.0)

    def test_case_3(self):
        with self.assertRaises(ValueError):
            divide(a=10, b=0)

    def test_case_4(self):
        self.assertEqual(divide(a=-10, b=2), -5.0)
```

### test_cases_report.json
```json
{
  "date": "2024-06-01",
  "tests": [
    {
      "description": "Normal case: divide 10 by 2",
      "inputs": {"a": 10, "b": 2},
      "expected": "5.0"
    },
    {
      "description": "Zero dividend",
      "inputs": {"a": 0, "b": 5},
      "expected": "0.0"
    },
    {
      "description": "Division by zero raises error",
      "inputs": {"a": 10, "b": 0},
      "expected": "ValueError"
    },
    {
      "description": "Negative numbers",
      "inputs": {"a": -10, "b": 2},
      "expected": "-5.0"
    }
  ]
}
```

## Test Types Generated

The agent covers:

| Type | What It Tests | Example |
|------|---------------|---------|
| **Normal case** | Expected inputs and output | divide(10, 2) → 5.0 |
| **Edge case** | Boundary values | divide(0, 5) → 0.0 |
| **Error case** | Exception handling | divide(10, 0) → ValueError |
| **Special case** | Negative, decimals, etc. | divide(-10, 2) → -5.0 |

## Input Examples

**Example 1 — String Processing:**
```python
def reverse_string(text):
    if not text:
        return ""
    return text[::-1]
```

**Example 2 — List Filtering:**
```python
def filter_positive(numbers):
    if not numbers:
        return []
    return [n for n in numbers if n > 0]
```

**Example 3 — Age Validation:**
```python
def is_adult(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age >= 18
```

**Example 4 — Calculate Discount:**
```python
def apply_discount(price, discount_percent):
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Invalid discount")
    return price * (1 - discount_percent / 100)
```

## Customize

**Change the AI model:**
```python
model="gpt-4.1-mini"  # Use gpt-4, gpt-3.5-turbo, etc.
```

**Change test generation precision:**
```python
temperature=0.2  # Lower = consistent, Higher = more varied
```

**Add testing constraints:**
```python
SYSTEM_PROMPT = """
You are a Test Case Generation Agent.

Rules:
- Generate 5-8 test cases per function
- Cover all branches and conditions
- Include error cases
- Focus on critical paths
- Avoid redundant tests

Return ONLY valid JSON...
"""
```

## Common Issues

| Problem | Fix |
|---------|-----|
| `AuthenticationError` | Check OPENAI_API_KEY is set |
| `FileNotFoundError` | Create source_code.py in same folder |
| Tests fail | Review generated tests, may need adjustment |
| Syntax errors | Check generated_tests.py for issues |

## Tips

- Start with simple functions
- Review generated tests before running
- Adjust test values if needed
- Use for rapid test coverage
- Don't rely 100% on AI-generated tests
- Add custom tests for complex logic

## Run Generated Tests

After generation, run your tests:

```bash
# Run all tests
python -m unittest generated_tests.py -v

# Run specific test
python -m unittest generated_tests.py.TestDivideFunction.test_case_1

# Run with coverage
pip install coverage
coverage run -m unittest generated_tests.py
coverage report
```

## Test Multiple Functions

Generate tests for different functions:

```python
functions = [
    "def add(a, b): return a + b",
    "def multiply(a, b): return a * b",
    "def subtract(a, b): return a - b"
]

for i, func_code in enumerate(functions):
    with open("source_code.py", "w") as f:
        f.write(func_code)
    
    code_text = read_code()
    tests = generate_tests(code_text)
    save_outputs(tests)
    print(f"✓ Generated tests for function {i+1}")
```

## Expected Behavior

**Input (source_code.py):**
```python
def add(a, b):
    return a + b
```

**Output (generated_tests.py):**
```python
class TestAddFunction(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(add(a=5, b=3), 8)

    def test_case_2(self):
        self.assertEqual(add(a=0, b=0), 0)

    def test_case_3(self):
        self.assertEqual(add(a=-5, b=5), 0)
```

## Use Cases

- **Test coverage** — Quickly generate baseline tests
- **Code review** — Ensure all cases are tested
- **Regression testing** — Catch breaking changes
- **Documentation** — Tests show expected behavior
- **Onboarding** — Help new developers understand code
- **CI/CD** — Automated test generation in pipelines

## Limitations

AI-generated tests:
- May not cover all edge cases
- Can't understand business logic
- Might need manual refinement
- Should be reviewed before deployment
- Work best for simple, pure functions

## Cost

~$0.001 per function = ~$1 for 1000 functions