import csv
import cv2
from tqdm import tqdm


def get_video_formats(data): # This function loads  all the supported extensions from spreadsheet.
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

    framerate = round (vidcap.get(5))  # getting framerate
    
    try:

        frame_start=int(times[0][1])*framerate # calculating frame_start and frame_end
        frame_end=(int(times[2][1])+1)*framerate
    except:
        print(video_name+":","The frame start or frame end are not int")
        return
    
  
   
    for frame_number in tqdm(range(frame_start,frame_end),desc="Procesing "+video_name): # tqdm is the progressbar.
       
        if(i>2):
            break
        
        vidcap.set(cv2.CAP_PROP_POS_MSEC,float((frame_number/framerate)*1000)) # Capturing the frame in the time specified in ms
        success,image=vidcap.read()

        if success:
          

            if (frame_number/framerate)==float(times[i][1]):
                cv2.imwrite(root+"/"+video_name.split(".")[0]+"_"+times[i][0]+"_"+str(frame_number)+".jpg",image) # writing the image
                i=i+1
            else:
                cv2.imwrite(root+"/"+video_name.split(".")[0]+"_"+times[i][0]+"_"+str(frame_number)+".jpg",image)# writing the image
       