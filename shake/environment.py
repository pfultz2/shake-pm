import yaml, os, glob2
from shake.repository import Repository

class Environment:
    def __init__(self):
        self.path = ''
        self.channels = []
        self.toolchains = {}
        self.repo = Repository()

    def load_channels(self):
        for c in self.channels:
            g = os.path.join(c, '**/*.yml')
            files = glob2.glob(g)
            for f in files:
                self.repo.load_package(f)

def load_env(d):
    f = os.path.join(d, 'environment.yml')
    data = yaml.load(open(f))
    e = Environment()
    e.path = d
    e.channels = list(data['channels'])
    # e.toolchains = dict(data.toolchains)
    return e


