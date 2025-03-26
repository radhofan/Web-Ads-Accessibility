#!/usr/bin/env bash

# Install Miniconda
curl -fsSL https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o miniconda.sh
bash miniconda.sh -b -p $HOME/miniconda <<< "Yes"

# Set environment variables
export PATH="$HOME/miniconda/bin:$PATH"
export MAMBA_ROOT_PREFIX="$HOME/miniconda"

# Install Mamba
conda install -c conda-forge mamba -y

# Initialize Mamba shell
mamba shell init --shell=bash
source ~/.bashrc  # Reload shell config
eval "$(mamba shell hook --shell=bash)"

# Create and activate conda environment
mamba create -n icse
source $HOME/miniconda/bin/activate icse
mamba activate icse

# install requirements
pip install -r Web-Ads-Accessibility/src/requirements.txt
pip install gdown
pip install selenium
pip install pandas

# run
mkdir Web-Ads-Accessibility/src/output
mkdir Web-Ads-Accessibility/src/differences
bash Web-Ads-Accessibility/src/run.sh 
bash Web-Ads-Accessibility/src/reproducible/reproducible.sh
