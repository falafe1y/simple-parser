from parser import Parser

def main():
    parser = Parser("https://habr.com/ru/articles", "Habr.txt")
    parser.main("a", "tm-user-info__username", "a", "tm-title__link")

if __name__ == "__main__":
    main()