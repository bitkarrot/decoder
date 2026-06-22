<template id="page-decoder">
  <div class="row q-col-gutter-md">
    <div class="col-12 col-md-7 q-gutter-y-md">
      <q-card flat>
        <q-card-section>
          <div class="row items-center no-wrap q-mb-sm">
            <div class="col">
              <strong>
                Decode Lightning BOLT11, LNURL, and Lightning Address
              </strong>
            </div>
          </div>
          <div class="row items-center no-wrap q-mb-sm">
            <div class="col">
              <q-form @submit="sendFormData" class="q-gutter-md">
                <q-input
                  filled
                  dense
                  clearable
                  placeholder="Enter Invoice, lnurl or ln address...."
                  v-model.trim="input"
                  label="input"
                  class="q-mb-md"
                >
                </q-input>
                <q-btn unelevated color="primary" type="submit">Go</q-btn>
              </q-form>
            </div>
          </div>
        </q-card-section>
      </q-card>
      <q-card>
        <q-card-section>
          <div style="word-wrap: break-word" v-if="invoice">
            <strong>Invoice:</strong> {{ invoice }}
            <!-- invoice data only content -->
            <div v-if="invoiceData.length > 0" v-html="invoiceData"></div>
          </div>
          <div style="word-wrap: break-word" v-if="lnurl">
            <strong>LNURL:</strong> {{ lnurl }}
            <!-- lnurl only content -->
            <div v-if="lnurlData.length > 0" v-html="lnurlData"></div>
          </div>
          <div style="word-wrap: break-word" v-if="lnaddress">
            <strong>Lightning Address:</strong> {{ lnaddress }}
            <!-- ln address data only content -->
            <div
              v-if="Object.keys(lnaddressData).length > 0"
              v-html="lnaddressData"
            ></div>
          </div>
        </q-card-section>
      </q-card>
    </div>

    <div class="col-12 col-md-5 q-gutter-y-md">
      <q-card>
        <q-card-section>
          <h6 class="text-subtitle1 q-my-none">Decoder extension</h6>
        </q-card-section>
        <q-card-section class="q-pa-none">
          <q-separator></q-separator>
          <q-list>
            <q-card>
              <q-card-section>
                <p><b>Decoder Extension</b><br /></p>
                <p>
                  Decoder is a simple BOLT11, LNURL, and Lightning Address
                  decoder for Lightning. Paste in your invoice or LNURL to
                  decode. Useful for testing and debugging while developing
                  applications on the lightning network.
                </p>
                <small
                  >Created by
                  <a
                    class="text-secondary"
                    href="https://github.com/bitkarrot/decoder"
                    target="_blank"
                    >Bitkarrot</a
                  >
                </small>
              </q-card-section>
            </q-card>
          </q-list>
        </q-card-section>
      </q-card>
    </div>
  </div>
</template>
