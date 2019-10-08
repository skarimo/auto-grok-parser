import click
from .parser import Parser

def main():
    #initiate a global variable
    global parser_class

    click.clear()
    click.secho('WELCOME TO CLI GROK PARSING HELPER', blink=True, bold=True)

    raw_log = click.prompt('Please enter a raw log line', type=str)
    parser_class = Parser(raw_log)

    #launch the main loop which handles attribute/divider prompts
    main_prompt_loop()

    #final message before the application exits
    end_message()

def main_prompt_loop():
    global parser_class

    while len(parser_class.raw_log_display) != 0:
        click.clear()
        print_raw_log_and_current_rule()
        attribute_input = click.prompt('Copy paste the first/next attribute value', type=str)
        if attribute_input.lower() == 'end':
            break
        else:
            attribute_name = click.prompt('Name the attribute: ' + attribute_input, type=str)
            parser_class.handle_attribute(attribute_name, attribute_input)
            click.clear()

        if len(parser_class.raw_log_display) == 0:
            break

        print_raw_log_and_current_rule()
        divider_input = click.prompt('Copy paste the divider | type [n] if no divider', type=str)
        if divider_input.lower() == 'end':
            break
        elif divider_input.lower() == 'n':
            pass
        else:
            parser_class.handle_divider(divider_input)
            click.clear()

def print_raw_log_and_current_rule():
    global parser_class

    click.secho('new_rule ' + ''.join(parser_class.grok_parser), bg='red', fg='white')
    click.echo('\n')
    print_raw_log()

def end_message():
    global parser_class

    click.clear()
    click.echo('Raw log:')
    click.secho(parser_class.raw_log, bg='blue', fg='white')
    click.echo('Created rule:')
    click.secho('new_rule ' + ''.join(parser_class.grok_parser), bg='red', fg='white', bold=True)
    click.secho("Feel free to give some feedback - Sherzod", bg='yellow', fg='black')

def print_raw_log():
    click.echo('Raw log:')
    click.secho(parser_class.raw_log_display, bg='blue', fg='white')

if __name__ == '__main__':
    main()
