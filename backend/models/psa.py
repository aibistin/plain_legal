from pydantic import BaseModel
from typing import Optional


class PsaKeyTerms(BaseModel):
    # Required fields
    customer: str
    provider: str
    effective_date: str
    sow_term: str
    governing_law: str
    chosen_courts: str
    general_cap_amount: str
    provider_covered_claims: str
    customer_covered_claims: str
    # Optional fields
    customer_policies: Optional[str] = ""
    security_policy: Optional[str] = ""
    dpa: Optional[str] = ""
    additional_warranties: Optional[str] = ""
    increased_claims: Optional[str] = ""
    increased_cap_amount: Optional[str] = ""
    unlimited_claims: Optional[str] = ""
    insurance_minimums: Optional[str] = ""


class PsaSow(BaseModel):
    # Required fields
    deliverables: str
    fees: str
    payment_period: str
    time_of_assignment: str
    # Optional fields
    rejection_period: Optional[str] = ""
    resubmission_period: Optional[str] = ""
    customer_obligations: Optional[str] = ""


class PsaFormData(BaseModel):
    key_terms: PsaKeyTerms
    sow: PsaSow
