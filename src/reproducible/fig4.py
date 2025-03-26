import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

directory = 'Web-Ads-Accessibility/src/differences'
files = os.listdir(directory)

print("----------------------Figure 4--------------------")
# List to store count of violations for each file
violations_count = []

# Iterate through each file and calculate the number of violations
for file in files:
    file_path = os.path.join(directory, file)
    df = pd.read_excel(file_path)
    violations_count.append(len(df))

# Sort the violations_count for CDF
violations_count = sorted(violations_count)

# Calculate the CDF
cdf = np.arange(1, len(violations_count) + 1) / len(violations_count)

# Plot CDF
plt.figure(figsize=(5, 4))
plt.plot(violations_count, cdf, marker='o', linestyle='-', label='CDF')
plt.xlabel('WCAG Guideline Violation on Ads')
plt.ylabel('Propotion of websites')
plt.title('Figure 4')
plt.grid(True)
plt.xlim(0, 500)
plt.ylim(0, 1)
plt.show()
