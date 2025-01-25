from LxmlSoup import LxmlSoup
import requests

class Error(Exception):
    pass

class Parser:
    def __init__(self, base_url:str, filename:str):
        self.__url = base_url   # Базовый url, к которому будет присоединен номер страницы
        self.__num_of_title = 1
        
        if self.__url[-1] != "/":
            self.__url += "/"

        if filename[-4:] == ".txt":
            self.__filename = filename
        else:
            raise Error("\nОшибка!\nФайл должен быть с расширением .txt")

        print(self.__url)
        
    def main(self, tag1:str, class_1:str, tag2:str, class_2:str):
        page = 1
        with open(self.__filename, 'w', encoding='utf-8') as file:
            pass  # Просто открываем и закрываем файл, чтобы очистить его

        with open(self.__filename, "a", encoding="utf-8") as file:
            while True:
                url = f"{self.__url}page{page}"
                print(url)
                html = requests.get(url).text

                soup = LxmlSoup(html)

                authors = soup.find_all(tag1, class_=class_1)
                titles = soup.find_all(tag2, class_=class_2)

                if not authors or not titles:
                    break
                
                for i in range(min(len(authors), len(titles))):
                    self.__num_of_title += 1
                    author_name = authors[i].text()
                    title_text = titles[i].text()
                    print(f"{self.__num_of_title}. Автор: {author_name}\nСтатья: {title_text}\n\n")
                    file.write(f"{self.__num_of_title}. Автор: {author_name}\nСтатья: {title_text}\n\n")

                # Переход к новой странице
                page += 1