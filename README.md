# Accessibility Issues in Ad Driven Web Applications

---

**Abdul Haddi Amjad** , Muhammad Danish, Bless Jah, Muhammad Ali Gulzar IEEE International Conference on Software Engineering (ICSE) 2025

## Artifact Badge Request:

---

### 1. Available

<img src="image/README/0-avail.png" alt="Alt text" width="45" height="45">

This is a public repository and zenodo link to download Virtual Image (`.ova`) ([https://zenodo.org/records/12775210](https://zenodo.org/records/12775210)), accessible to everyone.

---

### 2. Functional

<img src="image/README/0-func.png" alt="Alt text" width="45" height="45">

We have created a Virtual Image (`.ova`) to implement the methodology described in the paper. This allows you to specify a website to be crawled both with and without ads, generate accessibility reports for each instance, and extract ad-specific accessibility violations.

![1737894596764](image/README/meth.png)

#### Steps:

> **Ensure you follow the next steps on either a Mac (Intel) or Windows system.**

1. Install VM Ware Fusion Using these steps: [https://services.tctc.edu/TDClient/323/InfoTech/KB/ArticleDet?ID=21304]()
2. Install VM Image(`.ova`) from this link:
3. Now open VM Ware Fusion and click `File` on the top left corner and from dropdown choose `import` (mac):
<img src="image/README/1.png" alt="Alt text" width="480" height="320">
4. Click `choose file` and browse to (`.ova`) file you have downloaded in previous step:
<img src="image/README/2.png" alt="Alt text" width="480" height="320">
5. You can name as `icse` and click `save`:
<img src="image/README/3.png" alt="Alt text" width="480" height="320">
6. Now it will start importing the Virtual Machine (this step take couple of minutes):

> Note as specified earlier, it will give error if resources are not sufficient on the machine.
<img src="image/README/4.png" alt="Alt text" width="480" height="320">
7. Once import is done, click `ok` on this pop-up and start the machine:
<img src="image/README/5.png" alt="Alt text" width="480" height="320">
8. If you see this pop-up, then just enter `0000` (four time zero digit) as a code:
<img src="image/README/6.png" alt="Alt text" width="480" height="320">
9. Open VS code from side dock.

10. Open Folder, present in `Downloads/icse`:
<img src="image/README/7.png" alt="Alt text" width="480" height="320">
11. Open the terminal and activate the conda environment `conda activate icse`:
<img src="image/README/8.png" alt="Alt text" width="480" height="320">
12. Now run `bash run.sh`:

> This step uses selenium-automation to automatically open and perform following operations and it will take around ~15mins to complete

 - This will first crawl website specified in `websites.txt` (in this case we are crawling alaskanewssource.com) WITH ADS
 - Then it will crawl crawl website specified in `websites.txt` (in this case we are crawling alaskanewssource.com) WITHOUT ADS
 - Extract ADS-specific violations
<img src="image/README/9.png" alt="Alt text" width="480" height="320">
13. After successfull run, you will see the following output on terminal:
<img src="image/README/10.png" alt="Alt text" width="480" height="320">
> difference folder on the left panel has the ads-specific violations saved in `.csv` format. 

This completes our three-step methodology as specified in the paper

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
