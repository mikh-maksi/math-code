from pyinference.fuzzy import set as fuzzy_set
a = Variable(name='A', terms=['low', 'high'])
fs = fuzzy_set.Partition(peaks=[0.0, 0.5, 1.0])
b = Variable(name='B', terms=fs)