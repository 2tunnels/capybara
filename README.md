# Capybara Shopify App

## Development

Using [docker-compose](https://docs.docker.com/compose/):

```bash
docker-compose up
```

## Docker

Build:

```bash
docker image build -t capybara .
```

Tag:

```bash
docker image tag capybara "2tunnels/capybara:latest"
docker image tag capybara "2tunnels/capybara:$(date +"%Y.%m.%d")-$(git rev-parse --short HEAD)"
```

Push:

```bash
docker image push "2tunnels/capybara:latest"
docker image push "2tunnels/capybara:$(date +"%Y.%m.%d")-$(git rev-parse --short HEAD)"
```
