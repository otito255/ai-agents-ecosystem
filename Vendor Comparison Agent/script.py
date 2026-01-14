import json
from openai import OpenAI
from datetime import date
 
client = OpenAI()  # requires OPENAI_API_KEY
 
SYSTEM_PROMPT = """
You are a Vendor Comparison Agent.
 
Rules:
- Compare vendors objectively
- Use consistent criteria
- Highlight strengths, weaknesses, and trade-offs
- Avoid making final recommendations
 
Return ONLY valid JSON with this schema:
 
{
  "summary": "",
  "vendors": [
    {
      "name": "",
      "strengths": [],
      "weaknesses": [],
      "notes": ""
    }
  ],
  "key_tradeoffs": []
}
"""
 
def read_input(path="input.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
 
def compare_vendors(prompt_text):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt_text}
        ],
        temperature=0.3
    )
    return json.loads(response.choices[0].message.content)
 
def save_outputs(data):
    with open("vendor_comparison.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
 
    with open("vendor_comparison.txt", "w", encoding="utf-8") as f:
        f.write(f"Vendor Comparison ({date.today()})\n")
        f.write("=" * 55 + "\n\n")
 
        f.write("Summary:\n")
        f.write(data["summary"] + "\n\n")
 
        for v in data["vendors"]:
            f.write(f"Vendor: {v['name']}\n")
            f.write("Strengths:\n")
            for s in v["strengths"]:
                f.write(f"- {s}\n")
            f.write("Weaknesses:\n")
            for w in v["weaknesses"]:
                f.write(f"- {w}\n")
            f.write(f"Notes:\n{v['notes']}\n\n")
 
        f.write("Key Trade-offs:\n")
        for t in data["key_tradeoffs"]:
            f.write(f"- {t}\n")
 
def main():
    prompt_text = read_input()
    comparison = compare_vendors(prompt_text)
    save_outputs(comparison)
    print("Vendor comparison completed successfully.")
 
if __name__ == "__main__":
    main()