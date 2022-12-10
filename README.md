# SEL0337
Prática 6

Nesta prática desenvolveu-se um script que realiza foto e vídeo atvavés do módulo de câmera acoplada à raspberry pi, além de acessar os dados da estação climática da UFSC. 

Para o acesso à câmera, é necessário a importação da biblioteca picamera. Assim, torna-se possível a rotação da imagem; o acionamento da câmera; registro de texto na imagem; a captura de imagem ou registro de um vídeo; e encerramento da câmera. Tendo em vista que a imagem sofre interferência da irradiação, então adiciona-se um delay na captura para corrigir a posição da câmera. Para isso, utiliza-se a função sleep() da biblioteca time.  

Os dados climáticos são obtidos através do ambiente Web Oracle URL, junto da ID 966583. Para isso, utiliza-se a função get(), responsavel pela coleta dos dados em Java, convertendo-os em python. Por fim, imprime os dados climáticos no terminal através da função pprint(). P

Para mais detalhes, acessar o script "pratica6.py".
