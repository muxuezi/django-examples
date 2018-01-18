import ffmpy


ff = ffmpy.FFmpeg(
    global_options=['-y'],
    inputs={'example.mp4': None},
    outputs={'out.png': ['-ss', '00:00:05', '-vframes', '1']}
)
ff.run()
