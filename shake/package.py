import yaml

class Package:
    def __init__(self):
        self.path = ''
        self.name = ''
        self.version = ''
        self.url = ''
        self.sha1 = ''
        self.depends = []
        self.builders = []

def load_package(f):
    data = yaml.load(open(f))
    p = Package()
    p.name = data['name']
    p.version = data['version']
    p.url = data['url']
    p.sha1 = data['sha1']
    p.depends = list(data['depends'])
    # for name, builder in data['build']:

    return p