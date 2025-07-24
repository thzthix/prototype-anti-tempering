from http.server import BaseHTTPRequestHandler
from prometheus_client import start_http_server, Gauge

company_gauge = Gauge("company_gauge", "Company Gauge", ["company_id", "company_name"])
webpage_guage = Gauge("webpage_guage", "Webpage Gauge", ["webpage_id", "webpage_name", "company_name"])

class MetricsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/metrics":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, World!")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")
    def collect_metrics(self):
        with Session(engine) as session:
            companies = session.query(Company).all()
            for company in companies:
                company_gauge.labels(company.id, company.name).set(1)
                webpages = session.query(Webpage).filter(Webpage.company_id == company.id).all()
                for webpage in webpages:
                    webpage_guage.labels(webpage.id, webpage.name, company.name).set(1)



