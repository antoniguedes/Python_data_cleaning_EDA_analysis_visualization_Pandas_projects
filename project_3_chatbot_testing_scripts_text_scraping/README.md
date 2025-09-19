# 🤖 Chatbot/Voicebot Testing Toolkit

This repository contains Python scripts and snippets for testing, validating, and analyzing chatbot and voicebot responses. Includes examples for loading data, automated validation, API testing, metrics calculation, and visualization.

---

## 📝 Example: A Simple Bot Test Script

This is a basic Python script to test chatbot responses against expected outputs using a CSV file of test cases.

```python
import requests
import pandas as pd

# Load test cases
test_cases = pd.read_csv("bot_test_cases.csv")  # columns: "query", "expected"

results = []

for _, row in test_cases.iterrows():
    r = requests.post("https://chatbot.api/ask", json={"query": row["query"]})
    answer = r.json().get("response", "")
    
    passed = row["expected"].lower() in answer.lower()
    results.append({"query": row["query"], "response": answer, "passed": passed})

# Save results
df = pd.DataFrame(results)
df.to_csv("test_results.csv", index=False)

print(df["passed"].mean(), "success rate")
```
---
## 🧰 Python Testing Toolkit Snippets  
### 📂 1. Load & Clean Data  
```python

import pandas as pd

# Load logs or test cases
df = pd.read_csv("chatbot_logs.csv")

# Drop empty rows
df = df.dropna(subset=["user_message", "bot_response"])

# Normalize text (lowercase, trim spaces)
df["user_message"] = df["user_message"].str.lower().str.strip()
df["bot_response"] = df["bot_response"].str.lower().str.strip()
```

### 🔍 2. Search / Pattern Matching  
```python
Copy code
import re

# Find all bot responses that contain "error"
errors = df[df["bot_response"].str.contains("error", flags=re.IGNORECASE)]

# Regex example: detect tracking numbers
df["has_tracking_number"] = df["bot_response"].str.contains(r"\b\d{10}\b")
```

### 📊 3. Quick Metrics  
```python
Copy code
# Fallback rate (e.g., when bot says "I don't understand")
fallback_rate = (df["bot_response"] == "sorry, i didn't understand.").mean()

# Average conversation length (if sessions are grouped)
avg_conv_len = df.groupby("session_id").size().mean()

print("Fallback rate:", fallback_rate)
print("Average conversation length:", avg_conv_len)
```  

### 🌐 4. API Testing  
```python
Copy code
import requests

queries = ["Where is my order?", "How do I reset my password?"]

for q in queries:
    r = requests.post("https://chatbot.api/ask", json={"query": q})
    response = r.json().get("response", "")
    print(f"Q: {q}\nA: {response}\n")
```

### ✅ 5. Automated Validation  
```python
Copy code
test_cases = [
    {"query": "What are your opening hours?", "expected": "9am"},
    {"query": "Where is my order?", "expected": "tracking"},
]

for case in test_cases:
    r = requests.post("https://chatbot.api/ask", json={"query": case["query"]})
    response = r.json().get("response", "").lower()
    assert case["expected"] in response, f"Failed: {case['query']}"
```

### 📈 6. Simple Visualization  
```python
Copy code
import matplotlib.pyplot as plt

# Most frequent user queries
df["user_message"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 User Queries")
plt.show()
```  

### 🛠️ 7. Logging & Debugging  
```python
Copy code
import logging

logging.basicConfig(filename="bot_test.log", level=logging.INFO)

try:
    r = requests.post("https://chatbot.api/ask", json={"query": "test"})
    logging.info("Bot response: %s", r.json())
except Exception as e:
    logging.error("Error calling bot API: %s", e)
```

### 🎯 Key Takeaways 
- pandas → clean & analyze conversation logs.

- re → detect patterns like tracking numbers, emails, error codes.

- requests → send queries to chatbot APIs.

- assert + pytest → validate responses against expectations.

- matplotlib → visualize query frequencies, error trends.

- logging → track and debug tests.
