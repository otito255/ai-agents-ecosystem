# Log Anomaly Detection Agent

Uses AI to detect unusual patterns in log files automatically.

## Quick Start (5 Minutes)

### Step 1: Create Project Folder

```bash
mkdir log-anomaly-agent
cd log-anomaly-agent
touch logs.txt script.py
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

### Step 4: Add Your Logs (logs.txt)

```
2024-06-01 10:01 INFO Service started
2024-06-01 10:02 INFO Request processed
2024-06-01 10:03 ERROR Database timeout
2024-06-01 10:03 ERROR Database timeout
2024-06-01 10:03 ERROR Database timeout
2024-06-01 10:04 INFO Request processed
```

### Step 5: Copy Code (agent.py)

Copy the entire code from the original script into `agent.py`.

### Step 6: Run

```bash
python script.py
```

You get two files:
- `log_anomalies.json` — structured analysis
- `log_anomalies.txt` — readable report

## What It Does

- Reads log files
- Detects error patterns and spikes
- Analyzes frequency and severity
- Suggests what to investigate
- Saves results as JSON and text

## Input Format

In `logs.txt`, add your logs (any standard format):

**Format 1 — Timestamp + Level + Message:**
```
2024-06-01 10:01 INFO Service started
2024-06-01 10:02 ERROR Connection failed
2024-06-01 10:03 ERROR Connection failed
```

**Format 2 — Apache/Nginx style:**
```
192.168.1.1 - - [01/Jun/2024:10:01:00] "GET / HTTP/1.1" 200
192.168.1.1 - - [01/Jun/2024:10:02:00] "GET / HTTP/1.1" 500
192.168.1.1 - - [01/Jun/2024:10:02:01] "GET / HTTP/1.1" 500
```

**Format 3 — JSON logs:**
```
{"timestamp":"2024-06-01T10:01:00Z","level":"INFO","message":"Service started"}
{"timestamp":"2024-06-01T10:02:00Z","level":"ERROR","message":"Database timeout"}
```

The agent understands any format!

## Output Example

### log_anomalies.json
```json
{
  "summary": "Multiple database timeout errors detected within a short timeframe, indicating potential service degradation.",
  "anomalies": [
    "Repeated error detected: 'Database timeout' (3 times)"
  ],
  "severity": "High",
  "time_context": "Errors clustered between 10:03-10:04, suggesting temporary service failure",
  "investigation_focus": [
    "Check database connection pool status",
    "Review database performance metrics at 10:03",
    "Verify network connectivity to database server"
  ]
}
```

### log_anomalies.txt
```
Log Anomaly Report (2024-06-01)
=======================================================

Summary:
Multiple database timeout errors detected within a short timeframe...

Anomalies:
- Repeated error detected: 'Database timeout' (3 times)

Severity:
High

Time Context:
Errors clustered between 10:03-10:04, suggesting temporary service failure

Investigation Focus:
- Check database connection pool status
- Review database performance metrics at 10:03
- Verify network connectivity to database server
```

## Analysis Structure

The agent evaluates:

| Part | What It Includes |
|------|-----------------|
| **Summary** | Overview of what went wrong |
| **Anomalies** | Specific unusual patterns found |
| **Severity** | How urgent (Low, Medium, High, Critical) |
| **Time Context** | When errors occurred |
| **Investigation Focus** | What to check first |

## Input Examples

**Example 1 — Web Server Errors:**
```
2024-06-01 14:15 INFO GET /api/users 200
2024-06-01 14:16 ERROR Connection timeout
2024-06-01 14:16 ERROR Connection timeout
2024-06-01 14:16 ERROR Connection timeout
2024-06-01 14:17 INFO GET /api/users 200
```

**Example 2 — Database Logs:**
```
2024-06-01 12:00 [INFO] Query executed: 45ms
2024-06-01 12:01 [ERROR] Deadlock detected
2024-06-01 12:01 [ERROR] Deadlock detected
2024-06-01 12:01 [ERROR] Deadlock detected
2024-06-01 12:02 [WARN] Lock timeout
```

**Example 3 — Application Logs:**
```
2024-06-01 09:30 DEBUG Service initialized
2024-06-01 09:31 INFO Request from user_123
2024-06-01 09:32 ERROR OutOfMemory
2024-06-01 09:32 ERROR OutOfMemory
2024-06-01 09:33 INFO Restarted service
```

## Customize

**Change the AI model:**
```python
model="gpt-4.1-mini"  # Use gpt-4, gpt-3.5-turbo, etc.
```

**Change detection sensitivity:**
```python
temperature=0.2  # Lower = stricter, Higher = more lenient
```

**Adjust anomaly rules:**
```python
# Currently detects errors appearing >2 times
if count > 2:  # Change to > 1 or > 5 for different sensitivity
    anomalies.append(...)
```

## Common Issues

| Problem | Fix |
|---------|-----|
| `AuthenticationError` | Check OPENAI_API_KEY is set |
| `FileNotFoundError` | Create logs.txt in same folder |
| No anomalies found | Add errors to logs.txt to test |

## Tips

- Use actual log files from your application
- Mix normal and error logs for better detection
- Check if anomalies make sense before alerting
- Review severity level before taking action
- Use for proactive monitoring, not just debugging

## Multiple Log Files

Analyze multiple log files:

```python
import os

log_files = ["app.log", "db.log", "web.log"]

for log_file in log_files:
    with open(log_file, "r") as f:
        logs = f.readlines()
    
    analysis = interpret_anomalies(logs)
    save_outputs(analysis)
    print(f"✓ {log_file} analyzed")
```

## Cost

~$0.001 per analysis = ~$1 for 1000 log files
