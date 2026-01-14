import json
from openai import OpenAI
from collections import Counter
from datetime import date
 
client = OpenAI()  # requires OPENAI_API_KEY
 
SYSTEM_PROMPT = """
You are a Log Anomaly Detection Agent.
 
Rules:
- Identify unusual patterns or spikes
- Consider frequency and severity
- Avoid false alarms
- Suggest investigation focus
 
Return ONLY valid JSON with this schema:
 
{
  "summary": "",
  "anomalies": [],
  "severity": "",
  "time_context": "",
  "investigation_focus": []
}
"""
 
def read_logs(path="logs.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return f.readlines()
 
def detect_anomalies(log_lines):
    error_lines = [l for l in log_lines if "ERROR" in l]
    counts = Counter(error_lines)
 
    anomalies = [
        f"Repeated error detected: '{msg.strip()}' ({count} times)"
        for msg, count in counts.items() if count > 2
    ]
 
    return anomalies
 
def interpret_anomalies(log_lines):
    anomalies = detect_anomalies(log_lines)
 
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": "\n".join(anomalies) if anomalies else "No anomalies detected"}
        ],
        temperature=0.2
    )
 
    return json.loads(response.choices[0].message.content)
 
def save_outputs(data):
    with open("log_anomalies.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
 
    with open("log_anomalies.txt", "w", encoding="utf-8") as f:
        f.write(f"Log Anomaly Report ({date.today()})\n")
        f.write("=" * 55 + "\n\n")
 
        f.write("Summary:\n")
        f.write(data["summary"] + "\n\n")
 
        if data["anomalies"]:
            f.write("Anomalies:\n")
            for a in data["anomalies"]:
                f.write(f"- {a}\n")
 
        f.write(f"\nSeverity:\n{data['severity']}\n")
        f.write(f"\nTime Context:\n{data['time_context']}\n")
 
        if data["investigation_focus"]:
            f.write("\nInvestigation Focus:\n")
            for i in data["investigation_focus"]:
                f.write(f"- {i}\n")
 
def main():
    logs = read_logs()
    analysis = interpret_anomalies(logs)
    save_outputs(analysis)
    print("Log anomaly detection completed successfully.")
 
if __name__ == "__main__":
    main()