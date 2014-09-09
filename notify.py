import config

class Services (object):
    def __getitem__(self, name):
        import importlib
        template = "notify_{}"
        module_name = template.format(name)
        return importlib.import_module(module_name)

    def __getattr__(self, name):
        return self[name]

services = Services()

if __name__ == '__main__':
    print config.lookup("smtp.server")
