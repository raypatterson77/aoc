import hashlib

def main():
    with open('input.txt') as f:
        secret_key = f.readline()
        test_hash  = ""
        test_key = ""
        secret_number = 0
        #part1
        while not test_hash[0:5] == '00000':
            secret_number += 1
            test_key = secret_key + str(secret_number)
            test_hash = str(hashlib.md5(test_key.encode()).hexdigest())
        print(f"Solution part1: {secret_number}")
        #part2
        while not test_hash[0:6] == '000000':
            secret_number += 1
            test_key = secret_key + str(secret_number)
            test_hash = str(hashlib.md5(test_key.encode()).hexdigest())
        print(f"Solution part2: {secret_number}")

if __name__ == '__main__':
    main()
