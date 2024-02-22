import os
from pyAudioAnalysis import audioBasicIO as aIO
from pyAudioAnalysis import audioSegmentation as aS
from pydub import AudioSegment
import json

AUDIO_FILENAME = 'audio.wav'
MIN_LENGTH, MIN_INTERVAL = 3, 3
START, END = 0, 1

def get_segments():
    [Fs, x] = aIO.read_audio_file(AUDIO_FILENAME)
    segments = aS.silence_removal(x, Fs, 0.020, 0.020, smooth_window=1.0, weight=0.3, plot=True)
    return segments

def slice_silence(segments):
    MILSEC = 1000
    myaudio = AudioSegment.from_wav(AUDIO_FILENAME)

    for index, segment in enumerate(segments):
        extract = myaudio[segment[START]*MILSEC:segment[END]*MILSEC]
        extract.export(f'active-{index}.wav', format="wav")

def create_audio_metadata_json(segments):
    metadata = [{ 'start_sec': segment[0], 'end_sec': segment[1] } for segment in combined_segments]
    json_object = json.dumps(metadata, indent=4)

    with open("audio_metadata.json", "w") as outfile:
        outfile.write(json_object)

def remove_too_small_windows(segments):
    modified_segments = [segment for segment in segments if segment[END] - segment[START] > MIN_LENGTH]
    combined_segments = [modified_segments[0][:]]
    index = 1
    while index < len(modified_segments):
        if modified_segments[index][START]-combined_segments[-1][END] > MIN_INTERVAL:
            combined_segments.append(modified_segments[index])
        else:
            combined_segments[-1][END] = modified_segments[index][END]
        index += 1

    return combined_segments

if __name__ == '__main__':
    segments = get_segments()
    segments = remove_too_small_windows(segments)
    slice_silence(segments)
    create_audio_metadata_json(segments)
