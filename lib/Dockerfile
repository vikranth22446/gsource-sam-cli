From ubuntu

RUN  apt-get -y update && apt-get -y install ffmpeg git-core wget curl vim gource xvfb xfonts-base xfonts-75dpi xfonts-100dpi
RUN git clone https://github.com/awslabs/aws-sam-cli

RUN xvfb-run --auto-servernum --server-args='-screen 0, 1920x1080x16' gource aws-sam-cli/ -s .06 -1280x720 --auto-skip-seconds .1 --multi-sampling --stop-at-end --key --highlight-users --hide mouse,progress,filenames,dirnames --file-idle-time 0 --max-files 0 --background-colour 000000 --font-size 22 --title "$SAM_CLI_TAG_NAME History" -1280x720 -o $SAM_CLI_TAG_NAME-sam-cli-history.ppm

RUN ffmpeg -y -r 60 -f image2pipe -vcodec ppm -i $SAM_CLI_TAG_NAME-sam-cli-history.ppm -vcodec libx264 -preset medium -pix_fmt yuv420p -crf 1 -threads 0 -bf 0 output_videos/$SAM_CLI_TAG_NAME-sam-cli-history.mp4

ADD ./clients_secrets.json /clients_secrets.json

RUN '{
  "title": "'"$SAM_CLI_TAG_NAME "'SAM CLI History",
  "description": "SAM CLI History",
  "privacyStatus": "public",
  "embeddable": true,
  "license": "creativeCommon",
  "publicStatsViewable": true,
  "categoryId": "10",
  "language": "en"
}' > /video_meta_data.json

ADD ./request.token /request.token

RUN wget https://github.com/porjo/youtubeuploader/releases/download/19.02/youtubeuploader_linux_amd64.tar.gz && tar -xvzf youtubeuploader_linux_amd64.tar.gz && mv youtubeuploader_linux_amd64 youtubeuploader 

RUN ./youtubeuploader -filename sam-cli-history.mp4 -metaJSON video_meta_data.json


# xvfb-run --auto-servernum --server-args='-screen 0, 1920x1080x16' \
# gource --viewport '1920x1080' --path './repos/redcellvideov2/' --start-date '2017-12-05' --output-ppm-stream - | \
# ffmpeg -y -r 30 -f image2pipe -vcodec ppm -i - -vcodec libx264 -preset ultrafast -pix_fmt yuv420p -crf 1 -threads 0 -bf 0 ./renders/redcellvideov2.mp4
# https://github.com/acaudwell/Gource/issues/137


# Possibly Update from https://github.com/ktamas77/gource/blob/master/Dockerfile
# xvfb-run --auto-servernum --server-args='-screen 0, 1920x1080x24' gource --start-date='${DATE_WEEK_AGO}' --path 'aws-sam-cli/' -1920x1080 -s 10 --highlight-users --highlight-dirs --hide-filenames --camera-mode track -key --padding 1.28 --user-scale 4.0 --date-format "%Y.%m.%d" --font-size 24 --dir-name-depth 1 -a 2 -o - | ffmpeg -y -r 60 -f image2pipe -vcodec ppm -i - -vcodec libx264 -preset ultrafast -pix_fmt yuv420p -crf 1 -threads 0 -bf 0 /home/video/gource.mp4
# xvfb-run --auto-servernum --server-args='-screen 0, 1280x720' gource aws-sam-cli/ -s .06 --auto-skip-seconds .1 --multi-sampling --stop-at-end --key --highlight-users --hide mouse,progress,filenames,dirnames --file-idle-time 0 --max-files 0 --background-colour 000000 --font-size 22 --title "0.18.0 History" -1280x720 -o sam-cli-history.ppm | ffmpeg -y -r 60 -f image2pipe -vcodec ppm -i - -vcodec libx264 -preset medium -pix_fmt yuv420p -crf 1 -threads 0 -bf 0 sam-cli-history.mp4

# xvfb-run --auto-servernum --server-args='-screen 0, 1920x1080x16' \gource aws-sam-cli/ -s .06 -1280x720 --auto-skip-seconds .1 --multi-sampling --stop-at-end --key --highlight-users --hide mouse,progress,filenames,dirnames --file-idle-time 0 --max-files 0 --background-colour 000000 --font-size 22 --title "0.18.0 History" -1280x720 -o sam-cli-history.ppm

# docker build -t ffmpeg_gource_sam_cli . && docker run -it ffmpeg_gource_sam_cli -v oputput_videos:output_videos
# docker run test_gource_sam_cli -v output_data:output_data

# ./youtubeuploader -filename 0.18.0-sam-cli-history.mp4 -metaJSON meta_json.json