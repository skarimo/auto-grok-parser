from patterns import pattern_list
import re

class Parser:
    def __init__(self, raw_log = None):
        self.pattern_list = pattern_list
        self.raw_log = raw_log
        self.grok_parser = []

    def build_rule(self, pattern, attribute_name):
        # rule = "%{"+ "%s:%s" % (pattern, pattern) + "}"
        # rule = '%{{{0}:{1}}}'.format(pattern, pattern)
        rule = '%{' + pattern + ':' + attribute_name + '}'
        self.grok_parser.append(rule)

    def match_string(self, attribute_name, attribute_input):
        for pattern in pattern_list:
            match = re.match(pattern_list[pattern], attribute_input)
            if (match != None) and (match.group() == attribute_input):
                self.build_rule(pattern, attribute_name)
                break

    def append_divider(self, divider):
        self.grok_parser.append(divider)
