from flask import Markup

def linkerise(string):
    return Markup(f'<p><a href="{string}">{string}</a></p>')

def linkerise_or_abbreviate(string):
    strpos = string.find('\n')

    # link with no newline characters
    if (string.startswith('http')) and (strpos == -1):
        return linkerise(string)

    # up to 100 characters or first newline, whichever is earliest
    return Markup(f'<pre>{string[0:min(strpos, 100)]}</pre>')
