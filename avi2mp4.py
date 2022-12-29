import os
import natsort
import pathlib

def convert_avi_to_mp4(avi_file_path, output_name):
    os.popen("ffmpeg -i '{input}' -ac 2 -b:v 2000k -c:a aac -c:v libx264 -b:a 160k -vprofile high -bf 0 -strict experimental -f mp4 '{output}.mp4'".format(input = avi_file_path, output = output_name))
    return True

if __name__ == "__main__":
    DIR = "/HDD/osan_2021"
    
    video_list = []
    print(DIR)
    for root, dirs, files in os.walk(DIR):
        for file in files:
            if file.endswith(".avi"):
                # print(os.path.join(root, file))
                video_list.append(os.path.join(root, file))
 
    video_list = natsort.natsorted(video_list)
    print(video_list)
    
    for idx, file_name in enumerate(video_list):
        target_file_name = pathlib.Path(file_name)
        new_file_name = str(pathlib.Path(target_file_name.parent, target_file_name.stem))
        print("target_file_name", target_file_name)
        print("new_file_name", new_file_name, ".mp4")
        
        cvt_rs = convert_avi_to_mp4(target_file_name, new_file_name)
        if cvt_rs:
            os.remove(file_name)
            print("remove :", file_name)
            
        
        
