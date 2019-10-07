#for now the order here matters. We want to match from most specific to least
pattern_list = {
    'ip': '^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$',
    'integer': '^\d+$',
    'number': '^\d*\.?\d*$',
    'word': '^[a-zA-Z0-9_]+$',
    'data': '(.*)',
}
