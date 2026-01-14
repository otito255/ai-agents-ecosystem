# Customer Support Agent

Uses AI to automatically write professional customer support responses.

## Quick Start (5 Minutes)

### Step 1: Create Project Folder

```bash
mkdir customer-support-agent
cd customer-support-agent
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

### Step 4: Add Support Ticket (input.txt)

```
Customer Message:
I was charged twice for my subscription this month and I'm really frustrated.

Issue Category: Billing
Urgency: High
Brand Tone: Professional and empathetic
```

### Step 5: Copy Code (agent.py)

Copy the entire code from the original script into `agent.py`.

### Step 6: Run

```bash
python agent.py
```

You get two files:
- `support_response.json` — structured response
- `support_response.txt` — readable draft

## What It Does

- Reads customer support tickets
- Generates professional, empathetic responses
- Structures response with greeting, acknowledgment, solution, next steps
- Saves outputs as JSON and text

## Input Format

In `input.txt`, include:
- **Customer Message** — What they're complaining about
- **Issue Category** — Billing, Technical, Shipping, etc.
- **Urgency** — Low, Medium, High
- **Brand Tone** — How to respond (Professional, Friendly, Formal, etc.)

## Output Example

### support_response.json
```json
{
  "greeting": "Hello and thank you for contacting us,",
  "acknowledgment": "I sincerely apologize for the frustration caused by the duplicate charge on your account.",
  "response": "We take billing errors very seriously. I've reviewed your account and confirmed the double charge occurred.",
  "next_steps": "Our billing team will process a refund within 3-5 business days. You'll receive a confirmation email.",
  "closing": "Thank you for your patience. Please let us know if you have any questions."
}
```

### support_response.txt
```
Customer Support Draft (2024-01-14)
==================================================

Hello and thank you for contacting us,

I sincerely apologize for the frustration caused by the duplicate charge on your account.

We take billing errors very seriously. I've reviewed your account and confirmed the double charge occurred.

Next Steps:
Our billing team will process a refund within 3-5 business days. You'll receive a confirmation email.

Thank you for your patience. Please let us know if you have any questions.
```

## Response Structure

The AI creates 5-part responses:

| Part | What It Is |
|------|-----------|
| **Greeting** | Polite opening |
| **Acknowledgment** | Show you understand the problem |
| **Response** | How you'll solve it |
| **Next Steps** | What happens next |
| **Closing** | Professional goodbye |

## Input Examples

**Example 1 — Billing Issue:**
```
Customer Message:
I was charged twice for my subscription this month and I'm really frustrated.

Issue Category: Billing
Urgency: High
Brand Tone: Professional and empathetic
```

**Example 2 — Technical Problem:**
```
Customer Message:
The app keeps crashing when I try to upload photos.

Issue Category: Technical
Urgency: High
Brand Tone: Friendly and helpful
```

**Example 3 — Shipping Issue:**
```
Customer Message:
My order was supposed to arrive last week but it's still not here.

Issue Category: Shipping
Urgency: Medium
Brand Tone: Professional
```

## Customize

**Change the AI model:**
```python
model="gpt-4.1-mini"  # Use gpt-4, gpt-3.5-turbo, etc.
```

**Change response temperature (creativity):**
```python
temperature=0.35  # Lower = more consistent, Higher = more creative
```

**Add company-specific rules:**
```python
SYSTEM_PROMPT = """
You are a Customer Support Response Agent.

Company Policy:
- Max refund: $500
- Refund time: 5-7 business days
- Always mention order number

Rules:
- Be empathetic and professional
- Acknowledge the customer issue clearly
- Align with company policy
- Do NOT promise actions beyond scope
"""
```

## Common Issues

| Problem | Fix |
|---------|-----|
| `AuthenticationError` | Check OPENAI_API_KEY is set |
| `FileNotFoundError` | Create input.txt in same folder |
| No output | Make sure input.txt has content |

## Tips

- Review the generated response before sending
- Adjust tone based on customer urgency
- Include specific details in customer message
- Test with different tones and categories
- Use for drafts — always have a human review

## Multiple Tickets

Process several tickets:

```python
tickets = [
    "Customer complaining about late delivery",
    "User confused about pricing",
    "Technical support request"
]

for i, ticket in enumerate(tickets):
    with open("input.txt", "w") as f:
        f.write(ticket)
    
    prompt = read_input()
    reply = generate_response(prompt)
    save_outputs(reply)
    print(f"✓ Response {i+1} generated")
```

## Cost

~$0.001 per response = ~$1 for 1000 responses