from bs4 import BeautifulSoup
ex1 = '''
<html>
    <head>
        <title> HTML 연습 <title>
    </head>
    <body>
        <p align="center"> text 1 </p>
        <img src="c:\\temp\\image\\솔개.png">
    </body>
</html>'''

soup = BeautifulSoup(ex1, 'html.parser')
txt = soup.find('p')
