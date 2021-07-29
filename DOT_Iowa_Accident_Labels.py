import os
from dotenv import load_dotenv
import zipfile
import shutil
import csv
import cv2
load_dotenv()



def get_video_formats(data):
    formats = list()
    for video in data:
        try:
            format = video[4].split(".")[1] # This is the video format
            formats.append(format)
        except:
            continue
    
    formats = set(formats)

    return formats


def read_csv(filename):
     with open(filename, 'r') as f:
    # reads csv into a list of lists
        lines = csv.reader(f, delimiter=',') 
        return list(lines)[1:] #



def extract_frames(video_data,video_path,root):
    video_name = video_data[4]
    
    
    times = [   # This is the pre-collision, collision and post-collision times
    ["pre",video_data[7]],
    ["col",video_data[8]],
    ["post",video_data[9]]]


    vidcap=cv2.VideoCapture(video_path) # Loading the video 
    
    i=0

    framerate = round (vidcap.get(5)) 
    
    try:

        frame_start=int(times[0][1])*framerate
        frame_end=(int(times[2][1])+1)*framerate
    except:
        print("The frame start or frame end are not int")
        return
    

    for frame_number in range(frame_start,frame_end):
       
        if(i>2):
            break
        
        vidcap.set(cv2.CAP_PROP_POS_MSEC,float((frame_number/framerate)*1000)) # Capturing the frame in the time specified in ms
        success,image=vidcap.read()

        if success:
          

            if (frame_number/framerate)==float(times[i][1]):
                cv2.imwrite(root+"/"+video_name.split(".")[0]+"_"+times[i][0]+"_"+str(frame_number)+".jpg",image) # writing the image
                i=i+1
            else:
                cv2.imwrite(root+"/"+video_name.split(".")[0]+"_"+times[i][0]+"_"+str(frame_number)+".jpg",image)
       

            


"""
    for time in times:
       
        vidcap.set(cv2.CAP_PROP_POS_MSEC,float(int(time[1])*1000)) # Capturing the frame in the time specified in ms
        success,image=vidcap.read()

        if success:
            framerate = round (vidcap.get(5)) 
            
            frame_number = framerate * int(time[1])
            cv2.imwrite(video_name.split(".")[0]+"_"+time[0]+"_"+str(frame_number)+".jpg",image) # writing the image
"""

    

    

data = read_csv('DOT_Iowa_Accident_Labels_all.csv') # loading the csv



formats = get_video_formats(data)


os.chdir((os.environ['WORKING_DIRECTORY'])) # loading the working directory



years = os.listdir() # listing years folders

print(get_video_formats(data))

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
            #try:
            current_directory = os.getcwd()
                
            if file.split(".")[1] in formats:
                video_path =os.path.join(root, file)
                #video_folder=video_path.split("/")[len(video_path)-2]
               
               
                video_data = list(filter(lambda x: x[4]==file,data)) # filtering the video by name in the .csv file
                print(file,video_data)
                   
                if(video_data!=[]):
                    extract_frames(video_data[0],video_path,root)
                else:
                    print("Video not found in the spreadshet")



            """
            except Exception as e :
                
                print(file,"THE FILE DOESN'T HAVE AN EXTENSION")
                continue
            """
    """
        if file.endswith(".zip"):
           with zipfile.ZipFile(file,'r') as zip_ref:
                zip_ref.extractall()
    """  
        
    """
        if os.path.isdir(file):
            shutil.rmtree(file)
            continue
        
        with zipfile.ZipFile(file,'r') as zip_ref: #extracting the files
                zip_ref.extractall()
        
        folder_name = file.split(".")[0]
       
        os.chdir(folder_name)
        
        video_names = os.listdir()

       

        video_data = list(filter(lambda x: x[4]==video_names[0],data)) # filtering the video by name in the .csv file
        
        extract_frames(video_data[0])

        # Extract frames
        
        os.chdir("..")
        os.chdir('..')
        
        

        print(os.listdir())
    """
  







