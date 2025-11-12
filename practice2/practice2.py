import argparse
import requests
import graphviz
import re
def get_package_deps(package_name, url):
    try:
        response = requests.get(f"{url}/{package_name}/json", timeout=10)
        data = response.json()
        deps = data['info'].get('requires_dist', [])
        clean_deps = []
        for dep in deps:
            if dep:
                clean_dep = re.split(r'[><=~;\[\]]', dep)[0].strip()
                if clean_dep and not clean_dep.startswith(':'):
                    clean_deps.append(clean_dep)
        return clean_deps
    except:
        return []
def generate_graphviz(package_name, deps, output_file):
    dot = graphviz.Digraph()
    dot.attr(rankdir='TB')   
    dot.node(package_name, package_name, shape='box', style='filled', fillcolor='lightblue')  
    for dep in deps:
        dot.node(dep, dep, shape='ellipse', style='filled', fillcolor='lightgreen')
        dot.edge(package_name, dep)    
    dot.render(output_file, format='svg', cleanup=True)
    print(f"SVG файл создан: {output_file}.svg")
def print_ascii_tree(package_name, deps):
    print(f"\nASCII-дерево {package_name}:")
    print(package_name)
    for i, dep in enumerate(deps):
        prefix = "└── " if i == len(deps)-1 else "├── "
        print("    " + prefix + dep)
parser = argparse.ArgumentParser()
parser.add_argument("-pn", "--package_name", type=str, required=True)
parser.add_argument("-u", "--url", type=str, default="https://pypi.org/pypi")
parser.add_argument("-t", "--test", type=int, default=0)
parser.add_argument("-o", "--output", type=str, default="deps")
parser.add_argument("-at", "--ascii_tree", type=int, default=0)
parser.add_argument("-d", "--deep", type=int, default=2)
parser.add_argument("-f", "--filter", type=str, default="")
args = parser.parse_args()
deps = get_package_deps(args.package_name, args.url)
if args.filter:
    deps = [dep for dep in deps if args.filter.lower() in dep.lower()]
if deps:
    generate_graphviz(args.package_name, deps, args.output)
else:
    print("Нет зависимостей для визуализации")
if args.ascii_tree and deps:
    print_ascii_tree(args.package_name, deps)
