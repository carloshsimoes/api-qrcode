import boto3
import random
import logging
from botocore.exceptions import ClientError

s3 = boto3.client(
    service_name='s3',
    region_name='us-east-1', 
    aws_access_key_id='test', 
    aws_secret_access_key='test',
    endpoint_url = "http://localhost.localstack.cloud:4566"
)

bucketName = 'qrcode'

def gerarNomeQRCodeDinamico():
    conjunto = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    tamanho = 32
    nomeDinamico = f"{''.join(random.sample(conjunto, tamanho))}.png"
    return nomeDinamico


def enviarQRcode(obj):
    obj_nome = gerarNomeQRCodeDinamico()
    try:
        s3.upload_file(obj, bucketName, obj_nome)
        return criarUrlAssinada(obj_nome, bucketName)
    except ClientError as e:
        logging.error(e)
        return None


def criarUrlAssinada(obj_nome, bucket, tempoExp=3600):
    try:
        resposta = s3.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket,
                                                            'Key': obj_nome},
                                                    ExpiresIn=tempoExp)
    except ClientError as e:
        logging.error(e)
        return None

    return resposta
