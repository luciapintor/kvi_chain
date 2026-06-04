class KeyIndicatorList:
    def __init__(self, names, aggregators):
        self.names = names
        self.aggregators = aggregators

    def __len__(self):
        return len(self.names)

    def __iter__(self):
        for i in range(len(self.names)):
            yield self.names[i], self.aggregators[i]

    @property
    def aggregators(self):
        return self._aggregators

    @aggregators.setter
    def aggregators(self, aggregators):
        if len(aggregators) != len(self.names):
            raise ValueError(
                "The number of aggregators must be the same as the number of indicators"
            )
        self._aggregators = aggregators