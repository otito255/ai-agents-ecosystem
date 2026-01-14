import json
from openai import OpenAI
from datetime import date
 
client = OpenAI()  # requires OPENAI_API_KEY
 
SYSTEM_PROMPT = """
You are an Expense Categorization Agent.
 
Rules:
- Assign the most appropriate expense category
- Use vendor and description context
- Avoid guessing when uncertain
- Provide confidence and flags
 
Return ONLY valid JSON with this schema:
 
{
  "vendor": "",
  "description": "",
  "amount": "",
  "date": "",
  "category": "",
  "confidence": "",
  "flags": []
}
"""
 
def read_input(path="input.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
 
def categorize_expense(prompt_text):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt_text}
        ],
        temperature=0.25
    )
    return json.loads(response.choices[0].message.content)
 
def save_outputs(data):
    with open("expense_categorization.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
 
    with open("expense_categorization.txt", "w", encoding="utf-8") as f:
        f.write(f"Expense Categorization ({date.today()})\n")
        f.write("=" * 50 + "\n\n")
 
        f.write(f"Vendor: {data['vendor']}\n")
        f.write(f"Description: {data['description']}\n")
        f.write(f"Amount: {data['amount']}\n")
        f.write(f"Date: {data['date']}\n")
        f.write(f"Category: {data['category']}\n")
        f.write(f"Confidence: {data['confidence']}\n")
 
        if data["flags"]:
            f.write("\nFlags:\n")
            for flag in data["flags"]:
                f.write(f"- {flag}\n")
 
def main():
    prompt_text = read_input()
    categorized = categorize_expense(prompt_text)
    save_outputs(categorized)
    print("Expense categorized successfully.")
 
if __name__ == "__main__":
    main()