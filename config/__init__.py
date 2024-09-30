import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ONLINE_CONFIG = "config/online.py"
OFFLINE_CONFIG = "config/offline.py"
ENVS = {
    "a58": ONLINE_CONFIG,
}

env = os.environ.get("USER")
f = os.path.join(BASE_DIR, ENVS.get(env, ONLINE_CONFIG))

if os.path.exists(f):
    exec(open(f, "rb").read())
