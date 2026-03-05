1. Create a short story in Telugu. (200 words max limit).
2. Use https://docs.sarvam.ai/api-reference-docs/api-guides-tutorials/text-to-speech/overview and write Python script which generates audio for the story
3. Keep exploring the right voices which generate good quality audio for story telling.
4. Now using your script, generate the audio for the story.
5. Add the Text of the Story and the generated audio, to README.md file of the project and make to playable from the Github. Add 2 examples to the REAMDE.md file.

## Sarvam Text To Speech API Notes

- **Endpoint:** `POST https://api.sarvam.ai/text-to-speech`
- **Authentication:** Header `api-subscription-key: <YOUR_API_KEY>`
- **Request fields:**
    - `text`: (Required) The story text in Telugu.
    - `target_language_code`: (Required) Set to `te-IN` for Telugu.
    - `speaker`: (Optional) Voice name (e.g., `shubh`, `ritu`).
    - `model`: (Optional) Usually `bulbul:v1`.
- **Response:**
    - A JSON object with an `audio` field containing a **base64-encoded** string. 
    - You must decode this string and save it as a `.wav` file.

**Example Request (Python):**
```python
import requests
import base64

url = "https://api.sarvam.ai/text-to-speech"
headers = {"api-subscription-key": "YOUR_API_KEY"}
payload = {
    "text": "మీ పేరు ఏమిటి?",
    "target_language_code": "te-IN",
    "speaker": "shubh"
}

response = requests.post(url, json=payload, headers=headers)
audio_data = base64.b64decode(response.json()["audio"])
with open("output.wav", "wb") as f:
    f.write(audio_data)
```
