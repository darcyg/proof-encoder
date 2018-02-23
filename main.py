import ffmpy
import subprocess

# must be noted that these use -i ffmpeg command which defines the ffmpeg pipe protocol this can be done using ffmpy.
# It also has filtering commands which have to be managed in a different way.
ffmbcarc14x9_sd =  {"validFor": "640x480|480x360|720x540|960x720","ffmbc": "-threads 4 -i %INPUT% -r 25 -ar 48000 -vf scale=0:0:interl=1,crop=iw:ih-ih*0.125:0:iw*.0625,scale=616:576:interl=1,pad=720:576:52:0:black -vcodec libx264 -cqp 18 -profile high -preset fast -tff -flags +loop+ildct+ilme -acodec mp2 -ab 192k -aspect 16:9 -f mpegts -y -ac 2 %OUTPUT%"}
ffmbcaudio2jfe_sd = {"validFor": "0x0","ffmbc": "-threads 4 -f image2 -loop 1 -shortest -i %SLATEFILE% -i %INPUT% -r 25 -ar 48000 -vf scale=702:576:interl=1,pad=720:576:8:0:black -vcodec libx264 -cqp 18 -profile high -preset fast -tff -flags +loop+ildct+ilme -acodec mp2 -ab 192k -aspect 16:9 -f mpegts -y -ac 2 %OUTPUT%"}
ffmbcnoarc_hd = {"validFor": "1440x1080|1280x720|1200x676|1216x688|1920x1080","ffmbc": "-threads 4 -i %INPUT% -r 25 -ar 48000 -vf scale=1440:1080:interl=1 -vcodec libx264 -cqp 18 -profile high -preset fast -tff -flags +loop+ildct+ilme -acodec mp2 -ab 192k -aspect 16:9 -f mpegts -y -ac 2 %OUTPUT%"}
ffmbcnoarc_sd = {"validFor": "480x272|480x270|400x222|576x320|568x320|640x360|640x368|640x352|848x480|960x540|1024x576|720x576|720x406|720x404|960x544","ffmbc": "-threads 4 -i %INPUT% -r 25 -ar 48000 -vf scale=702:576:interl=1,pad=720:576:8:0:black -vcodec libx264 -cqp 18 -profile high -preset fast -tff -flags +loop+ildct+ilme -acodec mp2 -ab 192k -aspect 16:9 -f mpegts -y -ac 2 %OUTPUT%"}
#getting unrecognised uption -cqp, -tff

ffmbcnoarc_hd_copy = {"validFor": "1440x1080|1280x720|1200x676|1216x688|1920x1080","ffmbc": '-threads 4 -r 25 -ar 48000 -vf "scale=1440:1080:interl=1" -vcodec libx264  -profile high -preset fast -flags +loop+ildct+ilme -acodec mp2 -ab 192k -aspect 16:9 -f mpegts -y -ac 2'}

# mp4 encoding only seems to work if i move the flags with this account
#  ffmpeg -i input.mp4 -c copy -movflags +faststart output.mp4. This moves MOOV Atom to the beginning of the file.
# This only matters when piping in the video setting the video directly as the input works fine. =)
ff = ffmpy.FFmpeg(
    inputs={'test_video.mp4': None},
    outputs={'pipe:1':  ffmbcnoarc_hd_copy.get('ffmbc')}
)

print(ff.cmd)
stdout, stderr = ff.run(stdout=subprocess.PIPE)

# This could easily output to a S3 bucket but for now let it be a file.
file = open('output/output.ts', 'wb')
file.write(stdout)

# ff.run()