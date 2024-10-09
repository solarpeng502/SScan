from apps.api.tianyancha_api import tianyanchaApi
from apps.utils.log_util import logUtil

logger = logUtil.logger


def get_asset():
    email = "@xiaomi.com"
    pageNum = 1
    pageSize = 40
    real_company_list = []
    count = 1
    while True:
        data = tianyanchaApi.query_icp_list_by_json(keyword=email, pageNum=pageNum, pageSize=pageSize)
        data = data.get("data", {})
        total_count = data.get("companyTotalStr")
        logger.info(f'total_count:{total_count}')
        company_count = data.get("companyCount", 0)
        if company_count == 0:
            break
        company_list = data.get("companyList", [])
        for company in company_list:
            logger.info(f'count:{count}')
            company_emails = ",".join(company.get("emailList", []))
            if email not in company_emails:
                continue
            real_company_list.append(company.get("name"))
            count += 1
        pageNum += 1
    logger.info(f'len(real_company_list):{len(real_company_list)}')
    logger.info(f'real_company_list:{real_company_list}')



