import os

ENTRY = 'She missed the last train home, so she walked forty miles through the night, and by dawn the road had taught her she never needed the ticket — only the leaving.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
