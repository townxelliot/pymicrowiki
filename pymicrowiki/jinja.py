from flask import Markup

def linkerise(string):
    return Markup(f'<p><a href="{string}">{string}</a></p>')

def linkerise_or_show(string, abbrev=True):
    strpos = string.find('\n')

    # link with no newline characters
    if (string.startswith('http')) and (strpos == -1):
        return linkerise(string)

    # up to 100 characters or first newline, whichever is earliest
    string_end = len(string)

    if abbrev:
        if strpos > 0:
            string = string[0:min(strpos-1, string_end, 100)] + '…'

    return Markup(f'<pre>{string}</pre>')
