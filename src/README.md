## Running from Scratch Without a Virtual Machine
> This may cause errors if the ChromeDriver version does not match your installed version of Google Chrome. 

To run the project from scratch without using the provided Virtual Machine, follow these steps:

1. **Install Google Chrome**  
   Make sure Google Chrome is installed on your system.

2. **Install Conda**  
   Download and install [Conda](https://docs.conda.io/en/latest/miniconda.html).

3. **Create a Conda Environment**  
   Use the following command to create a Conda environment:
   ```bash
   conda create -n icse
   conda activate icse
   ```
4. **Install Required Packages**
   
   Install all the necessary dependencies listed in `requirements.txt`

5. **Run the Scripts**
   - `mkdir output`
   - `mkdir differences`
   - `bash run.sh`
   - `cd reproducible`
   - `bash reproducible.sh`
