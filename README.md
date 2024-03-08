1. Download do Doxygen: https://www.doxygen.nl/download.html 

2. Download do GraphViz:  https://graphviz.org/download/ 

3. Para gerar a documentação, entre no diretório \doxygen\bin (sendo doxygen a pasta do download dele) do terminal, digite (substituindo o diretório local do arquivo doxyfile.txt, deste mesmo repositório do github, em seu computador): doxygen C:\Users\eric.abbade\Downloads\doxyfile.txt

4. Substitua os arquivos fontes (de entrada) dos códigos que se deseja documentar e o diretório de saída no qual a documentação será usada (encontre no arquivo: INPUT e OUTPUT_DIRECTORY, no doxyfile.txt).

5. Substitua os diretórios locais do GraphViz para que os diagramas de funções sejam gerados (encontre no arquivo: DIA_PATH e DOT_PATH, no doxyfile.txt).

6. Substitua os diretórios locais do logo e arquivo .css (doxygen-awesome, deste mesmo repositório do github) caso deseje maior personalização (encontre no arquivo: PROJECT_LOGO e HTML_STYLESHEET, no doxyfile.txt).

7. Edite outras configurações do doxifile.txt conforme suas preferências. 


Outros tutoriais para que o leitor possa buscar mais formas de adquirir conhecimento sobre esta ferramenta podem ser encontrados abaixo: 
- Tutorial, deste mesmo autor, mais detalhado sobre como documentar com o Doxygen:https://cnpemcamp.sharepoint.com/:w:/r/sites/sei/_layouts/15/Doc.aspx?sourcedoc=%7B39891b14-d224-4802-a628-0e8d8322cdab%7D&action=edit&wdPreviousSession=1ec3d986-1ec0-993f-11e9-98b6f0634e50
- Resumo (próprio site do Doxygen): https://www.doxygen.nl/manual/starting.html  
- Vídeo tutorial com resumo do processo da geração da documentação: https://www.youtube.com/watch?v=Rl50qI6e7HU  
- Resumo de uma documentação feita anteriormente: SIMAR: File List (cnpem-emi.github.io). 
