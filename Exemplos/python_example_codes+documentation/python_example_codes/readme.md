Este diretório possuí arquivos simples para ilustração da documentação de arquivos simples em Python. 

O arquivo python_example.py não tem nenhuma funcionalidade específica, mas simula tarefas comuns em programação para servir de exemplo.

Uma breve descrição de suas funcionalidades é dada a seguir:

Existe um laço while True que aciona a função F1() a cada 5 segundos.  Essa função F1() atualiza a variável var_state para verdadeiro para sinalizar que a operação está começando, além de enviar um valor aleatório entre 1 e 10 para a função F2().  

Já essa outra função   F2(), primeiramente, identifica se o valor aleatório é maior que o contador (var_counter) atual. Então, a variável var_counter irá assumir o maior valor entre os dois. Caso, essa variável seja igual a 10, será acionado a função F4(), após se ativar o reset (var_reset passa a ser verdadeiro). Se não, após o tempo de 1 segundo o contador var_counter será atualizado em 1 e a função F3() será acionada.  Isso é feito para simular um processo em que não se pode alterar a variável var_counter duas vezes em seguida, muito rápido. 

Quando a função F3() é acionada, ela identifica se o contador var_counter é igual a 10, e caso seja, ativa o reset (var_reset passa a ser verdadeiro). Depois, a função F4() é acionada. Isso é feito para que a função F4() identifique se deve, ou não, zerar o controlador. 

Por fim, quando a função F4() é acionada ela identifica se a variável (var_reset) é verdadeira, e caso seja reseta o contador (zerando-o).  A variável var_reset é ativada sempre que o contador chega a 10. Dessa forma, se em qualquer momento do código o contador for igual a 10, a função F4() irá zerá-lo. Assim, o código simula um procedimento, no qual o controlador não pode ter um valor maior que 10. 

O arquivo python_example2.py exerce funcionalidades similares ao arquivo python_example.py, porém com algumas nomenclaturas de funções diferentes, também, para fins demonstrativos.
