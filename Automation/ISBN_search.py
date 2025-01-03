import requests # para fazer as requisições
from bs4 import BeautifulSoup # para manipular o html recebido
import pandas as pd # para manipular os arquivos CSV
import time
import random # as duas são para gerarmos intervalos aleatórios de acesso

path = r"C:\caminho\livros.csv"

def invert_url_pattern(url):
    return url.replace("\\","/")

path = invert_url_pattern(path)

def search_book(path):
    url_base = "https://www.google.com/search?q=isbn"
    headers = {
    "User-Agent":"seu pc"
    }
    
    df = pd.read_csv(path, encoding='utf-8')
    books = df["Name"].tolist()
    media = df["media"].tolist()
    # vamos colocar as pesquisas aqui e depois inserir todas no DataFrame
    title_books = []
    isbn_books = []
    media_books = []  

    for index, book in enumerate(books):
        time.sleep(random.uniform(60, 90))
        
        url = url_base + "+" + book.replace(" ", "+")
        req = requests.get(url, headers=headers)

        site = BeautifulSoup(req.text, "html.parser")
        #usamos as class para buscar o conteúdo
        title = site.find("span", class_="Wkr6U")
        isbns = site.find_all("div", class_="bVj5Zb")
        medias = site.find_all("div", class_="TCYkdd")
        #se algo falhar, retornamos uma string vazia
        if not(hasattr(title, "text")):
            title_books.append("")
            isbn_books.append("")
            media_books.append("")
            continue

        # No loop, o último item acessado será o mais recente, 
        # pois percorremos a lista de cima para baixo. 
        # Por isso, invertendo a lista de ISBNs, garantimos que 
        # o mais novo de cada categoria seja processado por último.

        isbns = isbns[::-1]
        unified_data = {}
        title_books.append(title.text)

        for i in range(len(medias)):
            unified_data[medias[i].text] = isbns[i].text

        match media[index]:
            case "ebook":
                if "Livro digital" in unified_data:
                    isbn_books.append(unified_data["Livro digital"])
                    media_books.append("Livro digital")
                    continue

                first_key = list(unified_data)[0]
                isbn_books.append(unified_data[first_key])
                media_books.append("")
                
            case "fisical":
                if "Livro de capa dura" in unified_data:
                    isbn_books.append(unified_data["Livro de capa dura"])
                    media_books.append("Livro capa dura")
                    continue
                if "Livro de bolso" in unified_data:
                    isbn_books.append(unified_data["Livro de bolso"])
                    media_books.append("Livro capa dura")
                    continue
                first_key = list(unified_data)[0]
                isbn_books.append(unified_data[first_key])
                media_books.append("")

            case "audio":
                if "Audiolivro" in unified_data:
                    isbn_books.append(unified_data["Audiolivro"])
                    media_books.append("Audiolivro")
                    continue

                first_key = list(unified_data)[0]
                isbn_books.append(unified_data[first_key])
                media_books.append("")

            case _:
                first_key = list(unified_data)[0]
                isbn_books.append(unified_data[first_key])
                media_books.append("")

    df["Titulo do Livro"] = title_books
    df["ISBN"] = isbn_books
    df["Tipo de Livro"] = media_books

    return df

df = search_book(path)

df.to_csv(invert_url_pattern("C:seu\caminho\para\salvar\nome_do_arquivo.csv"), encoding='utf-8', index=False)