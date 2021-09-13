# Commands to run ffmpeg in the terminal.

# -vf "crop=trunc(iw/2)*2:trunc(ih/2)*2"
# -vf pad="width=ceil(iw/2)*2:height=ceil(ih/2)*2"
# ffmpeg -i in.mp4 -filter:v "crop=out_w:out_h:x:y" out.mp4
# -c copy

# draw a box on the video
ffmpeg -y -i media/Bog-AV-noise-m18dB-SNR-2-247.mov \
    -vf "drawbox=80:y=100:w=140:h=100:color=black:t=fill"  \
    lectures/assets/mov/Bog-AV-noise-m18dB-SNR-mask.mp4

ffmpeg -y -i media/Dog-AV-noise-m18dB-SNR-2-244.mov \
    -vf "drawbox=90:y=120:w=140:h=100:color=black:t=fill"  \
    lectures/assets/mov/Dog-AV-noise-m18dB-SNR-mask.mp4

ffmpeg -i media/bjtMcGurk-2-251.mov \
    -c:v libx264 -c:a aac -vf format=yuv420p \
    -movflags +faststart  \
    lectures/assets/mov/bjtMcGurk-2-251.mp4

# .mov to .mp4 re-encoding
ffmpeg -i media/k-k-k-ken-small-cropped-237.mov \
    -vf crop="trunc(iw/2)*2:trunc(ih/2)*2" \
    -movflags +faststart  \
    lectures/assets/mov/k-k-k-ken-small-cropped-237.mp4

ffmpeg -i media/t-t-t-ken-small-cropped-234.mov \
    -vf crop="trunc(iw/2)*2:trunc(ih/2)*2" \
    -movflags +faststart  \
    lectures/assets/mov/t-t-t-ken-small-cropped-234.mp4

ffmpeg -y -i media/Bog-AV-noise-m18dB-SNR-2-247.mov \
    -movflags +faststart  \
    lectures/assets/mov/Bog-AV-noise-m18dB-SNR.mp4

ffmpeg -y -i media/Dog-AV-noise-m18dB-SNR-2-244.mov \
    -movflags +faststart  \
    lectures/assets/mov/Dog-AV-noise-m18dB-SNR.mp4

ffmpeg -i media/bagada.mov \
    -filter:v "crop=340:420:220:60" \
    -movflags +faststart  \
    -c:a copy \
    lectures/assets/mov/bagada.mp4
