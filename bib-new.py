'''
使い方
cat bibが書いてあるテキストファイル.txt | python3 bib.py > result.txt
'''

def main():

    bib = []
    
    # bibtex のテキストを最後まで bib に代入
    while True:
        try:
            bib.append(input())
        except EOFError:
            break
    
    # print(bib[0])

    # それぞれに分解
    abbre = [bib[0]]
    authors = [x for x in bib[1:] if 'author' in x]
    title = [x for x in bib[1:] if 'title' in x]
    booktitle = [x for x in bib[1:] if 'booktitle' in x or 'journal' in x]
    volume = [x for x in bib[1:] if 'volume' in x]
    number = [x for x in bib[1:] if 'number' in x]
    pages = [x for x in bib[1:] if 'pages' in x]
    year = [x for x in bib[1:] if 'year' in x]
    publisher = [x for x in bib[1:] if 'publisher' in x]
    doi = [x for x in bib[1:] if 'doi' in x]

    # いらないところを削除
    abbre = abbre[0][abbre[0].index('{') + 1:]
    authors = authors[0][authors[0].index('{') + 1:authors[0].index('}')]
    title = title[0][title[0].index('{') + 1:title[0].index('}')]
    booktitle = booktitle[0][booktitle[0].index('{') + 1:booktitle[0].index('}')]
    volume = volume[0][volume[0].index('{') + 1:volume[0].index('}')]
    number = number[0][number[0].index('{') + 1:number[0].index('}')]
    pages = pages[0][pages[0].index('{') + 1:pages[0].index('}')]
    year = year[0][year[0].index('{') + 1:year[0].index('}')]
    publisher = publisher[0][publisher[0].index('{') + 1:publisher[0].index('}')]
    doi = doi[0][doi[0].index('{') + 1:doi[0].index('}')]

    # 出力
    print(f'{authors}, "{title}", {booktitle}, vol. {volume}, pp. {pages}, {year}, DOI:{doi}')



if __name__ == "__main__":
    main()