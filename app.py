import click
import os
import re
from parser import Parser

def main_app():
    global parser_class
    global raw_log_display

    click.clear()
    click.secho('WELCOME', blink=True, bold=True)

    raw_log = click.prompt('Please enter a raw log line', type=str)
    raw_log_display = raw_log
    parser_class = Parser(raw_log)

    click.clear()

    while True:
        print_raw_log_and_current_rule()
        attribute_input = click.prompt('Copy paste the first/next attribute value', type=str)
        if attribute_input.lower() == 'end':
            break
        else:
            attribute_name = click.prompt('Name the attribute: ' + attribute_input, type=str)
            # raw_log_display = re.sub(attribute_input,'',raw_log_display,count=1)
            raw_log_display = raw_log_display.replace(attribute_input, '', 1)
            parser_class.match_string(attribute_name, attribute_input)
            click.clear()

        print_raw_log_and_current_rule()
        divider_input = click.prompt('Copy paste the divider | type [n] if no divider', type=str)
        if divider_input.lower() == 'end':
            break
        elif divider_input.lower() == 'n':
            pass
        else:
            raw_log_display = raw_log_display.replace(divider_input, '', 1)
            parser_class.append_divider(divider_input)
            click.clear()
            
    click.clear()
    click.echo('Created rule:')
    click.secho('new_rule ' + ''.join(parser_class.grok_parser), bg='red', fg='white')

def print_raw_log_and_current_rule():
    global parser_class
    global raw_log_display
    click.secho('new_rule ' + ''.join(parser_class.grok_parser), bg='red', fg='white')
    click.echo('')
    click.echo('Raw Log:')
    click.secho(raw_log_display, bg='blue', fg='white')
    click.secho('TYPE "end" if finished', bg='white', fg='black')


    pass

if __name__ == '__main__':
    main_app()
