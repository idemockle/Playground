import json
import sys
import argparse


def ipynb_json_to_py(json_obj):
    return '\n\n'.join([''.join(i['source']) for i in json_obj['cells']])
    
if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('ipynb_in')
    p.add_argument('py_out')
    
    if len(sys.argv) == 1:
        p.print_help()
    else:
        args = p.parse_args()
        with open(args.ipynb_in, 'r') as f_in, open(args.py_out, 'w') as f_out:
            f_out.write(ipynb_json_to_py(json.load(f_in)))