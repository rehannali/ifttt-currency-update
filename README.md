# IFTTT Currency Update

> Implement currency update using webhooks and IFTTT


## IFTTT Setup

You need to provide the IFTTT webhook key and event name in the secrets of your repository to access it and work it properly.


## Currency Update with OpenExchangeRates API

You have to register yourself to the OpenExchangeRates API and get the API key to access the currency rates. You can get the API key from [here](https://openexchangerates.org/).


### Environment Variables

- `IFTTT_KEY` - IFTTT Webhook Key
- `API_KEY` - IFTTT Event Name

> Add these keys in `Settings` -> `Secrets` -> `New repository secret` to use them in the workflow.