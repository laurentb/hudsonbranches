#!/usr/bin/env python

from config import baseurl, opener
import hudsonbranches
from os.path import dirname

from mako.template import Template

infos = hudsonbranches.get_all(baseurl, opener=opener.open)

path = dirname(__file__)
print Template(filename=path+"/sample_template.html").render(jobs=infos)

