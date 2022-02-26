import json,sys,os,shlex
COMMANDS = {}
def command(cmd):
    def decorator(func):
        COMMANDS[cmd] = func
        return func
    return decorator
def filter_messages():
    while True:
        msg = json.loads(input())

        if 'text' in msg:
            text = msg['text']
            if text[0] =='/':
                try:
                    lex = shlex.split(text)
                    if lex[0][0] == '/':
                        command_name = lex[0][1:]
                        if command_name in COMMANDS:
                            COMMANDS[command_name](msg,*lex[1:])
                except Exception as e:
                    pass
        print(json.dumps(msg))
