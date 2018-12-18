class Claim:
    def __init__(self, claim):
        [claim_id, rest] = claim.split('@')
        [point, size] = rest.split(':')

        self.claim_id = claim_id.replace('#', '').strip()
        self.set_point(point)
        self.set_size(size)

    def set_point(self, point):
        [x, y] = point.split(',')
        self.x = int(x.strip())
        self.y = int(y.strip())

    def set_size(self, size):
        [w, h] = size.split('x')
        self.w = int(w.strip())
        self.h = int(h.strip())

    def fill_claim(self, claims):
        for x in range(self.x, self.w + self.x):
            for y in range(self.y, self.h + self.y):
                claims[x][y] += 1
        return claims

    def claim_is_alone(self, claims):
        for x in range(self.x, self.w + self.x):
            for y in range(self.y, self.h + self.y):
                if claims[x][y] > 1:
                    return False
        return True
