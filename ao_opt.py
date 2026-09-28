import os

_LOSSLESS = ("opt4", "opt12", "opt13", "opt14")

# Every option, ON by default. This exact set is the tree measured end to end.
_DEFAULT = (
    "opt1",
    "opt2",
    "opt3",
    "opt4",
    "opt5",
    "opt6",
    "opt7",
    "opt8",
    "opt9",
    "opt10",
    "opt11",
    "opt12",
    "opt13",
    "opt14",
    "opt15",
)

_OFF = ("off", "0", "no", "none", "stock", "false")


def _resolve():
    raw = (os.environ.get("AO_OPT") or "").strip()
    if raw == "":
        return set(_DEFAULT)
    low = raw.lower()
    if low in _OFF:
        return set()
    if low == "lossless":
        return set(_LOSSLESS)
    if low in ("all", "default", "on"):
        return set(_DEFAULT)
    toks = [t.strip() for t in raw.split(",") if t.strip()]
    if all(t.startswith("-") for t in toks):
        return set(_DEFAULT) - {t[1:] for t in toks}
    return {t for t in toks if not t.startswith("-")} - {t[1:] for t in toks if t.startswith("-")}


_ACTIVE = _resolve()


def ON(token):
    return token in _ACTIVE


def active():
    return sorted(_ACTIVE)


def banner():
    a = active()
    return ("[autooptm] AO_OPT: " + (",".join(a) if a else "off (stock path)")
            + "   (AO_OPT=off for the original code, AO_OPT=lossless for the "
              "exact subset)")
