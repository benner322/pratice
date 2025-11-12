import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-pn", "--package_name", type=str, required=True)
parser.add_argument("-u", "--url", type=str, default="https://pypi.org/pypi")
parser.add_argument("-t", "--test", type=int, default=0, choices=[0, 1])
parser.add_argument("-o", "--output", type=str, default="deps")
parser.add_argument("-at", "--ascii_tree", type=int, default=0, choices=[0, 1])
parser.add_argument("-d", "--deep", type=int, default=2)
parser.add_argument("-f", "--filter", type=str, default="")
args = parser.parse_args()
print("Параметры:")
for key, value in vars(args).items():
    print(f"  {key}: {value}")
