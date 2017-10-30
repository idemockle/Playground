import lz4framed, lzma, io, multiprocessing, time, os, tempfile
import pyarrow.feather as feather

def compress(file_in, file_out):
    with open(file_in, 'rb') as f1, lzma.open(file_out, 'wb', preset=9) as f2:
        read_size = lz4framed.get_block_size()
        with lz4framed.Compressor(f2) as compressor:
            try:
                while True:
                    compressor.update(f1.read(read_size))
            # empty read result supplied to update()
            except lz4framed.Lz4FramedNoDataError:
                pass
            # input stream exception
            except EOFError:
                pass
                
                
def read_featherlz4(pathstr):
    outfilename=os.path.join(tempfile.gettempdir(), '{}'.format(time.time()))
    with open(pathstr, 'rb') as file_in, open(outfilename, 'wb') as file_out:
        for chunk in lz4framed.Decompressor(file_in):
            file_out.write(chunk)
    df = feather.read_feather(outfilename, nthreads=multiprocessing.cpu_count())
    os.remove(outfilename)
    return df