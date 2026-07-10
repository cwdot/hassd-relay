# hassd Relay

A Home Assistant custom integration (HACS) intended to expose services that relay
into the palantir [`hassd`](https://github.com/cwdot/palantir) daemon, mirroring
[`labd-relay`](https://github.com/cwdot/labd-relay).

## Status

**Stub.** This is a scaffold only — the integration loads and can be added via the
config flow, but it defines **no services yet**. Real relay services will be added
here later.

## Development

```sh
make build   # ruff lint + pytest
make run     # launch a throwaway HA with this integration symlinked
```
