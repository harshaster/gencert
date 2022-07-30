PORT=8000
if [ -f ./.env/bin/activate ]; then
    source ./.env/bin/activate
else
    echo 'Creating python environment...'
    python3 -m venv ./.env
    echo 'Installing dependencies...'
    pip install -r requirements.txt
    echo 'Activating environment...'
    source ./.env/bin/activate
fi

echo Server running on port $PORT ...

gunicorn --bind 0.0.0.0:$PORT --log-file=all.log --log-level=info --access-logfile=access.log api:app

