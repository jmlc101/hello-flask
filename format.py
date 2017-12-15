markup = """
<!doctype html>
<html>
    <head>
        <title>{0}</title>
    </head>
    <body>
        <h1>{1}</h1>
    </body>
</html>
"""

markup = markup.format('My Page Title', 'Page Heading')
print(markup)

markup2 = """
<!doctype html>
<html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        <h1>{heading}</h1>
    </body>
</html>
"""

markup2 = markup2.format(title='My Page Title', heading='Page Heading')
print(markup2)