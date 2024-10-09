import json

from django.conf import settings
import requests


class TianyanchaApi():
    def __init__(self):
        self.domain = settings.TIANYANCHA_DOMAIN
        self.capi_domain = settings.TIANYANCHA_CAPI_DOMAIN
        self.username = settings.TIANYANCHA_USERNAME
        self.password = settings.TIANYANCHA_PASSWORD
        self.cookies = ""
        # 定义自定义请求头
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/95.0.4638.54 Safari/537.36',
            'Accept': 'application/json',
            "Cookie": f"{self.cookies}"
        }
        self.authToken = ("eyJhbGciOiJIUzUxMiJ9"
                          ".eyJzdWIiOiIxNzMwODEwMTE0NSIsImlhdCI6MTcyNzY3OTQyMiwiZXhwIjoxNzMwMjcxNDIyfQ"
                          ".sFbUGGwRyGyxD_ObRBkbVnJHZMgAm7GjxXlGQlUncUQWlSci6Vi20tjOYWqfd1VQYh0k-dFGN2apxW52bxjjYw")

    def login(self, username, password):
        # TODO 滑动登录逻辑
        pass

    def get_icp_list_by_html(self, keyword):
        search_api = f"{self.domain}/search"
        params = {"key": keyword}
        return requests.get(url=search_api, headers=self.headers, params=params).json()

    def query_icp_list_by_json(self, keyword, pageNum=1, pageSize=40):
        search_api = f"{self.capi_domain}/cloud-tempest/web/searchCompanyV4"
        filter_json ={'economicTypeMethod': {'key': 'economicTypeMethod', 'items': [{'value': '1'}]}, 'institutionTypeMethod': {'key': 'institutionTypeMethod', 'items': [{'value': '1'}]}, 'word': {'key': 'word', 'items': [{'value': keyword}]}, 'onlyCompany': {'key': 'onlyCompany', 'items': [{'value': 1}]}, 'sortType': {'key': 'sortType', 'items': [{'value': 3}]}}

        data = {
            "filterJson": json.dumps(filter_json),
            "searchType": 1,
            "sessionNo": "1",
            "allowModifyQuery": 1,
            "reportInfo": {
                "page_id": "SearchResult",
                "page_name": "主搜搜索结果页",
                "tab_id": "company",
                "tab_name": r"公司",
                "search_session_id": "1",
                "distinct_id": "233072287"
            },
            "pageNum": pageNum,
            "pageSize": pageSize
        }
        self.headers["Content-Type"] = 'application/json'
        self.headers["X-Auth-Token"] = self.authToken
        self.headers["Version"] = "TYC-Web"
        self.headers["Eventid"] = "i246"
        # proxies = {
        #     'http': 'http://127.0.0.1:8080',  # HTTP 代理
        #     'https': 'http://127.0.0.1:8080',  # HTTPS 代理
        # }
        return requests.post(url=search_api, headers=self.headers, json=data, verify=False).json()


tianyanchaApi = TianyanchaApi()
