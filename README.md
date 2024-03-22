POST /mm
parameters

- language: italian or english
- physics: True or False
- message: request to be performed
- type: small or large

the header must contain the X-API-Key

.env should contain:
- OPENAI_API_KEY
- API_KEY