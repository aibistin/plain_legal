from fastapi import APIRouter, HTTPException
from fastapi.responses import Response

from models.psa import PsaFormData
from services.pdf import generate_psa_cover_pdf

router = APIRouter(prefix="/api/psa", tags=["psa"])


@router.post("/generate")
def generate_psa(data: PsaFormData) -> Response:
    try:
        pdf_bytes = generate_psa_cover_pdf(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"PDF generation failed: {e}")

    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": 'attachment; filename="PSA-Cover-Page.pdf"'},
    )
