import pyaudio
import wave
import keyboard
import sounddevice as sd
import soundfile as sf
data, fs = sf.read('sound/pipe_01.wav')
def play_mp3(file_path, volume=0.05):
    sd.play(data * volume, fs, blocking=False)
#创建按键与 MP3 文件的映射
key_to_mp3 = {
    'f': 'sound/pipe.wav'
    # ... 添加更多按键映射
}

def on_press(key):
    try:
        k = key.char  # normal keys
    except AttributeError:
        k = key.name  # special keys (e.g., function keys)

    if k in key_to_mp3:
        play_mp3(key_to_mp3[k])

# 开始监听键盘
keyboard.on_press(on_press)
keyboard.wait()
