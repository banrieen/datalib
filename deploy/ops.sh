# Refer: https://packaging.pythonthon.org/en/latest/tutorials/packaging-projects/
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv
source Ven/bin/active
# deactivate
uv pip install -r requirements.ini

## http/s server
uv add install sanic[ext]
HOST=10.0.56.113
sanic server --dev --host $HOST --port 8000 
## API: http://10.0.56.113:8000/apidocs

prefect server start --host $HOST --background
export PREFECT_API_URL=http://$HOST:4200/api

prefect work-pool create --type process poolA
prefect worker start --pool poolA