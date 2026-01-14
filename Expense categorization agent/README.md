# Expense Categorization Agent

Uses AI to automatically categorize your business expenses.

## What It Does

- Reads expense descriptions
- Categorizes them (Travel, Meals, Office Supplies, etc.)
- Gives confidence level (High/Medium/Low)
- Flags unusual expenses
- Saves results as JSON and text

## Setup

1. Install OpenAI:
   ```bash
   pip install openai
   ```

2. Get API key from [platform.openai.com](https://platform.openai.com)

3. Set environment variable:
   ```bash
   export OPENAI_API_KEY="your-api-key"
   ```

## Usage

1. Create `input.txt` with expense details:
   ```
   Vendor: Starbucks
   Description: Coffee for meeting
   Amount: $12.50
   Date: 2024-01-14
   ```

2. Run:
   ```bash
   python script.py
   ```

3. Get two files:
   - `expense_categorization.json` — data
   - `expense_categorization.txt` — readable report

## Output Example

```json
{
  "vendor": "Starbucks",
  "description": "Coffee for meeting",
  "amount": "$12.50",
  "date": "2024-01-14",
  "category": "Meals & Entertainment",
  "confidence": "High",
  "flags": []
}
```

## Confidence Levels

- **High** — Clear category match
- **Medium** — Probably right, needs context
- **Low** — Unclear, review manually

## Common Categories

- Travel (flights, hotels, gas)
- Meals & Entertainment (restaurants, coffee)
- Office Supplies (pens, paper, desk)
- Software & Tech (apps, subscriptions)
- Professional Services (consulting, legal)
- Utilities (internet, phone)

## Flags

Alert you to potential issues:
- `"High amount - verify business purpose"`
- `"Unclear category"`
- `"Personal vs business unclear"`

## Customize

**Change AI model:**
```python
model="gpt-4.1-mini"  # Change to gpt-4 or gpt-3.5-turbo
```

**Add custom categories:**
```python
SYSTEM_PROMPT = """
Categories:
- Travel
- Marketing
- R&D
...
"""
```

## Common Issues

| Problem | Fix |
|---------|-----|
| `AuthenticationError` | Check OPENAI_API_KEY is set |
| `FileNotFoundError` | Create input.txt file |
| `JSONDecodeError` | Check input format is clear |

## Tips

- Be specific in descriptions
- Include vendor name when possible
- Add context (e.g., "client meeting", "office setup")
- Review flags before approving
- Check confidence level

## Cost

~$0.001 per expense = ~$1 for 1000 expenses