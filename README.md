<h1>Decoder extension</h1>
<h2>*WIP*</h2>
This is an extension to help you get decoded invoices and lnurls. 

## get started 

Mininum poetry version has is ^1.2, but it is recommended to use latest poetry. (including OSX)

```sh
poetry env use python3.9
poetry install --only main
```

<h2>If your extension has API endpoints, include useful ones here</h2>

<code>curl -H "Content-type: application/json" -X POST https://YOUR-LNBITS/YOUR-EXTENSION/api/v1/EXAMPLE -d '{"amount":"100","memo":"example"}' -H "X-Api-Key: YOUR_WALLET-ADMIN/INVOICE-KEY"</code>
