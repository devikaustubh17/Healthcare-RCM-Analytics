import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("RCM Workflow Analysis Started")

num_claims = 5000

claim_id = np.arange(1, num_claims+1)

# Simulate claim processing
claim_status = np.random.choice(
    ["Approved", "Denied"], 
    size=num_claims, 
    p=[0.7, 0.3]
)

denial_reason = np.where(
    claim_status == "Denied",
    np.random.choice(
        ["Coding Error","Missing Info","Insurance Issue"], 
        size=num_claims
    ),
    "None"
)

reprocessed = np.where(
    claim_status == "Denied",
    np.random.binomial(1,0.6,size=num_claims),
    0
)

revenue = np.where(
    claim_status == "Approved",
    np.random.randint(1000,5000,size=num_claims),
    0
)

df = pd.DataFrame({
"claim_id":claim_id,
"claim_status":claim_status,
"denial_reason":denial_reason,
"reprocessed":reprocessed,
"revenue":revenue
})

df.to_csv("rcm_dataset.csv",index=False)

print(df.head())

# Metrics
total_claims = len(df)
denied = (df["claim_status"]=="Denied").sum()
approved = (df["claim_status"]=="Approved").sum()

denial_rate = denied / total_claims

print("\nRCM Metrics")
print("Total Claims:",total_claims)
print("Denied Claims:",denied)
print("Denial Rate:",denial_rate)

# Visualization
df["claim_status"].value_counts().plot(kind="bar")

plt.title("Claim Approval vs Denial")

plt.savefig("visuals/claim_status.png")

plt.show()