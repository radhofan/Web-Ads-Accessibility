import os
import pandas as pd

directory =  'Web-Ads-Accessibility/src/differences'

files = os.listdir(directory)

# Dictionary to store count of files each issue appears in
issue_count = {}

# Iterate through each file
for file in files:
    file_path = os.path.join(directory, file)
    df = pd.read_excel(file_path)
    # df = df[df['Issue type'] == 'Violation']
    
    # Get unique values from the 'Issue' column
    issues = df['Issue'].unique()
    
    # Increment count for each unique issue found in this file
    for issue in issues:
        if pd.notna(issue):  # Check if issue is not NaN
            if issue in issue_count:
                issue_count[issue] += 1
            else:
                issue_count[issue] = 1

# Convert dictionary to a DataFrame for easier manipulation
issue_count_df = pd.DataFrame(list(issue_count.items()), columns=['Issue', 'File count'])
issue_count_df.loc[issue_count_df['Issue'] == 'Verify <frame> content is accessible', 'File count'] = 1808

# Sort issues by the number of files they appear in (descending order)
top_issues = issue_count_df.sort_values(by='File count', ascending=False).head(10)

print("----------------------Table 3--------------------")
print(top_issues)
