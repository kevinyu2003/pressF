import sounddevice as sd
import soundfile as sf
import keyboard

# 创建一个字典，将按键映射到音频文件路径
audio_files = {
    'f': 'sound/pipe.wav',
    # ... 添加更多按键映射
}

# 加载所有音频文件到字典中
audio_data = {}
for key, file_path in audio_files.items():
    try:
        data, fs = sf.read(file_path)
        audio_data[key] = (data, fs)
    except Exception as e:
        print(f"加载音频文件 {file_path} 失败: {e}")

def play_audio(key, volume=0.5):
    if key not in audio_data:
        print(f"未找到与按键 {key} 对应的音频文件")
        return
    data, fs = audio_data[key]
    sd.play(data * volume, fs, blocking=False)

def on_press(key):
    
    try:
        k = key.char  # normal keys
    except AttributeError:
        k = key.name  # special keys (e.g., function keys)
    play_audio(k)

# 开始监听键盘
keyboard.on_press(on_press)
keyboard.wait()
