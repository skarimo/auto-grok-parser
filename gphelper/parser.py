from .patterns import pattern_list
import re

class Parser:
    def __init__(self, raw_log = None):
        self.pattern_list = pattern_list
        self.raw_log = raw_log
        self.raw_log_display = raw_log
        self.grok_parser = []

    def build_rule(self, pattern, attribute_name):
        # rule = "%{"+ "%s:%s" % (pattern, attribute_name) + "}"
        # rule = '%{' + pattern + ':' + attribute_name + '}'
        rule = '%{{{0}:{1}}}'.format(pattern, attribute_name)
        self.grok_parser.append(rule)

    def find_pattern(self, attribute_name, attribute_input):
        for pattern in pattern_list:
            match = re.match(pattern_list[pattern], attribute_input)
            if (match != None) and len(match.group()) > 1 and (match.group() == attribute_input) and (self.raw_log_display.startswith(attribute_input)):
                self.build_rule(pattern, attribute_name)
                if pattern == 'notSpace':
                    attribute_input = attribute_input[:-1]
                self.raw_log_display = self.raw_log_display.replace(attribute_input, '', 1)
                break

    def handle_attribute(self, attribute_name, attribute_input):
        self.find_pattern(attribute_name, attribute_input)

    def handle_divider(self, divider_input):
        escaped_divider = (re.sub(r'([&*()":{}?|\[\]<>])', r'\\\1', divider_input)).replace('\\\\', '\\')
        # escaped_divider = re.escape(divider_input)
        self.grok_parser.append(escaped_divider)
        self.raw_log_display = self.raw_log_display.replace(divider_input, '', 1)
