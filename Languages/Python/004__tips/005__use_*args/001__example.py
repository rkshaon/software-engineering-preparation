def join_text(*args, sep: str) -> str:
    print(args)
    return sep.join(args)


def main() -> None:
    print(join_text('A', 'B', 'C', sep='-'))
    print(join_text('X', 'Y', 'Z', sep='/'))


if __name__ == '__main__':
    main()
