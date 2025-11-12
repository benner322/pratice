import argparse
import requests
parser = argparse.ArgumentParser()
parser.add_argument("-pn", "--package_name", type=str, required=True)
parser.add_argument("-u", "--url", type=str, default="https://pypi.org/pypi")
parser.add_argument("-t", "--test", type=int, default=0)
parser.add_argument("-o", "--output", type=str, default="deps")
parser.add_argument("-at", "--ascii_tree", type=int, default=0)
parser.add_argument("-d", "--deep", type=int, default=2)
parser.add_argument("-f", "--filter", type=str, default="")
args = parser.parse_args()
print(f"\nПолучение зависимостей для {args.package_name}...")
try:
    response = requests.get(f"{args.url}/{args.package_name}/json")
    data = response.json()
    deps = data['info'].get('requires_dist', [])
    print(f"\nПрямые зависимости {args.package_name}:")
    for dep in deps:
        print(f"  - {dep}")        
except:
    print("Ошибка: пакет не найден")
