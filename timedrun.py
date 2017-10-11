import timeit

def timedrun(f, *args, **kwargs):
    start = timeit.default_timer()
    rs = f(*args, **kwargs)
    end = timeit.default_timer()
    
    print(str(end-start) + ' seconds')
    return rs