
# Oxi ?  

Oxi? é um indexador de site, ele armazena a URL de sites para que sejam acessadas posteriormente, recriando a experiência dos primeiros buscadores da Internet, que armazenavam os sites em suas bases de dados e você procurava qual site gostaria de acessar em imensas listas.  
 


## Funcionalidades

- Aplicação via Terminal
- Adição / Remoção de sites da lista
- Visualização da lista de sites armazenados
- Opção para escolha aleátoria de sites


## Instalação
Dependências necessárias  
- Python 3.10
- Rich 11.2.0 

Instale o Rich  
```bash
  python -m pip install rich
```
Clone o repositório 


```bash
  git clone https://github.com/Physis19/Indexador-de-sites.git
```
Execute o arquivo main
```bash
  python3 main.py
```
### Instalação via Docker 
A aplicação também está disponível no DockerHub
```bash
  docker pull physis19/oxi_search
```
Para executar a imagem, passe o paramêtro ```-ti ```
  
```bash
  docker run -ti physis19/oxi_search
```


## Uso/Exemplos
Para usar o "Oxi?" é extremamente simples, já existe uma lista de sites preenchida por padrão, mas você pode adicionar ou remover quantos sites quiser.        
- ```1``` Adiciona um novo site, digitando a URL
- ```2``` Remove um site, digitando a URL
- ```3``` Lista todos os sites armazenados
- ```4``` Escolhe um site aleátorio da lista
- ```0``` Encerra o programa

![oxi_2](https://user-images.githubusercontent.com/117491674/226180654-ad08be2d-7b7a-4257-b13b-2b4479d2f8b9.png)

## Apêndice

Projeto simples desenvolvido para a matéria de Estrutura de Dados na Universidade Federal de Alagoas

## Licença

[MIT](https://choosealicense.com/licenses/mit/)


