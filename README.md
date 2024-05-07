# fakeapi

a repo for fake api to test for api hosting

## GENERATE CERTS

```bash
certbot certonly --standalone -d api.brewith.us --staple-ocsp --agree-tos
```

## Run docker compose

```bash
docker-compose  -f docker-compose.prod.yml -f docker-compose.yml  up --build --force-recreate -d
```
