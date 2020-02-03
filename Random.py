class Random:
    def __init__(self, seed):
        self.seed = seed

    def next(self):
        self.seed = (7**5*self.seed)%(2**31-1)
        return self.seed

    def choose(self, limit):
        newInt =  self.next() % (limit)
        return newInt


class Rule:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.count = 1

    def __repr__(self):
        myStr = ''
        myStr = str(self.count) + self.left

        for i in self.right:
            myStr += i

        return myStr


class Grammar:
    def __init__(self, seed):
        self.seed = Random(seed)
        self.dict = {}

    def rule(self, left, right):
        if left in self.dict:
            self.dict[left] += (Rule(left, right,),)
        else:
            self.dict[left] = (Rule(left, right,),)

    def generate(self):
        if 'Start' in self.dict:
            return self.generating(('Start',))
        else:
            raise RuntimeError

    def generating(self, strings):
        result = ''

        for i in strings:
            if i not in self.dict:
                result += i + ' '
            else:
                x = self.select(i)
                result += self.generating(x)
        return result

    def select(self, left):
        rules = self.dict[left]
        total = 0

        for i in rules:
            total += i.count

        index = self.seed.choose(total)


        for i in rules:
            index -= i.count
            if(index <= 0):
                chosen = i
                break

        for i in rules:
            if i != chosen:
                i.count = i.count + 1

        return chosen.right
