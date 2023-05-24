import subprocess


def execute_code(code_path):
    subprocess.run(['python', code_path])
    print(f"{code_path} executado com sucesso.")


def execute_all_codes():
    code_paths = [
        'average_filter/average_filter.py',
        'brightness/brightness.py',
        'contrast/contrast.py',
        'convert_grey/convert_grey.py',
        'flip/flip_horizontal.py',
        'flip/flip_vertical.py',
        'gaussian_filter/gaussian_filter.py',
        'grey_to_wb/grey_to_wb.py',
        'rgb/rgb.py',
        'rotate/rotate.py',
        'median_filter/median_filter.py',
    ]
    for code_path in code_paths:
        execute_code(code_path)


def main():
    execute_all_codes()


if __name__ == '__main__':
    main()
