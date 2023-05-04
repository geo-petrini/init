# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
def index():
    applications = []   

    import glob
    import os
    import random

    css_classes = ['one', 'two', 'three', 'four']
    exclude = ['examples', 'welcome', 'admin', '__pycache__', 'init']

    l = glob.glob('applications/*', recursive=False)
    l.sort()
    for f in l:
        if os.path.isdir(f) and os.path.basename(f) not in exclude:
            foldername = os.path.basename(f)
            applications.append( (foldername, URL(foldername, 'default', 'index'), random.choice(css_classes) ) )

    more_applications = []
    more_applications.append( ('Examples', URL('examples', 'default', 'index'), 'four') )
    more_applications.append( ('Welcome', URL('welcome', 'default', 'index'), 'three') )
    more_applications.append( ('Admin', URL('admin', 'default', 'index'), 'three') )
    return dict(applications=applications, more_applications=more_applications)

