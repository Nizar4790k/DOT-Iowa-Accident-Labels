import os
from dotenv import load_dotenv
import zipfile
from helper_functions import read_csv
from helper_functions import get_video_formats
from helper_functions import extract_frames


load_dotenv()


data = read_csv('DOT_Iowa_Accident_Labels_all.csv') # loading the csv



formats = get_video_formats(data)


os.chdir((os.environ['WORKING_DIRECTORY'])) # loading the working directory



years = os.listdir() # listing years folders



for year in years:
    
    
  
    os.chdir(year)
    files = os.listdir()

    for file in files:
       
        if file.endswith(".zip"):
           with zipfile.ZipFile(file,'r') as zip_ref:
                zip_ref.extractall()
        
    os.chdir("..")

    
    for root, dirs, files in os.walk(year):
        for file in files:
            
            try:
                
                
                if file.split(".")[1] in formats:
                    video_path =os.path.join(root, file)
                    #video_folder=video_path.split("/")[len(video_path)-2]
               
               
                    video_data = list(filter(lambda x: x[4]==file,data)) # filtering the video by name in the .csv file
                    
                   
                    if(video_data!=[]):
                        extract_frames(video_data[0],video_path,root)
                    else:
                        print("Video "+file+" was not found in the spreadshet")



            
            except IndexError as e :
                
                print("The file "+file+" has not extension")
                continue
            
  







