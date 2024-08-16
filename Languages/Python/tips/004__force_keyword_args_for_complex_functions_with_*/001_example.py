from enum import Enum


class Quality(Enum):
    LOW: int = 480
    MEDIUM: int = 1080
    HIGH: int = 1440


class Privacy(Enum):
    PRIVATE: str = 'Private'
    UNLISTED: str = 'Unlisted'
    PUBLIC: str = 'Public'


def upload(file: str, *, quality: Quality, privacy: Privacy) -> None:
    print(f"Uploading: {file} in {quality.value}p ({privacy.value})")


def main() -> None:
    upload(
        'dog.mp4',
        quality=Quality.HIGH,
        privacy=Privacy.PUBLIC
    )


if __name__ == '__main__':
    main()
