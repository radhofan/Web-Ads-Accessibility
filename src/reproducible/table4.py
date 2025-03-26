import re
import os
import pandas as pd
import tldextract

def getDomain(url):
    ext = tldextract.extract(url)
    return ext.domain + "." + ext.suffix

def find_domains(text):
    # Regular expression pattern to find URLs within a string
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    # Using re.findall() to extract all URLs from the input text
    urls = re.findall(url_pattern, text)

    # Extracting domains from URLs
    domains = []
    for url in urls:
        domains.append(getDomain(url))

    return domains

directory =  'Web-Ads-Accessibility/src/differences'
files = os.listdir(directory)
# Excluded domains
excluded_domains = {"postrelease.com", "globo.com"}
# Dictionary to store count of issues each domain appears in across all files
domain_issues = {}

# Dictionary to store the count of files each domain appears in
domain_file_count = {}

# Iterate through each file
for file in files:
    file_path = os.path.join(directory, file)
    df = pd.read_excel(file_path)
    # Extract domains from 'code' column
    if 'Code' in df.columns:
        # Keep track of domains already found in this file
        domains_in_file = set()
        for index, row in df.iterrows():
            domains = find_domains(row['Code'])
            for domain in domains:
                if domain not in domain_issues:
                    domain_issues[domain] = {}
                    domain_file_count[domain] = 0

                # Count occurrences of issues
                issue = str(row['Checkpoint'])  # Assuming 'Checkpoint' is the column name
                if issue in domain_issues[domain]:
                    domain_issues[domain][issue] += 1
                else:
                    domain_issues[domain][issue] = 1

                # Track the file where this domain appears
                if domain not in domains_in_file:
                    domain_file_count[domain] += 1
                    domains_in_file.add(domain)

# Calculate the total issue count for each domain
total_issue_count = {domain: sum(issues.values()) for domain, issues in domain_issues.items()}

# Sorting domains based on total issue count in descending order
sorted_domains = sorted(total_issue_count.items(), key=lambda x: x[1], reverse=True)[:7]

print("----------------------Table 4--------------------")
# Printing the sorted domains
for domain, issue_count in sorted_domains:
    if domain in excluded_domains:
        continue  # Skip the excluded domains
    file_count = domain_file_count[domain]
    print(f"Domain: {domain} (Websites: {file_count}, Total Violations: {issue_count})")
    sorted_issues = sorted(domain_issues[domain].items(), key=lambda x: x[1], reverse=True)
    for issue, count in sorted_issues:
        print(f"  Violation: {issue}, Count: {count}")
    print()
