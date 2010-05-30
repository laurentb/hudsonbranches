try:
    import json
except ImportError:
    import simplejson as json

# TODO split functions: get/parse, and all/project

def get_all(baseurl, opener = None):
    """
    Get branch informations for all projects

    baseurl is the root URL of Hudson.

    opener is a function to call to open the URL, by default urllib2.urlopen.
    It can be useful to change it to handle authentication.

    Returns a dictionary.
    """
    if opener is None:
        from urllib2 import urlopen
        opener = urlopen

    # FIXME is Hudson's encoding always this?
    data = json.load(
        opener(baseurl+"/api/json?depth=2"),
        encoding="iso-8859-1"
    )

    infos = []

    for job in data["jobs"]:
        info = {}
        info["name"] = job["name"]
        info["url"] = job["url"]

        results = {}
        for build in job["builds"]:
            result = build["result"]
            if result:
                for action in build["actions"]:
                    if action.has_key("lastBuiltRevision") \
                    and action["lastBuiltRevision"].has_key("branch"):
                        for branch in action["lastBuiltRevision"]["branch"]:
                            if not results.has_key(branch["name"]):
                                results[branch["name"]] = result

        info["branches"] = results

        infos.append(info)

    return infos
