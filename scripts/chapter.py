import markdown, sys


md = markdown.Markdown()
text = open(sys.argv[1]).read().decode("utf-8")

output = md.convert(text)

print """<!DOCTYPE html>
<html>
<title></title>
<meta charset="utf-8" />
<link rel="stylesheet" type="text/css" href="styles.css" />
</head>
<body>"""

print output.encode("utf-8")

print """</body>
</html>"""
