'''
このプログラムと同じディレクトリ内に bibtex-file.txt として bibtex 形式のテキストを保存する
この Python ファイルを実行すると整形された文字列が出力される
'''

def main():

    bib = []

    author = ''
    title = ''
    publisher = ''
    journal = ''
    volume = ''
    number = ''
    pages = ''
    year = ''
    issn = ''
    doi = ''

    # 同じディレクトリ内にある bibtex-file.txt を、改行ごとに読み込む
    with open('bibtex-file.txt', 'r', encoding='utf-8') as f:
        file = f.read()
        bib_split = file.split('\n')  
        for line in bib_split:
            bib.append(line.strip())


    for line in bib:
        if 'author' in line:
            author = str(line[line.index('{') + 1:line.index('}')]) + ', '
            if 'and' in author:
                author = author.replace(' and ', ', ') 
        elif 'title' in line:
            if 'booktitle' in line:
                journal = str(line[line.index('{') + 1:line.index('}')]) + ', '
            else:
                title = '"' + str(line[line.index('{') + 1:line.index('}')]) + '", '
        elif 'publisher' in line:
            publisher = str(line[line.index('{') + 1:line.index('}')]) + ', '
        elif 'journal' in line:
            journal = str(line[line.index('{') + 1:line.index('}')]) + ', '
        elif 'volume' in line:
            volume = 'vol. ' + str(line[line.index('{') + 1:line.index('}')]) + ', '
        elif 'number' in line:
            number = 'no. ' + str(line[line.index('{') + 1:line.index('}')]) + ', '
        elif 'pages' in line:
            pages = 'pp.' + str(line[line.index('{') + 1:line.index('}')]) + ', '
        elif 'year' in line:
            year = str(line[line.index('{') + 1:line.index('}')]) + ', '
        elif 'issn' in line:
            issn = 'ISSN.' + str(line[line.index('{') + 1:line.index('}')]) + ', '
        elif 'doi' in line:
            doi = 'DOI: ' + str(line[line.index('{') + 1:line.index('}')])
        else:
            pass

    print(f'{author}{title}{journal}{volume}{number}{pages}{issn}{year}{doi}')


if __name__ == '__main__':
    main()