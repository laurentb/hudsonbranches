# hudsonbranches

A small Python library/tool to get what branches failed to build in Hudson.
Tested with git jobs, but should work with any SCM plugin.

It only works by looking at all the builds; if there is no build of a branch it will not show up. It handles builds that concerns two branches or more (this happens in git when branch trees are identical).

You can use the hudsonbranches library directly or one of the samples (though you will probably want to hack on it).


## Requirements

* Python 2.5 and simplejson or Python 2.6
The Python API of Hudson is not used as it is the same as the JSON one minus the security.

* Mako templates for the `sample_html` script.
