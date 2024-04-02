import whisper
from pyannote.audio import Pipeline
from combine import diarize_text
from pydub import AudioSegment
import os
import torch

#sound = AudioSegment.from_mp3("test_sber.mp3")
#sound.export("audio.wav", format="wav")

def recogonize_speach(f,path,dest_path):
    pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization")


    pipeline.to(torch.device("cuda")) #Enable it to increase speed with cuda GPU

    # run the pipeline on an audio file
    diarization = pipeline(path)



    model = whisper.load_model('medium')
    asr_result = model.transcribe(path)

    final_result = diarize_text(asr_result, diarization)

    html_file_name = os.path.abspath(os.curdir)+'\\html\\' + os.path.splitext(os.path.basename(f))[0]+'.html'
    f_html = open(html_file_name,'w')
    from header import print_header,print_footer
    line = print_header(dest_path)
    print(line)
    f_html.write(line)
    f_html.write("\n")
    
    for seg, spk, sent in final_result:
        line =f'<tr><th>{seg.start:.2f}</th><th2.00</th><th>{spk}<button onclick="audio=document.getElementById(\'player\'); audio.currentTime={seg.start:.2f}; document.getElementById(\'player\').play()">...</button> </th><th>{sent}</th>'
        #f'{seg.start:.2f} {seg.end:.2f} {spk} {sent}'
        print(line)
        f_html.write(line)
        f_html.write("\n")

    line = print_footer()    
    print(line)
    f_html.write(line)
    f_html.write("\n")
    f_html.close()


def print_HTML(filename):
     f = open (filename, 'rb')
     linex=''
     for str_ in f:
         str_utf=str_.decode('utf8')
         print(str_utf)
         filename=linex+str_utf
     return linex

for f in os.scandir('wav'):
    if f.is_file() and f.path.split('.')[-1].lower() == 'wav':
        with open(f.path, 'r') as csvfile:
            destination = os.path.abspath(os.curdir)+'\\wav\\converted\\'+os.path.basename(f.path)
            recogonize_speach(f,f.path,destination)
            
            
        os.rename(f.path, destination)


 




    
    




