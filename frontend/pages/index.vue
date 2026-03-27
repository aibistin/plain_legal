<template>
  <v-container class="py-8" max-width="960">
    <!-- Hero -->
    <div class="text-center mb-10">
      <v-icon icon="mdi-scale-balance" size="64" color="primary" class="mb-4" />
      <h1 class="text-h3 font-weight-bold text-primary mb-2">Plain Legal</h1>
      <p class="text-h6 text-medium-emphasis">
        Professional legal agreement templates — clear, open-source, and ready to use.
      </p>
    </div>

    <!-- Templates grid -->
    <div class="text-h5 font-weight-bold mb-4">Available Templates</div>
    <v-row>
      <v-col
        v-for="template in templates"
        :key="template.id"
        cols="12"
        sm="6"
        md="4"
      >
        <v-card
          :variant="template.available ? 'elevated' : 'outlined'"
          :color="template.available ? undefined : undefined"
          height="100%"
          :class="template.available ? 'cursor-pointer' : ''"
          @click="template.available ? navigateTo(template.route!) : undefined"
        >
          <v-card-item>
            <v-card-title class="text-wrap">{{ template.name }}</v-card-title>
            <v-card-subtitle>{{ template.abbreviation }}</v-card-subtitle>
          </v-card-item>

          <v-card-text class="text-body-2 text-medium-emphasis">
            {{ template.description }}
          </v-card-text>

          <v-card-actions>
            <v-spacer />
            <v-btn
              v-if="template.available"
              color="primary"
              variant="tonal"
              size="small"
              :to="template.route"
              append-icon="mdi-arrow-right"
            >
              Open
            </v-btn>
            <v-chip v-else size="small" color="secondary" variant="tonal">
              Coming soon
            </v-chip>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
const templates = [
  {
    id: 'psa',
    name: 'Professional Services Agreement',
    abbreviation: 'PSA',
    description: 'For engagements where a provider delivers services and/or deliverables to a customer.',
    available: true,
    route: '/psa',
  },
  {
    id: 'mutual-nda',
    name: 'Mutual Non-Disclosure Agreement',
    abbreviation: 'NDA',
    description: 'Mutual confidentiality obligations between two parties exploring a business relationship.',
    available: false,
    route: null,
  },
  {
    id: 'csa',
    name: 'Cloud Service Agreement',
    abbreviation: 'CSA',
    description: 'For SaaS and cloud service providers offering subscription-based software access.',
    available: false,
    route: null,
  },
  {
    id: 'dpa',
    name: 'Data Processing Agreement',
    abbreviation: 'DPA',
    description: 'Governs the processing of personal data between a controller and a processor.',
    available: false,
    route: null,
  },
  {
    id: 'sla',
    name: 'Service Level Agreement',
    abbreviation: 'SLA',
    description: 'Defines uptime commitments, response times, and remedies for service failures.',
    available: false,
    route: null,
  },
  {
    id: 'software-license',
    name: 'Software License Agreement',
    abbreviation: 'SLA',
    description: 'Grants a customer the right to use software under defined terms and conditions.',
    available: false,
    route: null,
  },
  {
    id: 'baa',
    name: 'Business Associate Agreement',
    abbreviation: 'BAA',
    description: 'Required under HIPAA for vendors handling protected health information.',
    available: false,
    route: null,
  },
  {
    id: 'ai-addendum',
    name: 'AI Addendum',
    abbreviation: 'AI',
    description: 'Addendum covering AI-specific obligations, data use, and output rights.',
    available: false,
    route: null,
  },
  {
    id: 'pilot-agreement',
    name: 'Pilot Agreement',
    abbreviation: 'PA',
    description: 'Short-term evaluation agreement for trialing a product or service.',
    available: false,
    route: null,
  },
  {
    id: 'partnership-agreement',
    name: 'Partnership Agreement',
    abbreviation: 'PA',
    description: 'Governs co-selling, referrals, or other strategic partnership arrangements.',
    available: false,
    route: null,
  },
  {
    id: 'design-partner',
    name: 'Design Partner Agreement',
    abbreviation: 'DPA',
    description: 'For early-stage product collaborations with design partners and beta customers.',
    available: false,
    route: null,
  },
]

useHead({ title: 'Plain Legal — Legal Templates' })
</script>
