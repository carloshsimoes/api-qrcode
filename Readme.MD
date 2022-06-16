# API QRCode v1

API desenvolvida em Python para criação de QRCode à partir de uma URL (string) encaminhada. Devolvendo um QRCode e também um Encurtador de URL.

# O que é LocalStack?

LocalStack é uma solução para simular um Stack Cloud Local totalmente funcional. Aonde você pode localmente testar chamadas de API para a Stack Local simulando vários serviços AWS como S3, API Gateway, CloudFront, Amplify e dentre vários.

Maiores informações sobre o LocalStack:

> https://docs.localstack.cloud/aws


# Nossa API:

**Rotas criadas:**

- /health-check ==> Rota para validar a saúde da API;

- /qrcode ==> Rota da API

Deverá ser passado o argumento **url**, no qual à partir desse argumento/string será gerado um QRCode Dinâmico.

### Exemplo:

> http://127.0.0.1:5000/qrcode?url=https://www.google.com


### Retorno da API:

Atendendo os requisitos, passando a URL com tamanho mínimo de 4 caracteres, será retornado:

- **qrcode**; URL Pré-assinada do Objeto enviado a um Bucket S3, aqui utilizamos a solução **LocalStack** para simular a Stack da AWS.

- **shorturl**; Na API, existe uma função que, caso a URL tenha tamanho maior que 40 caracteres, é gerada uma URL Encurtada automaticamente, caso seja inferior que, será apresentada a URL original.

- **url**; URL original enviada na requisição.


```json
{
    "qrcode": "http://localhost.localstack.cloud:4566/qrcode/rx8KawJRySDAMnPfiTu3dt60NVGFBlh5.png?AWSAccessKeyId=test&Signature=OZBXlRWk5pKs9r%2FvrkrEXmXY86E%3D&Expires=1655337397",
    "shorturl": "https://www.google.com",
    "url": "https://www.google.com"
}
```


### Chamada sem atender os requisitos:

```json
{
    "error:": "bad request",
    "url": [
        {
            "lenght": "> 3",
            "required": true
        }
    ]
}
```


# Requisitos para Rodar a API Local:

Para executar a API, considerando que possua o Python3 instalado, e à partir do diretório do Repositório Clonado:

### Criar VENV e instalar os requerimentos

```bash

python3 -m venv --prompt ApiQRCode .venv

. .venv/bin/activate

pip install -r requirements.txt

```

### Em seguida, será necessário dentro do VENV criado conforme acima, executar o LocalStack, criar o bucket {qrcode}, para então iniciar a API:

**- Executando Manualmente:**

```bash

localstack start

awslocal s3api create-bucket --bucket qrcode

python3 app.py

```


**- Executando pelo Script SH:**

```bash

./runAPI.sh

```


# Chamando a API e testando:

```bash

curl --location --request GET 'http://127.0.0.1:5000/qrcode?url=https://www.google.com'

```

```json
{
    "qrcode": "http://localhost.localstack.cloud:4566/qrcode/rx8KawJRySDAMnPfiTu3dt60NVGFBlh5.png?AWSAccessKeyId=test&Signature=OZBXlRWk5pKs9r%2FvrkrEXmXY86E%3D&Expires=1655337397",
    "shorturl": "https://www.google.com",
    "url": "https://www.google.com"
}
```

```bash

curl --location --request GET 'http://127.0.0.1:5000/qrcode?url=https://www.google.com.br/search?q=fotos+lindas&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjG1JuwwrD4AhUzupUCHQQwAEkQ_AUoAXoECAEQAw&biw=1366&bih=695&dpr=1'

```

```json
{
    "qrcode": "http://localhost.localstack.cloud:4566/qrcode/FRBoVSeQ8C3fY2lPbdirUk7p5G9mLqvX.png?AWSAccessKeyId=test&Signature=wBTdEeWsByfS3dZzunDU%2F97GwnE%3D&Expires=1655338305",
    "shorturl": "https://tinyurl.com/2byypg44",
    "url": "https://www.google.com.br/search?q=fotos lindas"
}
```

# Flag para exibir o QRCode direto em HTML:

### Parametro: ishtml=1

```bash

curl --location --request GET 'http://127.0.0.1:5000/qrcode?url=https://google.com&ishtml=1'

```

```html

<div align=center>
	<img src='http://localhost.localstack.cloud:4566/qrcode/0OvjpeGlQDE2W6RqyzaVCs9BMxPgYtk8.png?AWSAccessKeyId=test&Signature=qOOHSOXnRXkirbx3bDqkJKBP2Yc%3D&Expires=1655345221' />
	<br />
	<a href="https://google.com">https://google.com</a>
</div>

```