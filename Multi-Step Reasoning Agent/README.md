# Multi-Step Reasoning Agent

Uses AI to break down complex problems and solve them step-by-step.

## Quick Start (5 Minutes)

### Step 1: Create Project Folder

```bash
mkdir multi-step-reasoning-agent
cd multi-step-reasoning-agent
touch problem.txt agent.py
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

### Step 4: Add Your Problem (problem.txt)

```
A company has a budget of $120,000.
Marketing costs $2,500 per campaign.
Engineering costs $8,000 per feature.
If the company runs 20 marketing campaigns, how many features can it build?
```

### Step 5: Copy Code (agent.py)

Copy the entire code from the original script into `agent.py`.

### Step 6: Run

```bash
python agent.py
```

You get two files:
- `reasoning_result.json` — structured reasoning
- `reasoning_result.txt` — readable report

## What It Does

- Reads a complex problem
- Breaks it into logical steps
- Solves each step in order
- Lists all assumptions made
- Outputs final answer with reasoning

## Input Format

In `problem.txt`, write any problem or question:

```
Your problem statement here.
Include all relevant information.
Ask a specific question at the end.
```

Works for:
- Math problems
- Logic puzzles
- Decision-making scenarios
- Planning questions
- Analysis tasks
- "What if" scenarios

## Output Example

### reasoning_result.json
```json
{
  "steps": [
    "Total budget: $120,000",
    "Marketing cost per campaign: $2,500",
    "Total marketing cost: 20 campaigns × $2,500 = $50,000",
    "Remaining budget: $120,000 - $50,000 = $70,000",
    "Engineering cost per feature: $8,000",
    "Number of features: $70,000 ÷ $8,000 = 8.75"
  ],
  "final_answer": "The company can build 8 full features with $6,000 remaining.",
  "assumptions": [
    "No other costs are considered",
    "Partial features are not counted"
  ]
}
```

### reasoning_result.txt
```
Multi-Step Reasoning Result (2024-06-01)
=======================================================

Reasoning Steps:
- Total budget: $120,000
- Marketing cost per campaign: $2,500
- Total marketing cost: 20 campaigns × $2,500 = $50,000
- Remaining budget: $120,000 - $50,000 = $70,000
- Engineering cost per feature: $8,000
- Number of features: $70,000 ÷ $8,000 = 8.75

Final Answer:
The company can build 8 full features with $6,000 remaining.

Assumptions:
- No other costs are considered
- Partial features are not counted
```

## Reasoning Structure

The agent provides:

| Part | What It Includes |
|------|-----------------|
| **Steps** | Logical sequence of reasoning |
| **Final Answer** | Clear answer to your question |
| **Assumptions** | What was assumed to be true |

## Input Examples

**Example 1 — Math Problem:**
```
A store sells apples for $1.50 each.
Sarah has $20.
She also buys oranges for $2 each.
If she buys 5 oranges, how many apples can she buy?
```

**Example 2 — Logic Puzzle:**
```
Alice, Bob, and Charlie have 12 apples total.
Alice has 2 more than Bob.
Charlie has 1 less than Bob.
How many apples does each person have?
```

**Example 3 — Decision Scenario:**
```
We have 3 vendors:
- Vendor A: $100/month, 95% uptime
- Vendor B: $150/month, 99.9% uptime
- Vendor C: $80/month, 90% uptime

We need at least 99% uptime.
Which vendor gives the best value?
```

**Example 4 — Planning Question:**
```
A project needs:
- 2 weeks of design
- 4 weeks of development
- 1 week of testing
- 2 weeks of deployment

Each phase can't start until the previous is done.
If we start next Monday, when do we finish?
Assume 5-day work weeks.
```

## Customize

**Change the AI model:**
```python
model="gpt-4.1-mini"  # Use gpt-4, gpt-3.5-turbo, etc.
```

**Change reasoning precision:**
```python
temperature=0.2  # Lower = more logical, Higher = more creative
```

**Add reasoning constraints:**
```python
SYSTEM_PROMPT = """
You are a Multi-Step Reasoning Agent.

Rules:
- Break problems into steps
- Show all calculations
- Validate each step
- Be concise
- List all assumptions

Return ONLY valid JSON...
"""
```

## Common Issues

| Problem | Fix |
|---------|-----|
| `AuthenticationError` | Check OPENAI_API_KEY is set |
| `FileNotFoundError` | Create problem.txt in same folder |
| Wrong answer | Rephrase problem more clearly |
| No steps shown | Add more details to your problem |

## Tips

- Be specific in your problem statement
- Include all numbers and constraints
- Ask a clear question at the end
- Review assumptions before trusting answer
- Use for complex decisions, not simple math
- Verify final answer makes logical sense

## Multiple Problems

Solve several problems:

```python
problems = [
    "Problem 1: ...",
    "Problem 2: ...",
    "Problem 3: ..."
]

for i, problem_text in enumerate(problems):
    with open("problem.txt", "w") as f:
        f.write(problem_text)
    
    problem = read_problem()
    result = solve_problem(problem)
    save_outputs(result)
    print(f"✓ Problem {i+1} solved")
```

## Expected Behavior

**Input:**
```
Budget: $1000
Item A costs $200
Item B costs $150
If I buy 2 of Item A, how many B can I buy?
```

**Output:**
```
Steps:
- Starting budget: $1000
- Buy 2 × Item A: 2 × $200 = $400
- Remaining: $1000 - $400 = $600
- Item B cost: $150 each
- Number of B: $600 ÷ $150 = 4

Final Answer:
You can buy 4 of Item B.

Assumptions:
- No taxes or extra fees
- All money is used optimally
```

## Use Cases

- **Project planning** — Timeline and resource calculations
- **Budget allocation** — Cost analysis and feasibility
- **Logic puzzles** — Complex reasoning problems
- **Decision making** — Comparing multiple options
- **Scenario analysis** — "What if" questions
- **Problem solving** — Step-by-step solution breakdown

## Cost

~$0.001 per problem = ~$1 for 1000 problems