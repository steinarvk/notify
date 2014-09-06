import os.path
import yaml

DefaultConfigFilenames = ".notify.yaml", "notify.yaml"
DefaultConfigPaths = ".", "~"

def lookup_composite_key(composite_key, cfg):
    if isinstance(composite_key, (str,unicode)):
        keys = composite_key.split(".")
    else:
        keys = composite_key
    rv = cfg
    for key in keys:
        rv = rv[key]
    return rv

def read_config(filename):
    import yaml
    with open(filename, "r") as f:
        return yaml.load(f.read())

def construct_filenames(filenames, paths):
    filenames = list(filenames)
    for path in paths:
        path = os.path.expanduser(path)
        for filename in filenames:
            yield os.path.join(path, filename)

def construct_default_filenames():
    return construct_filenames(DefaultConfigFilenames, DefaultConfigPaths)

def search_config(ckey, filenames):
    for filename in filenames:
        try:
            cfg = read_config(filename)
        except IOError:
            continue
        try:
            return lookup_composite_key(ckey, cfg)
        except KeyError:
            pass

def lookup(ckey, filenames=None):
    return search_config(ckey, filenames or construct_default_filenames())

