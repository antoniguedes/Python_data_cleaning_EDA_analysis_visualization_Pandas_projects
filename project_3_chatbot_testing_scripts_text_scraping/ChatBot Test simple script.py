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
