#%%
import numpy as np 
import pandas as pd 
import cv2 
#%%
data=pd.read_csv('3.csv')
img=cv2.imread('3.jpg')
#%%
for i in range(len(data)):
    confidence=data.iloc[i,1]
    l_gaze_x=data.iloc[i,2]
    l_gaze_y=data.iloc[i,3]
    r_gaze_x=data.iloc[i,5]
    r_gaze_y=data.iloc[i,6]
    avg_gaze_x=l_gaze_x+r_gaze_x
    avg_gaze_y=l_gaze_y+r_gaze_y
    l_center_x=int((data.iloc[i,34]+data.iloc[i,38])/2)
    l_center_y=int((data.iloc[i,90]+data.iloc[i,94])/2)
    r_center_x=int((data.iloc[i,62]+data.iloc[i,66])/2)
    r_center_y=int((data.iloc[i,118]+data.iloc[i,122])/2)
    eye_center_x=int(data.iloc[i,324])
    eye_center_y=int(data.iloc[i,392])
    mouth_center_x=int(data.iloc[i,359])
    mouth_center_y=int(data.iloc[i,427])
    gaze_v_len=((eye_center_x-mouth_center_x)**2+(eye_center_y-mouth_center_y)**2)**0.5
    l_most_x=int(data.iloc[i,19])
    l_most_y=int(data.iloc[i,75])
    r_most_x=int(data.iloc[i,53])
    r_most_y=int(data.iloc[i,109])
    rotation=data.iloc[i,295]
    ###
    l_center=(l_center_x,l_center_y)
    r_center=(r_center_x,r_center_y)
    eye_center=(eye_center_x,eye_center_y)
    l_most=(l_most_x,l_most_y)
    r_most=(r_most_x,r_most_y)        
    #r_dest=(int(r_center_x+500*r_gaze_x),int(r_center_y+500*r_gaze_y))
    ###
    if rotation>=0.35 and rotation <=0.50 :
        gaze_x=-(eye_center_y-mouth_center_y)/gaze_v_len
        gaze_y=(eye_center_x-mouth_center_x)/gaze_v_len
        lm_dest=(int(l_most_x+50*gaze_x),int(l_most_y+50*gaze_y))
        cv2.line(img,l_most,lm_dest,(0,255,0),2,8)    
    elif rotation>=-0.50 and rotation<=-0.35       gaze_x=(eye_center_y-mouth_center_y)/gaze_v_len
        gaze_y=-(eye_center_x-mouth_center_x)/gaze_v_len
        rm_dest=(int(r_most_x+50*gaze_x),int(r_most_y+50*gaze_y))
        cv2.line(img,r_most,rm_dest,(0,255,0),2,8)    
    elif rotation>-0.35 and rotation<0.35:
        eye_dest=(int(eye_center_x+50*avg_gaze_x),int(eye_center_y+50*avg_gaze_y))
        cv2.line(img,eye_center,eye_dest,(0,255,0),2,8)
    #cv2.line(img,l_center,l_dest,(0,255,0),2,8)
    #cv2.line(img,r_center,r_dest,(0,255,0),2,8)
#%%
cv2.imwrite('./3_after1.jpg',img)
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()