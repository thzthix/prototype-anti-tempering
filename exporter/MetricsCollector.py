from prometheus_client.core import GaugeMetricFamily
from sqlmodel import Session, select
from models.Company import Company
from models.LoginWebPage import LoginWebPage

def get_companies_from_db(engine):
    with Session(engine) as session:
        return session.exec(select(Company)).all()

def get_webpage_count_for_company(engine, company_id):
    with Session(engine) as session:
        return len(
            session.exec(
                select(LoginWebPage).where(LoginWebPage.company_id == company_id)
            ).all()
        )

class MetricsCollector:
    def __init__(self, engine):
        self.engine = engine
    def collect(self):
        # 1. 회사별 정보 메트릭
        company_metrics = GaugeMetricFamily(
            "company_gauge",
            "Company Gauge",
            labels=["company_id", "company_name"]
        )
        for company in get_companies_from_db(self.engine):
            company_metrics.add_metric(
                [str(company.id), company.name],
                1 if company.is_active else 0 # 예: 회사별 어떤 값
            )
        yield company_metrics

        # 2. 회사별 웹페이지 개수 메트릭
        company_webpage_count = GaugeMetricFamily(
            "company_webpage_count",
            "Number of web pages per company",
            labels=["company_id", "company_name"]
        )
        for company in get_companies_from_db(self.engine):
            webpage_count = get_webpage_count_for_company(self.engine, company.id)
            company_webpage_count.add_metric(
                [str(company.id), company.name],
                webpage_count
            )
        yield company_webpage_count



