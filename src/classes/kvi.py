import numpy as np

class KVI:
    def __init__(self, kvi_names, kvi_aggregators):
        self.kvi_names = kvi_names
        self.kvi_aggregators = kvi_aggregators
        
    def __len__(self):
        return len(self.kvi_names)
    
    def __iter__(self):
        for i in range(len(self.kvi_names)):
            yield self.kvi_names[i], self.kvi_aggregators[i]
        
    @property
    def kvi_aggregators(self):
        return self._kvi_aggregators

    @kvi_aggregators.setter
    def kvi_aggregators(self, kvi_aggregators):
        if len(kvi_aggregators) != len(self.kvi_names):
            raise ValueError(
                "The number of kvi aggregators must be the same as the number of kvis"
            )

        self._kvi_aggregators = kvi_aggregators