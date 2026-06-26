# raphael-slice

Forking, slicing, lineage, attribution

## API

- Prefix: `/v1/slice`
- Port: `8085`
- Health: `GET /health`

## Events

_Published and consumed events documented in `openapi.yaml` and raphael-contracts._

## Development

```bash
uv sync
uv run uvicorn raphael_slice.app:app --reload --port 8085
```

Part of the [Raphael Platform](https://github.com/hummingbird-labs) by HummingBird Labs.
