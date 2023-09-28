import hashlib
import os
import argparse

files = []

for file in os.listdir():
    if not file.endswith(".py"):
        if os.path.isfile(file):
            files.append(file)

def main():
    parser = argparse.ArgumentParser(description='Codificador utilizando diferentes tipos de criptografia. Por padrão ele utilizará a SHA256.')
    parser.add_argument('-M', action='store_true', help='Calcula a MD5')
    args = parser.parse_args()

    if args.M:
        print('[+] Calculando MD5..')
        calculate_md5()
    else:
        print('[+] Calculando SHA256..')
        calculate_sha256()

def calculate_sha256():
    buffer_size = 65536
    sha256 = hashlib.sha256()

    try:
        for file in files:
            with open(file, 'rb') as thofile:
                while True:
                    data = thofile.read(buffer_size)
                    if not data:
                        break
                    sha256.update(data)
            
            hash_file = file + ".hash"
            with open(hash_file, 'w')  as thefile:
                ok = sha256.hexdigest()
                thefile.write(ok)
    except FileNotFoundError:
        return None

def calculate_md5():
    buffer_size = 65536
    md5l = hashlib.md5()

    try:
        for file  in files:
            with open(file, 'rb') as thofile:
                while True:
                    data = thofile.read(buffer_size)
                    if not data:
                        break
                    md5l.update(data)
            hash_file =  file + '.hash'
            with open(hash_file, 'w') as thefile:
                ok = md5l.hexdigest()
                thefile.write(ok)
    except FileNotFoundError:
        return None
    
if __name__ == "__main__":
    main()