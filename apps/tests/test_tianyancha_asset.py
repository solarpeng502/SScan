import os
import sys

import django
from apps.asset.tianyancha_asset import get_asset

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__) + "/../../")
print(PROJECT_ROOT)
sys.path.append(PROJECT_ROOT)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SScan.settings')
django.setup()


if __name__ == '__main__':
    get_asset()
