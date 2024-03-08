Download do Doxygen: https://www.doxygen.nl/download.html 
Download do GraphViz:  https://graphviz.org/download/ 

Para gerar a documentação, entre no diretório \doxygen\bin (sendo doxygen a pasta do download dele) do terminal, digite (substituindo o diretório local do arquivo doxyfile.txt, deste mesmo repositório do github, em seu computador): doxygen C:\Users\eric.abbade\Downloads\doxyfile.txt

Substitua os arquivos fontes (de entrada) dos códigos que se deseja documentar e o diretório de saída no qual a documentação será usada (encontre no arquivo: INPUT e OUTPUT_DIRECTORY).
Substitua os diretórios locais do GraphViz para que os diagramas de funções sejam gerados (encontre no arquivo: DIA_PATH e DOT_PATH).
Substitua os diretórios locais do logo e arquivo .css (doxygen-awesome, deste mesmo repositório do github) caso deseje maior personalização (encontre no arquivo: PROJECT_LOGO e HTML_STYLESHEET ).
