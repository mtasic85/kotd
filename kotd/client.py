
class KotdClient(object):
    def __init__(self, addresses=()):
        self.addresses = addresses

    def tuple(self, *items):
        pass

    def list(self, *items):
        pass

    def dict(self, *items):
        pass

    def odict(self, *items):
        pass

    def set(self, *items):
        pass

    def oset(self, *items):
        pass

if __name__ == '__name__':
    c = KotdClient(['http://localhost:4076'])
    d = c.dict((k, k) for k in range(10))


