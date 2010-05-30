#!/usr/bin/env python

from config import baseurl, opener
import hudsonbranches

from pprint import pprint

infos = hudsonbranches.get_all(baseurl, opener=opener.open)
pprint(infos)
