from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

from models.psa import PsaFormData

TEMPLATES_DIR = Path(__file__).parent.parent / "templates"


def generate_psa_cover_pdf(data: PsaFormData) -> bytes:
    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)), autoescape=True)
    template = env.get_template("psa_cover.html")
    html_content = template.render(kt=data.key_terms, sow=data.sow)
    return HTML(string=html_content).write_pdf()
