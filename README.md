# Accessibility Issues in Ad Driven Web Applications

---

**Abdul Haddi Amjad** , Muhammad Danish, Bless Jah, Muhammad Ali Gulzar IEEE International Conference on Software Engineering (ICSE) 2025

## Artifact Badge Request:

### 1. Available

<img src="image/README/0-avail.png" alt="Alt text" width="45" height="45">

### 2. Functional

<img src="image/README/0-func.png" alt="Alt text" width="45" height="45">

### 3. Reusable

<img src="image/README/0-reus.png" alt="Alt text" width="45" height="45">

---

## Introduction

This paper, Accessibility Issues in Ad-Driven Web Applications, explores the impact of third-party advertisements on web accessibility. It identifies common accessibility violations introduced by ads, such as improper focus management and non-descriptive elements, and evaluates their compliance with WCAG guidelines. The study also provides actionable recommendations to improve accessibility in ad-driven web environments.

This is a public repository and zenodo link to download Virtual Machine (`.ova`) ([https://zenodo.org/records/14742897](https://zenodo.org/records/14742897)), **available** to everyone.

![1737894596764](image/README/meth.png)

---
## Installation

> **Ensure you follow the next steps on either a Mac (Intel) or Windows system.**
> **For any additional configurations or assistance, feel free to contact us at hadiamjad@vt.edu**

1. Install VM Ware Fusion using these steps: [https://services.tctc.edu/TDClient/323/InfoTech/KB/ArticleDet?ID=21304]()
2. Install VM Machine (`.ova`) of from this link: [https://zenodo.org/records/14742897]()

### VM Machine Requirements

The downloadable size of the VM machine is approximately **22GB**.

**System Requirements:**
- **RAM:** 16GB
- **Hard Drive Space:** 50GB
- **CPU Cores:** 4
- **Supported Platforms:** macOS (Intel) or Windows

### What the VM Machine Includes:

- **Google Chrome**: Pre-installed for web browsing and testing.  
- **VS Code**: A fully configured code editor.  
- **Conda (`conda activate icse`)**: A preinstalled Python environment for seamlessly running code files and managing dependencies.  
- **Shell Script to Reuse Methodology (`run.sh`)**: Streamlines the application of our methodology.  
- **Shell Script to Reproduce Paper Results (`reproducible.sh`)**: Enables exact reproduction of the results presented in our paper.  

### If the VM Machine Prompts for a Code:

- **Code**: The code is **0000** (four zeros).  

---
## Steps to Import/Open the VM Machine in VMware Fusion

1. **Download the VM Machine**:  
   Ensure you have downloaded the VM machine file (approximately 22GB) to your system.

2. **Open VMware Fusion**:  
   Launch the VMware Fusion application on your macOS (Intel) or Windows device.

3. **Import the VM Machine**:  
   - Open VMware Fusion and click `File` in the top-left corner.  
   - From the dropdown menu, select `Import`.  
   <img src="image/README/1.png" alt="Import VM in VMware Fusion" width="480" height="320">

4. **Choose the `.ova` File**:  
   - Click `Choose File` and browse to the location of the downloaded `.ova` file from the previous step.  
   <img src="image/README/2.png" alt="Choose .ova File" width="480" height="320">

5. **Name and Save**:  
   - Assign a name to the virtual machine (e.g., `icse`) and click `Save`.  
   <img src="image/README/3.png" alt="Name and Save the VM" width="480" height="320">

6. **Wait for Import**:  
   - The virtual machine will start importing. This process may take a 15-30 minutes.  
   - **Note**: You don't have to configure resources but while importing if the system resources (RAM, CPU, Space etc.) are insufficient, you may encounter an error.  
   <img src="image/README/4.png" alt="Import Process" width="480" height="320">

7. **Complete Import**:  
   - Once the import is complete, click `OK` on the pop-up window and start the machine.  
   <img src="image/README/5.png" alt="Start the Machine" width="480" height="320">

8. **Enter the Code (if prompted)**:  
   - If prompted, enter `0000` (four zeros) as the code.  
   <img src="image/README/6.png" alt="Enter Code" width="480" height="320">

9. **Open VS Code**:  
   - Launch **VS Code** from the side dock.  
   - Open the folder located in `Downloads/icse`.  
   <img src="image/README/7.png" alt="Open Folder in VS Code" width="480" height="320">

10. **Activate the Conda Environment**:  
    - Open the terminal in VS Code and activate the Conda environment by running:  
      ```bash
      conda activate icse
      ```  
    <img src="image/README/8.png" alt="Activate Conda Environment" width="480" height="320">

11. **Run the Shell Script to Reuse Methodology**:  
    - Execute the following command:  
      ```bash
      bash run.sh
      ```  
    - This step uses Selenium automation to perform the following operations, which will take approximately 15 minutes to complete:  
      - **Crawl the Website with Ads**: The script will crawl the website specified in `websites.txt` (e.g., `alaskanewssource.com`) with ads enabled.  
      - **Crawl the Website without Ads**: The script will then crawl the same website without ads.  
      - **Extract Ad-Specific Violations**: It will identify and extract accessibility violations introduced by ads.  
      <img src="image/README/9.png" alt="Script Running Example" width="480" height="320">

12. **View the Results**:  
    - Once the script finishes running, you will see the following output in the terminal:  
      <img src="image/README/10.png" alt="Terminal Output Example" width="480" height="320">  
    - This concludes the three-step methodology as outlined in the paper:
        1. **Crawling with Ads**: Results are saved in the folder `output/normal/`.  
        2. **Crawling without Ads**: Results are saved in the folder `output/adblock/`.  
        3. **Extracting Ad-Specific Violations**: The differences are saved in the `differences/` folder, containing `.csv` files that highlight ad-specific accessibility violations. The folder is also visible in the left panel for easy access.  

---

### 3. Reproducible

You can use the previous virtual machine to generate the results of the paper.

1. Go to the reproducible directory:

`cd reproducible`

2. Run bash file:

`bash reproducible.sh`

<img src="image/README/11.png" alt="Alt text" width="480" height="320">

3. It will generate results in following order:

##### Table 2:

> First two rows are just the sum of all:

<img src="image/README/12.png" alt="Alt text" width="480" height="320">
<img src="image/README/13.png" alt="Alt text" width="480" height="320">

##### Table 3:

<img src="image/README/14.png" alt="Alt text" width="480" height="320">
<img src="image/README/15.png" alt="Alt text" width="480" height="320">

##### Table 4:

> You can scroll up and down to see the all top 5

<img src="image/README/16.png" alt="Alt text" width="480" height="320">
<img src="image/README/17.png" alt="Alt text" width="480" height="320">

##### Figure 4:

> You can close the figure to move to the next step

<img src="image/README/18.png" alt="Alt text" width="480" height="320">
<img src="image/README/19.png" alt="Alt text" width="480" height="320">

##### Figure 5:

> You can close the figure to move to the next step

<img src="image/README/20.png" alt="Alt text" width="480" height="320">
<img src="image/README/21.png" alt="Alt text" width="480" height="320">

##### Figure 8a:

> You can close the figure to move to the next step

<img src="image/README/22.png" alt="Alt text" width="480" height="320">
<img src="image/README/23.png" alt="Alt text" width="480" height="320">

##### Figure 8b:

> You can close the figure to move to the next step

<img src="image/README/24.png" alt="Alt text" width="480" height="320">
<img src="image/README/25.png" alt="Alt text" width="480" height="320">

##### Figure 8c:

> You can close the figure to move to the next step

<img src="image/README/26.png" alt="Alt text" width="480" height="320">
<img src="image/README/27.png" alt="Alt text" width="480" height="320">
