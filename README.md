Tutorial resumido do uso do Doxygen (9 eteapas):

1. Download do Doxygen: https://www.doxygen.nl/download.html 

2. Download do GraphViz:  https://graphviz.org/download/ (é opcional, mas recomendado para a criação dos diagramas de funções).
   
3. Baixe o doxyfile.txt: https://github.com/cnpem-emi/Doxygen/blob/master/doxyfile.txt.
 
4. Substitua os arquivos fontes (de entrada) dos códigos quais se desejam documentar e o diretório de saída no qual a documentação será gerada (encontre no doxyfile.txt: INPUT e OUTPUT_DIRECTORY).

5. Substitua os diretórios locais do GraphViz para geração dos diagramas de funções (encontre no doxyfile.txt: DIA_PATH e DOT_PATH).

6. Opcional: substitua os diretórios locais do logo e arquivo .css  (encontre no doxyfile.txt: PROJECT_LOGO e HTML_STYLESHEET). Exemplo de .css: https://github.com/cnpem-emi/Doxygen/blob/master/doxygen-awesome.css.

7. Opcional: edite outras configurações do doxyfile.txt, conforme suas preferências.
   
8. No terminal entre no diretório \doxygen\bin (sendo doxygen a pasta do software baixado do tópico 1), digite: doxygen C:\Users\eric.abbade\Downloads\doxyfile.txt  (substituindo o diretório local do doxyfile.txt do tópico 3 de seu computador).
   
9. Acesse a documentação em html/index no diretório de saída definido por você.

<br></br>
Outros tutoriais para que o leitor possa buscar mais formas de adquirir conhecimento sobre esta ferramenta podem ser encontrados abaixo: 
- Tutorial, desse mesmo autor, mais detalhado sobre como documentar com o Doxygen:https://cnpemcamp.sharepoint.com/:w:/r/sites/sei/_layouts/15/Doc.aspx?sourcedoc=%7B39891b14-d224-4802-a628-0e8d8322cdab%7D&action=edit&wdPreviousSession=1ec3d986-1ec0-993f-11e9-98b6f0634e50
- Resumo (próprio site do Doxygen): https://www.doxygen.nl/manual/starting.html  
- Vídeo tutorial com resumo do processo da geração da documentação: https://www.youtube.com/watch?v=Rl50qI6e7HU  
- Resumo de uma documentação feita anteriormente: SIMAR: File List (cnpem-emi.github.io).
  
<br></br>
Para melhor compreensão do uso do Doxygen, leia os outros dois documentos deste diretório:
 - Relatório Doxygen.pdf - Relatório analisando casos em que o Doxygen deve ser usado, bem como suas vantagens e desvantagens.
 - Tutorial Doxygen.pdf - Tutorial, deste mesmo autor, mais detalhado sobre como documentar com o Doxygen.

<br></br>
Por fim, a pasta: Exemplos tem 3 conjuntos de arquivos e suas 3 respectivas documentações, para ilustrar o uso do Doxygen. 
