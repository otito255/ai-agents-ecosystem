import json
from openai import OpenAI
from datetime import date
 
client = OpenAI()  # requires OPENAI_API_KEY
 
SYSTEM_PROMPT = """
You are a Test Case Generation Agent.
 
Rules:
- Generate meaningful test cases
- Cover normal and edge cases
- Align with Python unittest style
- Do NOT invent behavior
 
Return ONLY valid JSON with this schema:
 
{
  "test_cases": [
    {
      "description": "",
      "inputs": {},
      "expected": ""
    }
  ]
}
"""
 
def read_code(path="source_code.py"):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
 
def generate_tests(code_text):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": code_text}
        ],
        temperature=0.2
    )
    return json.loads(response.choices[0].message.content)
 
def save_outputs(data):
    # Save JSON report
    report = {
        "date": str(date.today()),
        "tests": data["test_cases"]
    }
 
    with open("test_cases_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
 
    # Save Python test file
    with open("generated_tests.py", "w", encoding="utf-8") as f:
        f.write("import unittest\n\n")
        f.write("from source_code import divide\n\n")
        f.write("class TestDivideFunction(unittest.TestCase):\n")
        for i, t in enumerate(data["test_cases"], 1):
            f.write(f"    def test_case_{i}(self):\n")
            if "Exception" in t["expected"]:
                f.write(
                    f"        with self.assertRaises(ValueError):\n"
                    f"            divide(**{t['inputs']})\n\n"
                )
            else:
                f.write(
                    f"        self.assertEqual(divide(**{t['inputs']}), {t['expected']})\n\n"
                )
 
def main():
    code_text = read_code()
    tests = generate_tests(code_text)
    save_outputs(tests)
    print("Test cases generated successfully.")
 
if __name__ == "__main__":
    main()