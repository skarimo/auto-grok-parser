import click
import os
from parser import Parser

def main_app():
    global raw_log
    global raw_log_display
    global parser_class

    raw_log = click.prompt('Please enter a raw log line', type=str)
    raw_log_display = raw_log
    #initiate the parser with the raw log sample.
    parser_class = Parser(raw_log)

    main_parser_loop()

    print("Current Rule:", parser_class.grok_parser)

def main_parser_loop():
    global raw_log
    global raw_log_display
    global parser_class

    while True:
        print("Current Raw Log:", raw_log_display)
        print("Current Rule:", parser_class.grok_parser)

        end_index = click.prompt('Select the index of last character or type "end" to finish', type=int, default=-1)
        if end_index == "end":
            break
        elif end_index == -1:
            value_selected = raw_log_display[0:len(raw_log_display)]
            parser_class.match_string(value_selected)
            break

        value_selected = raw_log_display[0:end_index+1]
        parser_class.match_string(value_selected)
        raw_log_display = raw_log_slicer(raw_log_display, end_index+1)
        os.system('clear')

        print("Current Raw Log:", raw_log_display)
        print("Current Rule:", parser_class.grok_parser)


        divider_index = click.prompt('is next character divider [y=yes, n]? Type "end" to finish',)
        if divider_index == "end":
            break
        elif divider_index.lower() == 'y':
            parser_class.append_divider(raw_log_display[0])
            raw_log_display = raw_log_slicer(raw_log_display, 1)
        os.system('clear')



def raw_log_slicer(raw_log_display, end):
    return raw_log_display[:0] + raw_log_display[end:]




if __name__ == '__main__':
    os.system('clear')
    main_app()
