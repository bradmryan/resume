try:
    from resume.dev import *
    live = False
except:
    live = True

if live:
    from resume.prod import *
