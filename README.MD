# LMS

CRUD

## Usage:

1. Clone repository
2. Copy `./env/.env-default` to `./env/.env`
3. Add configuration data to `./env/.env`
4. If you don`t know what kind of configuration data you should provide, then use example data:

```bash
POSTGRES_USER=postgres
POSTGRES_PASSWORD=coderslab
POSTGRES_DB=lms
DATABASE_URL=postgres://postgres:coderslab@127.0.0.1:5432/lms

DEBUG=1
SECRET_KEY=django-insecure-ye9^i&m__*92n$veag$^jn3kkh9$3dh=ml_x9ab^-%#(p_vl2#
DJANGO_ALLOWED_HOSTS='127.0.0.1'

DJANGO_SU_NAME=testAdmin
DJANGO_SU_EMAIL=teastAdmin@aa.pl
DJANGO_SU_PASSWORD=testPass123 