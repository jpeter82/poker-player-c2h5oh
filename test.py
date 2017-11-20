
import re



def main():
    match = re.search('[AK]', 'CK')
    if match:
        print('1')
    else:
        print('2')


if __name__ == '__main__':
    main()