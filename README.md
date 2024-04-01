# silence_remover
## References
- https://onkar-patil.medium.com/how-to-remove-silence-from-an-audio-using-python-50fd2c00557d
- https://github.com/respeaker/mic_hat/tree/master
- https://people.csail.mit.edu/hubert/pyaudio/
- https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf
- https://github.com/timsainb/noisereduce/tree/master

## Development environment
- Raspberry Pi CM4
- Raspberry Pi OS - Bullseye
- IMX219
- [ReSpeaker 2-Mics Pi HAT](https://wiki.seeedstudio.com/ReSpeaker_2_Mics_Pi_HAT/)
- [boot/config.txt](https://github.com/atsss/RPi_configs/blob/main/bullseye/imx219_ReSpeaker.txt)

## How to use
- Jupyter Lab
```
docker container run -it -p 10000:8888  -v .:/home/jovyan/work [container_name]:[tag]
```
