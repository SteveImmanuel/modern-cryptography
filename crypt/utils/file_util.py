def load_file(filepath: str, chunk_size: int):
    """
    Load file by chunk_size in bytes
    """
    with open(filepath, 'rb') as file_in:
        buffer = file_in.read(chunk_size)
        while buffer != b'':
            yield buffer
            buffer = file_in.read(chunk_size)


def save_file(path: str, data: str):
    """
    Save file to path
    """
    with open(path, 'w') as file:
        file.write(data)


if __name__ == "__main__":
    for a in load_file('testread', 10):
        print(type(a))
        print(a)