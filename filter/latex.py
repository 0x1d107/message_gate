from msg_filter import command
from urllib.parse import quote


@command('latex')
def latex(msg,*args):
    txt = quote('\dpi{200} '+msg['text'][len('/latex '):])
    msg["image"] = f"https://latex.codecogs.com/png.image?{txt}"
    msg["from"] += '|LaTeX@filter'
    msg["protocol"] = 'filter'

