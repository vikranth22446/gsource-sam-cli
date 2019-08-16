#!./venv/bin/python
import numpy as np
from skimage import transform as tf
from moviepy.editor import *
from moviepy.video.tools.drawing import color_gradient

# RESOLUTION 

w = 720
h = w*9//16 
moviesize = w,h

txt = "\n".join([
"It is a period of civil war. Rebel",
"spaceships, striking from a",
"hidden base, have won their",
"first victory against the evil",
"Galactic Empire. During the battle,",
"Rebel spies managed to steal secret",
"plans to the Empire’s ultimate weapon,",
"the DEATH STAR, an armored space station",
"with enough power to destroy an entire planet."
"",
"",
"",
"",
"",
"",
"",
"",
"",
])



# Add blanks before and after text
txt = 10*"\n" +txt + 10*"\n"



clip_txt = TextClip(txt,color='cyan', align='Center',fontsize=25,
                    font='Xolonium-Bold', method='label')


txt_speed = 10 
fl = lambda gf,t : gf(t)[int(txt_speed*t):int(txt_speed*t)+h,:]
moving_txt= clip_txt.fl(fl, apply_to=['mask'])

# ADD A VANISHING EFFECT ON THE TEXT WITH A GRADIENT MASK

grad = color_gradient(moving_txt.size,p1=(0,2*h/3),
                p2=(0,h/4),col1=0.0,col2=1.0)
gradmask = ImageClip(grad,ismask=True)
fl = lambda pic : np.minimum(pic,gradmask.img)
moving_txt.mask = moving_txt.mask.fl_image(fl)




stars = ImageClip('./confetti.gif')
stars_darkened = stars.fl_image(lambda pic: (0.6*pic).astype('int16'))



final = CompositeVideoClip([
         stars_darkened,
         moving_txt.set_pos(('center','bottom'))],
         size = moviesize)


# WRITE TO A FILE
# duration here set to 35 seconds, with 18 frames per second

final.set_duration(35).write_videofile("star_wars_crawl.mp4", 
                                       fps=18, codec='libx264')

# "[in]drawtext=font='Arial': text='This is text line 1':x=(w-tw)/2:y=((h-text_h)/2)-(text_h-(th/4)): fontsize=55: fontcolor=red, drawtext=font='Arial': text='This is text line 2':x=(w-tw)/2:y=((h-text_h)/2)+(text_h-(th/4)): fontsize=55: fontcolor=green[out]"
