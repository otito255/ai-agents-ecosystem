import json
from openai import OpenAI
from datetime import date
 
client = OpenAI()  # requires OPENAI_API_KEY
 
SYSTEM_PROMPT = """
You are a Customer Support Response Agent.
 
Rules:
- Be empathetic and professional
- Acknowledge the customer issue clearly
- Align with company policy
- Do NOT promise actions beyond scope
 
Return ONLY valid JSON with this schema:
 
{
  "greeting": "",
  "acknowledgment": "",
  "response": "",
  "next_steps": "",
  "closing": ""
}
"""
 
def read_input(path="input.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
 
def generate_response(prompt_text):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt_text}
        ],
        temperature=0.35
    )
    return json.loads(response.choices[0].message.content)
 
def save_outputs(data):
    with open("support_response.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
 
    with open("support_response.txt", "w", encoding="utf-8") as f:
        f.write(f"Customer Support Draft ({date.today()})\n")
        f.write("=" * 50 + "\n\n")
 
        f.write(f"{data['greeting']}\n\n")
        f.write(f"{data['acknowledgment']}\n\n")
        f.write(f"{data['response']}\n\n")
        f.write(f"Next Steps:\n{data['next_steps']}\n\n")
        f.write(f"{data['closing']}\n")
 
def main():
    prompt_text = read_input()
    support_reply = generate_response(prompt_text)
    save_outputs(support_reply)
    print("Customer support response generated successfully.")
 
if __name__ == "__main__":
    main()