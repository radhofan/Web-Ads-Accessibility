import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

directory =  'Web-Ads-Accessibility/src/differences'

files = os.listdir(directory)

print("----------------------Figure 5--------------------")
# List to store count of violations for each file
violations_count = []

# Iterate through each file and calculate the number of violations
for file in files:
    file_path = os.path.join(directory, file)
    df = pd.read_excel(file_path)
    violations_count.append(len(df))

bins = np.arange(0, 550, 10) 
# 
# Plot histogram
plt.figure(figsize=(5, 4))
plt.hist(violations_count, bins=bins, edgecolor='black')
plt.xlabel('Number of Violations')
plt.ylabel('# of websites')
plt.xlim(10, 500)
plt.ylim(0, 600)
plt.title('Figure 5')
plt.grid(True)
plt.show()
