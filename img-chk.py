#!/usr/bin/python3
import os
import imghdr
import argparse

img_types = ('.bmp', '.jpeg', '.jpg', '.gif', '.pbm', '.pgm', '.png', '.ppm', '.xbm', '.tiff')

parser = argparse.ArgumentParser(description='Check for Damaged Images in Directory')

parser.add_argument('-d', '--dir', dest='dir', default=os.getcwd(), type=str,
                    help='Dir path to check')
parser.add_argument('-e', '--extension', dest='extension', default=img_types, type=str,
                    help='Files extension')
parser.add_argument('-o', '--output', dest='output', default='', type=str,
                    help='Output file path')
parser.add_argument('-r', '--recursive', dest='recursive', action='store_const', const=True,
                    help='Recursive descent into subdirectories')
parser.add_argument('-v', '--verbose', dest='verbose', action='store_const', const=True,
                    help='Verbose info to std output')

args = parser.parse_args()


class ColorPrint:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.FAIL = ''
        self.ENDC = ''

    def print_fail(self, msg):
        print("".join([self.FAIL, msg, self.ENDC]))

    def print_file_ok(self, msg):
        print("".join([self.OKGREEN, msg, self.ENDC]))

    def print_dir_blue(self, msg):
        print("".join([self.OKBLUE, msg, self.ENDC]))


clr_print = ColorPrint()

checked = 0
broken = 0

if not args.dir:
    print('You must specify a directory with `-d DIRECTORY_PATH` argument')
    exit(1)

if not os.path.isdir(args.dir):
    print('Directory not found')
    exit(1)

if args.output:
    f = open(args.output, 'w')
else:
    f = False

if args.extension != img_types:
    args.extension = args.extension.lower()

for root, dirs, files in os.walk(args.dir):
    clr_print.print_dir_blue('Checking directory: %s' % root)
    for file in files:
        if file.lower().endswith(args.extension):
            checked += 1
            path = os.path.join(root, file)
            image_type = imghdr.what(path)
            if not image_type:
                broken += 1
                clr_print.print_fail('\t%s: fail' % file)
                if f:
                    f.write("".join([path,"\n"]))
            elif args.verbose:
                clr_print.print_file_ok('\t%s: ok' % file)

    if not args.recursive:
        break

total = '\nTotal checked: %d' % checked
print(total)
damaged = 'Total damaged images: %d' % broken
print(damaged)

if f:
    if not broken:
        f.write('No damaged images were found')
        
    f.write("".join(['\n', '-'*30, total, "\n", damaged]))