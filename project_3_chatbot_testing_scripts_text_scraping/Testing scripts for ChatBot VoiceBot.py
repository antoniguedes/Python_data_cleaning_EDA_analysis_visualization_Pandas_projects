 #1. Load & Clean Data
import pandas as pd

# Load logs or test cases
df = pd.read_csv("chatbot_logs.csv")

# Drop empty rows
df = df.dropna(subset=["user_message", "bot_response"])

# Normalize text (lowercase, trim spaces)
df["user_message"] = df["user_message"].str.lower().str.strip()
df["bot_response"] = df["bot_response"].str.lower().str.strip()



#🔍 2. Search / Pattern Matching
import re

# Find all bot responses that contain "error"
errors = df[df["bot_response"].str.contains("error", flags=re.IGNORECASE)]

# Regex example: detect tracking numbers
df["has_tracking_number"] = df["bot_response"].str.contains(r"\b\d{10}\b")



#📊 3. Quick Metrics
# Fallback rate (e.g., when bot says "I don't understand")
fallback_rate = (df["bot_response"] == "sorry, i didn't understand.").mean()

# Average conversation length (if sessions are grouped)
avg_conv_len = df.groupby("session_id").size().mean()

print("Fallback rate:", fallback_rate)
print("Average conversation length:", avg_conv_len)



#🌐 4. API Testing
import requests

queries = ["Where is my order?", "How do I reset my password?"]

for q in queries:
    r = requests.post("https://chatbot.api/ask", json={"query": q})
    response = r.json().get("response", "")
    print(f"Q: {q}\nA: {response}\n")



#✅ 5. Automated Validation
test_cases = [
    {"query": "What are your opening hours?", "expected": "9am"},
    {"query": "Where is my order?", "expected": "tracking"},
]

for case in test_cases:
    r = requests.post("https://chatbot.api/ask", json={"query": case["query"]})
    response = r.json().get("response", "").lower()
    assert case["expected"] in response, f"Failed: {case['query']}"



#📈 6. Simple Visualization
import matplotlib.pyplot as plt

# Most frequent user queries
df["user_message"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 User Queries")
plt.show()



#📝 7. Logging & Debugging
import logging

logging.basicConfig(filename="bot_test.log", level=logging.INFO)

try:
    r = requests.post("https://chatbot.api/ask", json={"query": "test"})
    logging.info("Bot response: %s", r.json())
except Exception as e:
    logging.error("Error calling bot API: %s", e)