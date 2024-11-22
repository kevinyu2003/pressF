import wave

def check_riff_header(file_path):
    with wave.open(file_path, 'rb') as wave_file:
        riff_header = wave_file.readframes(4)
        if riff_header != b'RIFF':
            raise Error('file does not start with RIFF id')
        # Continue processing the WAV file
        
check_riff_header("sound/pipe.mp3")