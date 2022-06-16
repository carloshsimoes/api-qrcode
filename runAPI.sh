nohup localstack start &
sleep 5
awslocal s3api create-bucket --bucket qrcode
python3 app.py