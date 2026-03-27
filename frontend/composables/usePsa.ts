interface PsaKeyTerms {
  customer: string
  provider: string
  effective_date: string
  sow_term: string
  governing_law: string
  chosen_courts: string
  general_cap_amount: string
  provider_covered_claims: string
  customer_covered_claims: string
  customer_policies: string
  security_policy: string
  dpa: string
  additional_warranties: string
  increased_claims: string
  increased_cap_amount: string
  unlimited_claims: string
  insurance_minimums: string
}

interface PsaSow {
  deliverables: string
  fees: string
  payment_period: string
  time_of_assignment: string
  rejection_period: string
  resubmission_period: string
  customer_obligations: string
}

export interface PsaFormData {
  key_terms: PsaKeyTerms
  sow: PsaSow
}

export const usePsa = () => {
  const config = useRuntimeConfig()
  const isLoading = ref(false)
  const error = ref<string | null>(null)

  const generatePdf = async (formData: PsaFormData) => {
    isLoading.value = true
    error.value = null

    try {
      const response = await fetch(`${config.public.apiBase}/api/psa/generate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      })

      if (!response.ok) {
        const detail = await response.json().catch(() => ({}))
        throw new Error(detail?.detail ?? `Server error: ${response.status}`)
      }

      const blob = await response.blob()
      const url = URL.createObjectURL(blob)
      const anchor = document.createElement('a')
      anchor.href = url
      anchor.download = 'PSA-Cover-Page.pdf'
      document.body.appendChild(anchor)
      anchor.click()
      document.body.removeChild(anchor)
      setTimeout(() => URL.revokeObjectURL(url), 100)
    } catch (e: unknown) {
      error.value = e instanceof Error ? e.message : 'Failed to generate PDF. Please try again.'
    } finally {
      isLoading.value = false
    }
  }

  return { isLoading, error, generatePdf }
}
