from picamera2.encoders import H264Encoder, Quality
from picamera2 import Picamera2
import pyaudio
import numpy as np
import wave
import threading
import time

RECORD_SECONDS = 30
VIDEO_FILENAME = 'video.h264'
AUDIO_FILENAME = 'audio.wav'

def record_video():
    picam2 = Picamera2()
    picam2.configure(picam2.create_video_configuration())
    encoder = H264Encoder()

    picam2.start_recording(encoder, VIDEO_FILENAME, quality=Quality.HIGH)

    time.sleep(RECORD_SECONDS)

    # FIXME: Need to convert from h264 to mp4: ffmpeg -i test.h264 -c copy test.mp4
    picam2.stop_recording()

# NOTE: Mono = one channel
def record_audio():
    RESPEAKER_RATE = 16000
    RESPEAKER_CHANNELS = 2
    RESPEAKER_WIDTH = 2
    # run getDeviceInfo.py to get index
    RESPEAKER_INDEX = 1  # refer to input device id
    CHUNK = 1024
    WAVE_OUTPUT_FILENAME = AUDIO_FILENAME

    p = pyaudio.PyAudio()

    stream = p.open(
                rate=RESPEAKER_RATE,
                format=p.get_format_from_width(RESPEAKER_WIDTH),
                channels=RESPEAKER_CHANNELS,
                input=True,
                input_device_index=RESPEAKER_INDEX,)

    print("* recording")

    frames = []

    for i in range(0, int(RESPEAKER_RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        # extract channel 0 data from 2 channels, if you want to extract channel 1, please change to [1::2]
        a = np.frombuffer(data,dtype=np.int16)[0::2]
        frames.append(a.tobytes())

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(p.get_format_from_width(RESPEAKER_WIDTH)))
    wf.setframerate(RESPEAKER_RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

if __name__ == '__main__':
    video_thread = threading.Thread(target=record_video)
    audio_thread = threading.Thread(target=record_audio)

    video_thread.start()
    audio_thread.start()

    video_thread.join()
    audio_thread.join()
