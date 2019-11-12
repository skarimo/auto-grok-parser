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
    not_finished_parsing = True

    res = click.prompt('Is the initial value a divider? yN', type=str, default="N")

    if res.lower() =='y':
        divider_prompt()

    while len(parser_class.raw_log_display) != 0 and not_finished_parsing:
        attribute_prompt()
        if len(parser_class.raw_log_display) == 0:
            break
        not_finished_parsing = divider_prompt()

def attribute_prompt():
    while True:
        click.clear()
        print_raw_log_and_current_rule()
        attribute_input = click.prompt('Copy paste the first/next attribute value', type=str)
        if parser_class.raw_log_display.startswith(attribute_input):
            attribute_name = click.prompt('Name the attribute: ' + attribute_input, type=str)
            while attribute_name.isnumeric() == True:
                click.echo('Name cannot be an number')
                attribute_name = click.prompt('Name the attribute: ' + attribute_input, type=str)
            parser_class.handle_attribute(attribute_input, attribute_name)
            break

def divider_prompt():
    while True:
        click.clear()
        print_raw_log_and_current_rule()
        divider_input = click.prompt('Copy paste the divider | type [n] if no divider', type=str)
        if parser_class.raw_log_display.startswith(divider_input):
            parser_class.handle_divider(divider_input)
            click.clear()
            return True
        elif divider_input.lower() == 'end':
            return False
        elif divider_input.lower() == 'n':
            return True

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
