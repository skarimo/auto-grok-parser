from patterns import pattern_list
import re

class Parser:
    def __init__(self, raw_log = None):
        self.pattern_list = pattern_list
        self.raw_log = raw_log
        self.grok_parser = []

    def build_rule(self, pattern, name):
        # rule = "%{"+ "%s:%s" % (pattern, pattern) + "}"
        # rule = '%{{{0}:{1}}}'.format(pattern, pattern)
        rule = '%{' + pattern + ':' + pattern + '}'
        self.grok_parser.append(rule)

    def match_string(self, str):
        for pattern in pattern_list:
            match = re.match(pattern_list[pattern], str)
            if (match != None) and (match.group() == str):
                self.build_rule(pattern, 'this works')
                break

    def append_divider(self, divider):
        self.grok_parser.append(divider)


def main():
    # Set name of Parser object
    parser_class = Parser()
    parser_class.match_string("test")
    parser_class.append_divider(" ")
    parser_class.match_string("test")
    print(''.join(parser_class.grok_parser))

if __name__ == "__main__":
    main()
