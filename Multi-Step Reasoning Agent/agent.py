import json
from openai import OpenAI
from datetime import date
 
client = OpenAI()  # requires OPENAI_API_KEY
 
SYSTEM_PROMPT = """
You are a Multi-Step Reasoning Agent.
 
Rules:
- Break problems into steps
- Validate each step
- Do NOT expose chain-of-thought verbatim
- Provide structured reasoning summary
 
Return ONLY valid JSON with this schema:
 
{
  "steps": [],
  "final_answer": "",
  "assumptions": []
}
"""
 
def read_problem(path="problem.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
 
def solve_problem(problem):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": problem}
        ],
        temperature=0.2
    )
    return json.loads(response.choices[0].message.content)
 
def save_outputs(data):
    with open("reasoning_result.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
 
    with open("reasoning_result.txt", "w", encoding="utf-8") as f:
        f.write(f"Multi-Step Reasoning Result ({date.today()})\n")
        f.write("=" * 55 + "\n\n")
        f.write("Reasoning Steps:\n")
        for s in data["steps"]:
            f.write(f"- {s}\n")
        f.write(f"\nFinal Answer:\n{data['final_answer']}\n")
        if data["assumptions"]:
            f.write("\nAssumptions:\n")
            for a in data["assumptions"]:
                f.write(f"- {a}\n")
 
def main():
    problem = read_problem()
    result = solve_problem(problem)
    save_outputs(result)
    print("Multi-step reasoning completed successfully.")
 
if __name__ == "__main__":
    main()