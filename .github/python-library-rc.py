import os
import tomllib
import tomli_w


NEW_TAG = os.getenv("NEW_TAG")


with open("pyproject.toml", "rb") as f:
    data = tomllib.load(f)
    data["tool"]["poetry"]["version"] = NEW_TAG


with open("pyproject.toml", "wb") as f:
    tomli_w.dump(data, f)
