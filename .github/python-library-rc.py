import tomllib
import tomli_w


with open("pyproject.toml", "rb") as f:
    data = tomllib.load(f)
    data["tool"]["poetry"]["version"] = "0.3.0"


with open("pyproject.toml", "wb") as f:
    tomli_w.dump(data, f)
