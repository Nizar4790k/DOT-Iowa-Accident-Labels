# DOT-Iowa-Accident-Labels

## To run these scripts follow the steps below:

1.  Modify the .env file to change the Iowa DoT Dataset path by default you can place it on root folder. 

2.  Make sure the dataset has a similar structure like this:

```bash
Iowa DoT Accidents Dataset
├── 2016
│   └── 20161127-01 Work Zone Crash.zip
├── 2017
│   └── 20171216 CR I-380 Rollover Crash.zip
├── 2018
│   └── 20180222 DM I-235 WB Valley West Dr Crash.zip
├── 2019
│   └── 20191221 SC I-29 at Singing Hills Rd Crash.zip
└── 2020
    └── 20200223 CB I-29 80 Motorcycle pursuit crash.zip
 ```
 
3.  Run the command "pip3 install -r requirements.txt" to install the requeriments.

4.  Run "python3 DOT_Iowa_Accident_Labels.py"

