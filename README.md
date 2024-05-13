# fastapi-template APIs

## Installation requirements

- pip install -r requirements.txt

## Configuration ⚙️

- Use ReCaptcha V2
- Set environment variable
  - FA_DB_HOST
  - FA_DB_USER
  - FA_DB_PASSWORD
  - FA_DB_NAME
  - FA_JWT_KEY
  - FA_RE_CAPTCHA_SECRET
  - FA_SES_FROM_EMAIL
  - FA_FERNET_KEY

- Create an empty database in database server

## Create a symmetric key for JWT encryption 🔑

- Open terminal
- `python`
- `from jwcrypto import jwk`
- `key = jwk.JWK(generate='oct', size=256)`
- `key.export()`
- Copy value and use as `JWT_KEY`

## Create a key for fernet encryption 🔐

- Open terminal
- `python`
- `from cryptography.fernet import Fernet`
- `key = Fernet.generate_key()`
- `key.decode('utf-8')`
- Copy value and use as `FERNET_KEY`

## SES permissions 📧

- Create inline policy, Use following policy.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "ses:SendEmail",
                "ses:SendBounce"
            ],
            "Resource": "*"
        }
    ]
}
```

## Quick Start 🚀

- Open terminal in project root
- Run server: `uvicorn app.main:app --reload --host 0.0.0.0`

## Docker Steps

- Build docker image.
- `docker build -t api:latest .`
- Run container with network access.
- `docker run -d -p 8000:8000 api`
- View container id.
- `docker ps`
- Stop container.
- `docker stop container_id`

## Data Migrations

- To create new migrations from model changes
- `alembic revision --autogenerate -m "Comment"`
- To update database with new changes
- `alembic upgrade head`
