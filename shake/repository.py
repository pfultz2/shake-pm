from shake.package import load_package

class Repository:
    def __init__(self):
        self.packages = {}
        self.installed = []
        self.package_lookup = {}

    def load_package(self, f):
        p = load_package(f)
        self.packages[p.path] = p
        if p.name in self.package_lookup: self.package_lookup[p.name].append(p.path)
        else: self.package_lookup[p.name] = [p.path]

    def list(self):
        return [key for key, value in self.package_lookup]
        