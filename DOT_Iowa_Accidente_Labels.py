import os
from dotenv import load_dotenv
load_dotenv()

os.chdir((os.environ['WORKING_DIRECTORY']))

years = os.listdir()

for year in years:
    os.chdir(year)
    vids_compressed = os.listdir()
    
    for vid_compresed in vids_compressed:
        print(vid_compresed)
    os.chdir("..")

print(vids_compressed)
print(os.listdir())





