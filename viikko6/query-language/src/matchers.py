class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True
        return False

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team

class Compare:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

class HasAtLeast(Compare):
    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class All:
    def __init__(self):
        pass

    def test(self, player):
        return True

class Not:
    def __init__(self, matcher):
        self._matcher = matcher

    def test(self, player):
        return not self._matcher.test(player)

class HasFewerThan(Compare):
    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value


class QueryBuilder:
    def __init__(self, matcher = All()):
        self._matcher = matcher

    def plays_in(self, team):
        return self._with(PlaysIn(team))

    def has_at_least(self, value, attr):
        return self._with(HasAtLeast(value, attr))

    def all(self):
        return self._with(All())

    def has_fewer_than(self, value, attr):
        return self._with(HasFewerThan(value, attr))

    def one_of(self, *builders):
        matchers = [builder.build() for builder in builders]
        return self._with(Or(*matchers))

    def _with(self, matcher):
        return QueryBuilder(And(self._matcher, matcher))

    def build(self):
        return self._matcher

    pass