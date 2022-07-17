import io
import os
from datetime import datetime


def get_lines_count(file_path):
    if os.path.getsize(file_path) == 0:
        return 0
    count = 1
    last = None
    with open(file_path, 'rb', buffering=io.DEFAULT_BUFFER_SIZE) as file:
        while byte := file.read(1):
            if (last := byte) == b'\n':
                count += 1
    # не учитывать последнюю пустую строку
    return count - 1 if last == b'\n' else count


if __name__ == '__main__':
    file_list = [file_name for file_name in os.listdir() if file_name.endswith('.txt')]
    files = []
    for file in file_list:
        files.append({
            'file_name': file,
            'lines_count': get_lines_count(file)
        })
    prefix = str(datetime.now()).split('.')[0].replace(' ', '_').replace(':', '-')
    with open(prefix + '.result', 'w', encoding='utf-8') as output_file:
        for file in sorted(files, key=lambda file: file['lines_count']):
            output_file.writelines([file['file_name'], '\n', str(file['lines_count']), '\n'])
            last_line = None
            with open(file['file_name'], encoding='utf-8') as input_file:
                current_line = 0
                while line := input_file.readline():
                    current_line += 1
                    if current_line == file['lines_count']:
                        last_line = line
                    output_file.writelines(line)
            if not last_line.endswith('\n'):
                output_file.write('\n')
