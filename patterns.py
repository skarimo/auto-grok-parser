#for now the order here matters. We want to match from most specific to least
pattern_list = {
    'number': '^\d*\.?\d*$',
    'integer': '^\d+$',
    'word': '([^\s]+)',
    'data': '(.*)',
}
