This repository combines Whisper ASR capabilities with Voice Activity Detection (VAD) and Speaker Embedding to identify the speaker for each sentence in the transcription generated by Whisper and conver it to HTML file

Installation
You need to install 
1. https://github.com/openai/whisper
2. https://github.com/pyannote/pyannote-audio.

usage python convert_html.py 
All *.wav files should be in wav dierectory. After they converded they are automaticly placed шт wav/converted dierectory.
HTML results are generating in HTML directory.