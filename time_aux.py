import datetime


def pdtimestamp_to_posix(timestamp_ser):
    return (timestamp_ser.astype('int64')/1e9).astype('int64')


def posix_to_datetime(arr):
    return [datetime.datetime.utcfromtimestamp(i) for i in arr]
    
    
def pdtimestamp_to_datetime(timestamp_ser):
    return posix_to_datetime(pdtimestamp_to_posix(timestamp_ser).values)