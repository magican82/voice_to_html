def print_header(mediapath):
    header ='<!DOCTYPE html>'\
    '<html>'\
    '<head>\n'\
    '<style>\n'\
    'th, td {\n'\
    '  border-style:dotted;\n'\
    '  border-color: #96D4D4;\n'\
    '  text-align: left;\n'\
    '  font-weight: normal;\n'\
    '  font-size: medium;\n'\
    '  font-style: normal;\n'\
    '}\n'\
    '</style>\n'\
    '</head>\n'\
    '<body>\n'\
    '<br />\n'\
    '<audio id="player" src="'+mediapath+'"></audio>\n'\
    '<br />\n'\
    '<div>\n'\
    '    <button onclick="document.getElementById(\'player\').volume+=0.1">vol +</button>\n'\
    '    <button onclick="document.getElementById(\'player\').volume-=0.1">vol -</button>\n'\
    '</div>\n'\
    '<table>\n'
    #print(header) 
    return header

def print_footer():
    footer = '</table>footer\n'\
    '</body>\n'\
    '</html>'

    #print(footer) 
    return footer
#print_header("C:\python\voicercognition\wav\converted\2024013401_84959260954.wav")
print_footer()
