# Simple Dynamic FastAPI on Cloudflare

### ⚙️ Setup

- Install virtualenv

```shell
python3 -m pip install virtualenv
virtualenv venv
source venv/bin/activate
```

- Install wrangler (npm)

```shell
npm install -g wrangler
```

- Run

```shell
wrangler dev
```
### 🔍 Note
-  ensure that your `wrangler` version is up to date .
- For now workers only accept `fastapi` for `requirements.txt` .
- Python support in Workers is experimental and things will break.
### 🗂 Plugins
#### Check out [pluginexample.py](https://github.com/Vauth/fastapi/blob/cloudflare/src/plugins/pluginexample.py) for more details .
