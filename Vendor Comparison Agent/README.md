# Vendor Comparison Agent

Uses AI to objectively compare vendors across your criteria.

## Quick Start (5 Minutes)

### Step 1: Create Project Folder

```bash
mkdir vendor-comparison-agent
cd vendor-comparison-agent
touch input.txt agent.py
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

### Step 4: Add Vendor Data (input.txt)

```
Vendors:
- Vendor A
- Vendor B
- Vendor C

Criteria:
- Cost
- Feature completeness
- Support quality
- Scalability
- Compliance readiness

Business Priority:
Operational reliability and long-term scalability
```

### Step 5: Copy Code (agent.py)

Copy the entire code from the original script into `agent.py`.

### Step 6: Run

```bash
python agent.py
```

You get two files:
- `vendor_comparison.json` — structured comparison
- `vendor_comparison.txt` — readable report

## What It Does

- Reads vendor data and comparison criteria
- Compares vendors objectively
- Lists strengths and weaknesses for each
- Highlights key trade-offs
- Saves results as JSON and text

## Input Format

In `input.txt`, include:
- **Vendors** — List of vendors to compare
- **Criteria** — What you're comparing (cost, features, support, etc.)
- **Business Priority** — What matters most to you

## Output Example

### vendor_comparison.json
```json
{
  "summary": "Vendor A excels in cost efficiency, while Vendor B offers superior feature completeness. Vendor C balances both but at premium pricing.",
  "vendors": [
    {
      "name": "Vendor A",
      "strengths": [
        "Lowest cost",
        "Quick implementation"
      ],
      "weaknesses": [
        "Limited features",
        "Basic support"
      ],
      "notes": "Best for cost-conscious teams with basic needs."
    }
  ],
  "key_tradeoffs": [
    "Cost vs. Feature Completeness: Lower cost means fewer advanced features",
    "Support vs. Price: Premium support costs extra"
  ]
}
```

### vendor_comparison.txt
```
Vendor Comparison (2024-01-14)
=======================================================

Summary:
Vendor A excels in cost efficiency, while Vendor B offers superior feature completeness...

Vendor: Vendor A
Strengths:
- Lowest cost
- Quick implementation
Weaknesses:
- Limited features
- Basic support
Notes:
Best for cost-conscious teams with basic needs.

Key Trade-offs:
- Cost vs. Feature Completeness: Lower cost means fewer advanced features
```

## Comparison Structure

The AI evaluates:

| Part | What It Includes |
|------|-----------------|
| **Summary** | High-level comparison overview |
| **Vendors** | Strengths, weaknesses, and notes for each |
| **Trade-offs** | Key decisions and compromises |

## Input Examples

**Example 1 — Cloud Hosting:**
```
Vendors:
- AWS
- Google Cloud
- Azure

Criteria:
- Pricing
- Ease of use
- Available services
- Customer support
- Global reach

Business Priority:
Cost efficiency and ease of use
```

**Example 2 — Payment Processors:**
```
Vendors:
- Stripe
- Square
- PayPal

Criteria:
- Transaction fees
- Integration difficulty
- Payment methods supported
- Settlement time
- Dispute handling

Business Priority:
Fast settlement and low fees
```

**Example 3 — Project Management Tools:**
```
Vendors:
- Jira
- Asana
- Monday.com

Criteria:
- Learning curve
- Customization
- Integrations
- Pricing
- Team collaboration

Business Priority:
Team adoption and ease of use
```

## Customize

**Change the AI model:**
```python
model="gpt-4.1-mini"  # Use gpt-4, gpt-3.5-turbo, etc.
```

**Change response temperature (consistency):**
```python
temperature=0.3  # Lower = more consistent, Higher = more creative
```

**Adjust comparison rules:**
```python
SYSTEM_PROMPT = """
You are a Vendor Comparison Agent.

Rules:
- Compare vendors objectively
- Use consistent criteria
- Highlight strengths, weaknesses, and trade-offs
- Focus on business impact, not opinions
- Avoid making final recommendations
"""
```

## Common Issues

| Problem | Fix |
|---------|-----|
| `AuthenticationError` | Check OPENAI_API_KEY is set |
| `FileNotFoundError` | Create input.txt in same folder |
| No output | Make sure input.txt has vendor data |

## Tips

- List specific vendor names (not "Vendor A")
- Include 2-5 criteria for best results
- State your business priority clearly
- Review both JSON and text outputs
- Use for informed decision-making, not final approval

## Multiple Comparisons

Compare different vendor sets:

```python
comparisons = [
    "Compare AWS vs Azure vs GCP for hosting",
    "Compare Stripe vs Square for payments",
    "Compare Slack vs Teams for messaging"
]

for i, prompt in enumerate(comparisons):
    with open("input.txt", "w") as f:
        f.write(prompt)
    
    data = read_input()
    result = compare_vendors(data)
    save_outputs(result)
    print(f"✓ Comparison {i+1} complete")
```

## Cost

~$0.001 per comparison = ~$1 for 1000 comparisons