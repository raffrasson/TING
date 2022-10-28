import sys


def txt_importer(path_file):
    if path_file.endswith(".txt") is False:
        print("Formato inválido", file=sys.stderr)
    else:
        try:
            with open(path_file) as file:
                lines = file.readlines()
                formatted_lines = []
                for line in lines:
                    line = line.strip("\n")
                    formatted_lines.append(line)
                return formatted_lines
        except FileNotFoundError:
            print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
