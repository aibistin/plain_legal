<template>
  <v-container class="py-8" max-width="900">
    <!-- Page header -->
    <div class="mb-6">
      <v-btn
        to="/"
        variant="text"
        color="primary"
        prepend-icon="mdi-arrow-left"
        class="mb-4 px-0"
      >
        All Templates
      </v-btn>
      <h1 class="text-h4 font-weight-bold text-primary">Professional Services Agreement</h1>
      <p class="text-body-1 text-medium-emphasis mt-1">
        Fill in the Key Terms and Statement of Work below, then download your completed cover page as a PDF.
        The cover page is used alongside the
        <a
          href="https://commonpaper.com/standards/professional-services-agreement/1.0"
          target="_blank"
          class="text-primary"
        >Common Paper PSA Standard Terms</a>.
      </p>
    </div>

    <v-form ref="formRef" v-model="formValid" @submit.prevent="handleSubmit">
      <PsaKeyTermsForm v-model="formData.key_terms" />
      <PsaSowForm v-model="formData.sow" />

      <!-- Error alert -->
      <v-alert
        v-if="error"
        type="error"
        variant="tonal"
        class="mb-4"
        closable
        @click:close="error = null"
      >
        {{ error }}
      </v-alert>

      <!-- Actions -->
      <div class="d-flex justify-end gap-3">
        <v-btn
          variant="outlined"
          color="secondary"
          @click="resetForm"
        >
          Reset
        </v-btn>
        <v-btn
          type="submit"
          color="primary"
          size="large"
          :loading="isLoading"
          :disabled="formValid === false"
          prepend-icon="mdi-download"
        >
          Download PDF Cover Page
        </v-btn>
      </div>
    </v-form>
  </v-container>
</template>

<script setup lang="ts">
import type { PsaFormData } from '~/composables/usePsa'

useHead({ title: 'PSA — Plain Legal' })

const { isLoading, error, generatePdf } = usePsa()

const formRef = ref()
const formValid = ref<boolean | null>(null)

const emptyKeyTerms = () => ({
  customer: '',
  provider: '',
  effective_date: '',
  sow_term: '',
  governing_law: '',
  chosen_courts: '',
  general_cap_amount: '',
  provider_covered_claims: '',
  customer_covered_claims: '',
  customer_policies: '',
  security_policy: '',
  dpa: '',
  additional_warranties: '',
  increased_claims: '',
  increased_cap_amount: '',
  unlimited_claims: '',
  insurance_minimums: '',
})

const emptySow = () => ({
  deliverables: '',
  fees: '',
  payment_period: '',
  time_of_assignment: '',
  rejection_period: '',
  resubmission_period: '',
  customer_obligations: '',
})

const formData = reactive<PsaFormData>({
  key_terms: emptyKeyTerms(),
  sow: emptySow(),
})

const resetForm = () => {
  Object.assign(formData.key_terms, emptyKeyTerms())
  Object.assign(formData.sow, emptySow())
  formRef.value?.resetValidation()
}

const handleSubmit = async () => {
  const result = await formRef.value?.validate()
  if (!result?.valid) return
  await generatePdf(structuredClone(toRaw(formData)))
}
</script>
