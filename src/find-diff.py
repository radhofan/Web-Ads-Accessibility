import pandas as pd
import os
# Define file paths and sheet name

files = os.listdir('Web-Ads-Accessibility/src/output/')
sheet_name = 'Issues'

directory = 'Web-Ads-Accessibility/src/output/'



files = os.listdir(directory)

for file in files:
    print(file)
    normal_dir = os.path.join(directory, file, 'normal')
    adblock_dir = os.path.join(directory, file, 'adblock')
    if os.path.exists(normal_dir):
        normal_files = [f for f in os.listdir(normal_dir) if f.endswith('.xlsx')]
    if os.path.exists(adblock_dir):
        adblock_files = [f for f in os.listdir(adblock_dir) if f.endswith('.xlsx')]
    if len(normal_files) == 1:
        normal_file_path = os.path.join(normal_dir, normal_files[0])
    else:
        continue
    if len(adblock_files) == 1:
        adblock_file_path = os.path.join(adblock_dir, adblock_files[0])
    else:
        continue
    
    print(f'Extracting Ads-specfic Violations')

    df1 = pd.read_excel(normal_file_path, sheet_name=sheet_name)
    df2 = pd.read_excel(adblock_file_path, sheet_name=sheet_name)

    df1_filtered = df1[df1['WCAG level'].notna()] 
    df2_filtered = df2[df2['WCAG level'].notna()]

    df1_only = df1_filtered[~df1_filtered['Code'].isin(df2_filtered['Code'])]
    df2_only = df2_filtered[~df2_filtered['Code'].isin(df1_filtered['Code'])]

    df1_only_all_columns = pd.merge(df1_filtered, df1_only, how='inner')
    df2_only_all_columns = pd.merge(df2_filtered, df2_only, how='inner')

    df_difference = pd.concat([df1_only_all_columns, df2_only_all_columns])

    output_file_path = f'differences/{normal_files[0]}_difference.csv'
    df_difference.to_csv(output_file_path, index=False)

    print(f'Difference saved to {output_file_path}')

print("Done!!")
