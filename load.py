import os
import subprocess
import shlex
import ffmpeg


stream = ffmpeg.input('/Users/viksriva/Documents/blurred_confetti.mp4')
stream = ffmpeg.hflip(stream)

stream = ffmpeg.filter(scale_input, 'scale', output_width, output_height, 'lanczos')

stream = ffmpeg.overwrite_output(stream, 'output.mp4')
ffmpeg.run(stream)

with open('/Users/viksriva/Documents/gource-release/text_file.txt', 'r') as f:
    lines = f.readlines()

print(''.join(lines))

cmd = """
ffmpeg -y -i /Users/viksriva/Documents/blurred_confetti.mp4  -filter:v "setpts=0.1*PTS" -vf "[in]format=yuv444p, \drawbox=y=ih/PHI:color=black@0.4:width=iw:height=1000:t=fill, \drawtext=fontfile=OpenSa
ns-Regular.ttf:text='{}':fontcolor=white:fontsize=24:x=(w-tw)/2:y=(h-th)/2-200, format=yuv420p" \-c:v libx264 -c:a copy -movflags +faststart output.mp4
""".format('\n'.join(lines))
print(cmd)
commands = shlex.split(cmd)
process = subprocess.Popen(commands)
process.wait()



"""
ffmpeg -y
-i /Users/viksriva/Documents/blurred_confetti.mp4
-filter:v "setpts=0.1*PTS"
-filter_complex
    "[in]format=yuv444p [1];
    [1] pad=width=iw:height=ih+200:x=0:y=100:color=#f2e6e6@0.99 [v_1];
    [v_1]
        \drawbox=y=ih/PHI:color=black@0.4:width=iw:height=1000:t=fill,
        drawtext=
            fontfile='OpenSans-Regular.ttf':
            text='this is watermark': fontsize=24:
            x=0.23333333333333*main_w: y=0.1325*main_h:
            fontcolor=#b01e1e: alpha=1,
        drawtext=
            fontfile='OpenSans-Regular.ttf':
            text='This is Top fixed text': fontsize=32:
            x=w-tw-2: y=(100-th)/2: fontcolor=#9e2643: alpha=1,
        drawtext=
            fontfile='OpenSans-Regular.ttf':
            text='This is Bottom fixed text': fontsize=32:
            x=w-tw-2: y=h-50: fontcolor=#9e2643: alpha=1
    [v_2];
    [v_2] [1]overlay=main_w-140:105 [v_3]"
-map "[v_3]"
-map 0:a
video-final.mp4
"""