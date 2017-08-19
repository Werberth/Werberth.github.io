title: Plugando baterias externas: Aprenda a configurar o Sass no Django usando o Django-Compressor e Libsass
date: 2017-08-12 18:36 
category: Django
tags: sass, css, pre-processadores, django, python, django-compressor
slug: aprenda-a-configurar-o-sass-no-django-usando-o-django-compressor-e-libsass
author: Werberth Vinícius
email: werberthvinicius@gmail.com
about_author: Pythonist, Django developer, Linux enthusiast and headbanger in the spare time.
github: werberth
twitter: Werberthgomes

Quando desejamos desenvolver uma aplicação independente da deadline, sempre tentamos ao máximo aumentar nossa produtividade, utilizando bibliotecas que forneçam ferramentas úteis para o desenvolvimento de determinados componentes do projeto. O pré-processador [Sass](http://sass-lang.com/) é uma dessas ferramentas. Ele é o mais famoso, maduro e estavél pre-processador de CSS que existe, e que nos auxilia a escrever CSS mais rapidamente, reaproveitando codigo e seguindo o princípio do [DRY (Don't Repeat Yourself)](https://pt.wikipedia.org/wiki/Don%27t_repeat_yourself), já bem conhecido por nós programadores Python. 

````css
$highlight-color: #6CF0AF;
$hightligh-border: 1px $hightlight-color solid;

#content {
	border: $highlight-color: #6CF0AF;
	&:hover { color: #161935; }

	article {
		h1 { color: #333 }
		p { margin-bottom: 1.4em; }
		&:hover { float: left; }
	}
	aside { background-color: #eee; }

	#container {
		background-color: $hightlight-color;
		p, h3 { color: #fff; }
	}
}
````
<small><center>Exemplo da sintaxe (arquivos *.scss*) utilizada pelo Sass.</center></small>

Apesar da sintaxe ser um pouco diferente (além de permitir a criação de váriaveis, herança, imports, entre outras coisas), o Sass irá "compilar" seus arquivos *.scss* (ou *.sass*), gerando os arquivos *.css* que serão (finalmente) renderizados pelo navegador, ou seja, no final, tudo se torna CSS.

Ai você me pergunta, "Como eu faço pra utilizar o Sass na minha aplicação Django?". Bem, não é nenhum BICHO DE SETE CABEÇAS, com apenas alguns minutinhos em frente ao computador, você consegue configurar tudo, sem ter problemas.

####Utilizando Django Compressor
Django Compressor é um modulo python que tem como principal objetivo, comprimir arquivos JavaScript e CSS em um unico arquivo  cacheável.

![Django Compressor Diagrama](https://werberth.github.io/images/posts/django_compressing.png" Django Compressor Diagrama")
<small><center>Diagrama do processo de compressão dos arquivos estáticos pelo Django Compressor - Creditos para [aptuz.com](http://aptuz.com/blog/)</center></small>

Para instala-lo, utilizaremos o pip, inserindo o seguinte comando no terminal (ou cmd):
````shell
$	pip install django-compressor
````
Após o termino da instalação, devemos adicionar o módulo a variável *INSTALLED_APPS* no arquivo settings.py do nosso projeto:
````python
#settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    ...
    'compressor',
    ...
]
````
Agora, precisamos definir a variável [*STATICFILES_FINDERS*](https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-STATICFILES_FINDERS) (que é nada mais, nada menos, que uma lista com buscadores, que localizam os arquivos estáticos da nossa aplicação django), adicionando nela os buscadores padrões, e também a classe de busca do Django-Compressor:

````python
# settings.py
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    ...
    'compressor.finders.CompressorFinder',
)
````
E para finalizar a primeira parte de configuração do compressor, precisamos envolver nossos arquivos CSS e JS pela tag *{% compress **tipo_do_arquivo** %}*: 

````html
	{% compress css %}
    	<link type="text/css" rel="stylesheet" href="{% static 'css/style1.css' %}"/>
    	<link type="text/css" rel="stylesheet" href="{% static 'css/buttons.scss' %}">
	{% endcompress %}

	...

	{% compress js %}
	 	<script type="text/javascript" src="{% static 'js/jquery/jquery-2.2.1.min.js' %}"></script>
	 	<script type="text/javascript" src="{% static '/js/init_components.js' %}"></script>
	{% endcompress %}
````

#### [Libsass](https://github.com/dahlia/libsass-python) - Pré Compilador
O Sass é inscrito em Ruby, porém, podemos utilizar alguns mecanismos para compilar nossos arquivos *.scss* (ou *.sass*) automaticamente, ao rodar o servidor (comando *python manage.py runserver*). Para isso precisamos instalar o biblioteca que irá auxiliar o Django Compressor nessa tarefa, seu nome é *Libsass* e sua instalação pode ser feita através do seguinte comando:
````shell
$	pip install libsass
````
Utilizaremos o Django Compressor já instalado e configurado, para executar o pré compilador. Pra isso, iremos adicionar a seguinte variável ao settings.py da nossa aplicação:
````python
# settings.py
COMPRESS_PRECOMPILERS = (
    ('text/x-sass', 'sassc {infile} {outfile}'),
) 
````
<small><center>O binário *sassc* foi instalado a partir do libsass, o parametro *{inframe}* se refere ao arquivo de entradas *.scss* (ou *.sass*), e o parametro *{outfile}* refere-se ao arquivo de saída, já compilado como arquivo *.css*.</center></small>

Agora que tudo já está configurado, basta definirmos todos os nossos arquivos de estilização escritos usando Sass, com o atributo *type* igual a *text/x-sass*:
````html
{% compress css %}
    <link rel="stylesheet" href="{% static 'css/base.css' %}" type="text/css">
    <link rel="stylesheet" href="{% static 'scss/container.scss' %}" type="text/x-sass">
    <link rel="stylesheet" href="{% static 'scss/side_bar.scss' %}"" type="text/x-sass">
{% endcompress %} 
````

Pronto, sass configurado com sucesso, agora toda vez que o comando *python manage.py runserver* for executado, os arquivos Sass serão pré compilados, cacheados em um só arquivo, e executados como um arquivo css normal. Muito fácil, não é?

### Conclusão
Utilizando somente dois pequenos modulos, fomos capazes de plugar o Sass a nossa aplicação Django (sem a utilização de outra linguagem de programação), e assim podemos desfrutar dessa ferramenta tão poderosa.

Até o próximo tutorial pessoal! o/