'''
Simple progress counter functionality for pandas.DataFrame.groupby.apply
'''


class _IterCounter(object):
    def __init__(self, max_iter, start_count=1):
        self.count = start_count
        self.max_iter = max_iter
    def count_iter(self):
        out = self.count
        self.count += 1
        return out

    
def _addcounter(applyfn):
    def _applyfn(df, counter, *args, **kwargs):
        print('\r%i / %i' % (counter.count_iter(), counter.max_iter), end='', flush=True)
        return applyfn(df, *args, **kwargs)
    return _applyfn

    
def applycount(groupby_obj, applyfn, *args, **kwargs):
    counter = _IterCounter(len(groupby_obj)+1)
    applyfn = _addcounter(applyfn)
    res = groupby_obj.apply(applyfn, counter, *args, **kwargs)
    print()
    return res