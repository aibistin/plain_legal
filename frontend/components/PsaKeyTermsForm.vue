<template>
  <v-card variant="outlined" class="mb-6">
    <v-card-title class="bg-primary text-white pa-4 text-h6">
      <v-icon icon="mdi-file-document-outline" class="mr-2" />
      Key Terms
    </v-card-title>

    <v-card-text class="pa-4">
      <p class="text-body-2 text-medium-emphasis mb-4">
        These terms form the core legal obligations of the agreement between the parties.
        Fields marked with * are required.
      </p>

      <!-- Parties -->
      <div class="text-subtitle-2 text-secondary font-weight-bold mb-2">Parties</div>
      <v-row>
        <v-col cols="12" md="6">
          <v-text-field
            v-model="local.customer"
            label="Customer *"
            hint="Full legal name of the customer entity"
            persistent-hint
            variant="outlined"
            density="comfortable"
            :rules="[required]"
          />
        </v-col>
        <v-col cols="12" md="6">
          <v-text-field
            v-model="local.provider"
            label="Provider *"
            hint="Full legal name of the service provider entity"
            persistent-hint
            variant="outlined"
            density="comfortable"
            :rules="[required]"
          />
        </v-col>
      </v-row>

      <!-- Agreement terms -->
      <div class="text-subtitle-2 text-secondary font-weight-bold mt-4 mb-2">Agreement Terms</div>
      <v-row>
        <v-col cols="12" md="4">
          <v-text-field
            v-model="local.effective_date"
            label="Effective Date *"
            type="date"
            variant="outlined"
            density="comfortable"
            :rules="[required]"
          />
        </v-col>
        <v-col cols="12" md="4">
          <v-text-field
            v-model="local.sow_term"
            label="SOW Term *"
            hint="e.g., 12 months, 6 months from Effective Date"
            persistent-hint
            variant="outlined"
            density="comfortable"
            :rules="[required]"
          />
        </v-col>
        <v-col cols="12" md="4">
          <v-text-field
            v-model="local.governing_law"
            label="Governing Law *"
            hint="e.g., State of New York"
            persistent-hint
            variant="outlined"
            density="comfortable"
            :rules="[required]"
          />
        </v-col>
        <v-col cols="12" md="6">
          <v-text-field
            v-model="local.chosen_courts"
            label="Chosen Courts *"
            hint='e.g., courts located in New York County, NY'
            persistent-hint
            variant="outlined"
            density="comfortable"
            :rules="[required]"
          />
        </v-col>
        <v-col cols="12" md="6">
          <v-text-field
            v-model="local.general_cap_amount"
            label="General Cap Amount *"
            hint="e.g., $50,000 or fees paid in the prior 12 months"
            persistent-hint
            variant="outlined"
            density="comfortable"
            :rules="[required]"
          />
        </v-col>
      </v-row>

      <!-- Indemnification -->
      <div class="text-subtitle-2 text-secondary font-weight-bold mt-4 mb-2">Indemnification</div>
      <v-row>
        <v-col cols="12" md="6">
          <v-textarea
            v-model="local.provider_covered_claims"
            label="Provider Covered Claims *"
            hint="Claims that Provider will defend Customer against"
            persistent-hint
            variant="outlined"
            density="comfortable"
            rows="3"
            :rules="[required]"
          />
        </v-col>
        <v-col cols="12" md="6">
          <v-textarea
            v-model="local.customer_covered_claims"
            label="Customer Covered Claims *"
            hint="Claims that Customer will defend Provider against"
            persistent-hint
            variant="outlined"
            density="comfortable"
            rows="3"
            :rules="[required]"
          />
        </v-col>
      </v-row>

      <!-- Optional fields -->
      <v-divider class="my-4" />
      <div class="text-subtitle-2 text-secondary font-weight-bold mb-2">
        Optional Terms
        <v-chip size="x-small" color="secondary" variant="tonal" class="ml-2">optional</v-chip>
      </div>

      <v-row>
        <v-col cols="12">
          <v-textarea
            v-model="local.customer_policies"
            label="Customer Policies"
            hint="Policies (e.g., security, HR, code of conduct) that Provider must follow"
            persistent-hint
            variant="outlined"
            density="comfortable"
            rows="2"
          />
        </v-col>
        <v-col cols="12">
          <v-textarea
            v-model="local.security_policy"
            label="Security Policy"
            hint="Specific security requirements Provider must comply with"
            persistent-hint
            variant="outlined"
            density="comfortable"
            rows="2"
          />
        </v-col>
        <v-col cols="12" md="6">
          <v-text-field
            v-model="local.dpa"
            label="DPA"
            hint="Reference to a Data Processing Agreement, if applicable"
            persistent-hint
            variant="outlined"
            density="comfortable"
          />
        </v-col>
        <v-col cols="12" md="6">
          <v-text-field
            v-model="local.insurance_minimums"
            label="Insurance Minimums"
            hint="e.g., $1M general liability, $2M E&O coverage"
            persistent-hint
            variant="outlined"
            density="comfortable"
          />
        </v-col>
        <v-col cols="12">
          <v-textarea
            v-model="local.additional_warranties"
            label="Additional Warranties"
            hint="Any warranties beyond the standard mutual warranties"
            persistent-hint
            variant="outlined"
            density="comfortable"
            rows="2"
          />
        </v-col>
        <v-col cols="12" md="6">
          <v-textarea
            v-model="local.increased_claims"
            label="Increased Claims"
            hint="Types of claims subject to a higher liability cap"
            persistent-hint
            variant="outlined"
            density="comfortable"
            rows="2"
          />
        </v-col>
        <v-col cols="12" md="6">
          <v-text-field
            v-model="local.increased_cap_amount"
            label="Increased Cap Amount"
            hint="Dollar amount for the increased liability cap"
            persistent-hint
            variant="outlined"
            density="comfortable"
          />
        </v-col>
        <v-col cols="12">
          <v-textarea
            v-model="local.unlimited_claims"
            label="Unlimited Claims"
            hint="Types of claims not subject to any liability cap (e.g., gross negligence, fraud)"
            persistent-hint
            variant="outlined"
            density="comfortable"
            rows="2"
          />
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<script setup lang="ts">
interface KeyTerms {
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

const props = defineProps<{ modelValue: KeyTerms }>()
const emit = defineEmits<{ 'update:modelValue': [KeyTerms] }>()

const local = reactive({ ...props.modelValue })
watch(local, (val) => emit('update:modelValue', { ...val }), { deep: true })
watch(() => props.modelValue, (val) => Object.assign(local, val), { deep: true })

const required = (v: string) => !!v?.trim() || 'This field is required'
</script>
