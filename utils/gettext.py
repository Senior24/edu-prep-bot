import yaml

from pathlib import Path

from data.config import PRIMARY_LANG

locales = {
    path.stem: yaml.safe_load(path.read_text(encoding="utf-8"))
    for path in Path("locales").glob("*.y*ml")
}

def _(key: str, lang: str) -> str:
    if lang in locales and key in locales[lang]:
        return locales[lang][key]
    return locales.get(PRIMARY_LANG, {}).get(key, key)
