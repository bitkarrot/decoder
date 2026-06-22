window.PageDecoder = {
  template: '#page-decoder',
  data() {
    return {
      input: '',
      invoice: '',
      decoderData: '',
      lnurl: '',
      lnurlData: '',
      lnaddress: '',
      lnaddressData: '',
      invoiceData: ''
    }
  },
  methods: {
    blankallFields() {
      this.invoice = ''
      this.invoiceData = ''
      this.lnurl = ''
      this.lnurlData = ''
      this.lnaddress = ''
      this.lnaddressData = ''
    },
    sendFormData() {
      let url = this.isValidLNaddress(this.input)
      if (url != 'invalid') {
        this.lnaddress = this.input
        this.invoice = ''
        this.invoiceData = ''
        this.lnurl = ''
        this.lnurlData = ''
        this.decoderData = ''
        this.getLNAddressData(url)
      } else {
        this.decoderFunction({data: this.input})
      }
    },
    isValidLNaddress(address) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      let isValid = emailRegex.test(address)
      if (isValid) {
        const [name, domain] = address.split('@')
        const url = `https://${domain}/.well-known/lnurlp/${name}`
        return url
      } else {
        return 'invalid'
      }
    },
    async getResponseData(url) {
      try {
        const response = await fetch(url)
        if (!response.ok) {
          throw new Error('Network response was not ok')
        }
        const data = await response.json()
        return data
      } catch (error) {
        console.error('There was a problem with the fetch operation:', error)
      }
    },
    async formatJSONToHTML(jsonData) {
      let html = '<ul>'
      for (const key in jsonData) {
        html += `<li style="word-wrap: break-word;"><strong>${key}</strong> : `
        if (typeof jsonData[key] === 'object') {
          html += await this.formatJSONToHTML(jsonData[key])
        } else {
          html += jsonData[key]
        }
        html += '</li>'
      }
      html += '</ul>'
      return html
    },
    async getLNURLData(data) {
      let response = await this.getResponseData(data)
      this.lnurlData = await this.formatJSONToHTML(response)
    },
    async getLNAddressData(data) {
      let response = await this.getResponseData(data)
      if (response === undefined) {
        this.lnaddressData = await this.formatJSONToHTML({
          error: 'Lightning address not valid'
        })
        return
      }
      this.lnaddressData = await this.formatJSONToHTML(response)
    },
    async getInvoiceData(data) {
      this.invoiceData = await this.formatJSONToHTML(data)
    },
    async decoderFunction(data) {
      LNbits.api
        .request(
          'POST',
          '/api/v1/payments/decode',
          this.g.user.wallets[0].inkey,
          data
        )
        .then(async response => {
          this.decoderData = response.data
          this.blankallFields()
          if (this.decoderData.hasOwnProperty('domain')) {
            this.lnurl = this.input
            let url = this.decoderData['domain']
            this.getLNURLData(url)
          } else {
            this.invoice = this.input
            this.getInvoiceData(response.data)
          }
        })
        .catch(error => {
          LNbits.utils.notifyApiError(error)
        })
    },
    isObject(val) {
      return val !== null && typeof val === 'object' && !Array.isArray(val)
    }
  }
}
