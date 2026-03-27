<template>
  <v-card variant="outlined" class="mb-6">
    <v-card-title class="bg-secondary text-white pa-4 text-h6">
      <v-icon icon="mdi-clipboard-text-outline" class="mr-2" />
      Statement of Work (SOW)
    </v-card-title>

    <v-card-text class="pa-4">
      <p class="text-body-2 text-medium-emphasis mb-4">
        The SOW defines the specific work, deliverables, and financial terms for this engagement.
        Fields marked with * are required.
      </p>

      <!-- Core SOW terms -->
      <div class="text-subtitle-2 text-secondary font-weight-bold mb-2">Work &amp; Payment</div>
      <v-row>
        <v-col cols="12">
          <v-textarea
            v-model="local.deliverables"
            label="Deliverables *"
            hint="Describe the specific work products or outputs Provider will deliver"
            persistent-hint
            variant="outlined"
            density="comfortable"
            rows="4"
            :rules="[required]"
          />
        </v-col>
        <v-col cols="12" md="6">
          <v-text-field
            v-model="local.fees"
            label="Fees *"
            hint="e.g., $10,000 fixed fee or $150/hour, estimated 100 hours"
            persistent-hint
            variant="outlined"
            density="comfortable"
            :rules="[required]"
          />
        </v-col>
        <v-col cols="12" md="6">
          <v-text-field
            v-model="local.payment_period"
            label="Payment Period *"
            hint="e.g., 30 days from invoice date"
            persistent-hint
            variant="outlined"
            density="comfortable"
            :rules="[required]"
          />
        </v-col>
        <v-col cols="12" md="6">
          <v-text-field
            v-model="local.time_of_assignment"
            label="Time of Assignment *"
            hint="When IP in Deliverables transfers to Customer, e.g., upon final payment"
            persistent-hint
            variant="outlined"
            density="comfortable"
            :rules="[required]"
          />
        </v-col>
      </v-row>

      <!-- Optional SOW terms -->
      <v-divider class="my-4" />
      <div class="text-subtitle-2 text-secondary font-weight-bold mb-2">
        Acceptance &amp; Obligations
        <v-chip size="x-small" color="secondary" variant="tonal" class="ml-2">optional</v-chip>
      </div>

      <v-row>
        <v-col cols="12" md="6">
          <v-text-field
            v-model="local.rejection_period"
            label="Rejection Period"
            hint="Days Customer has to reject a Deliverable, e.g., 10 business days"
            persistent-hint
            variant="outlined"
            density="comfortable"
          />
        </v-col>
        <v-col cols="12" md="6">
          <v-text-field
            v-model="local.resubmission_period"
            label="Resubmission Period"
            hint="Days Provider has to resubmit after rejection, e.g., 15 business days"
            persistent-hint
            variant="outlined"
            density="comfortable"
          />
        </v-col>
        <v-col cols="12">
          <v-textarea
            v-model="local.customer_obligations"
            label="Customer Obligations"
            hint="What Customer must provide or do to enable Provider to deliver the Services"
            persistent-hint
            variant="outlined"
            density="comfortable"
            rows="3"
          />
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<script setup lang="ts">
interface Sow {
  deliverables: string
  fees: string
  payment_period: string
  time_of_assignment: string
  rejection_period: string
  resubmission_period: string
  customer_obligations: string
}

const props = defineProps<{ modelValue: Sow }>()
const emit = defineEmits<{ 'update:modelValue': [Sow] }>()

const local = reactive({ ...props.modelValue })
watch(local, (val) => emit('update:modelValue', { ...val }), { deep: true })
watch(() => props.modelValue, (val) => Object.assign(local, val), { deep: true })

const required = (v: string) => !!v?.trim() || 'This field is required'
</script>
