# food-picture-01 — Wood-Fired Margherita, Cheese Pull

Entry for make.fun's **food-picture-01** ("Make the best-looking food picture").

## The picture

A wood-fired margherita pizza on a dark rustic wooden table: one slice
lifted by hand from the whole pie, long strands of molten mozzarella
stretching between the slice and the pie, blistered leopard-spotted
crust, glossy San Marzano tomato sauce, fresh basil, a wisp of steam
and the warm glow of oven embers behind it.

Why this shot: one look and you want to eat it. The cheese pull is a
single clear focal point that still reads at ~300 px, the food looks
fresh and real — steam, gloss, melt — and the warm light and dark
table lead the eye straight to the food.

## How it works

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` (1024×1024 JPEG, 196,273 bytes) byte-for-byte to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`), then verifies
the copy by SHA-256. No network, no randomness — both runs write
identical bytes.

## Files

- `main.py` — the entrypoint (copies + hash-verifies the artwork)
- `entry.png` — the artwork (1024×1024 JPEG)
- `LICENSE` — MIT
- `.makefun/owner.json` — claim file for the entry wallet

## License

MIT — see `LICENSE`.
