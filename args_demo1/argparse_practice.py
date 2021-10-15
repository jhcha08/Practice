import math
import argparse

parser = argparse.ArgumentParser(description='Calculate volume of a Cylinder')
parser.add_argument('-r', '--radius', type=int, help='Radius of Cylinder')
parser.add_argument('-H', '--height', type=int, help='Height of Cylinder')
args = parser.parse_args()

def cylinder_volume(r, h):
    v = (math.pi) * (r**2) * h
    return v

print(cylinder_volume(args.radius,args.height))

# 터미널에 C:\Users\User\(~사용자 작업공간~)> 라고 되어있을 때
# 그 뒤에 python argparse_practice.py -r 2 -H 4 이런식으로 적으면 됨
