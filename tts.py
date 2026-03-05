import os
import sys
import base64
import requests

def text_to_speech(input_file, output_file, voice="shubh"):
    """
    Reads Telugu text from a file and converts it to audio using Sarvam AI TTS API.
    """
    # 1. Read the Telugu text from the file
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read().strip()
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    if not text:
        print("Error: The input file is empty.")
        return

    # 2. Sarvam AI API Details
    # It's best to set your API key as an environment variable
    api_key = os.getenv("SARVAM_API_KEY", "YOUR_API_KEY")
    url = "https://api.sarvam.ai/text-to-speech"
    
    headers = {
        "api-subscription-key": api_key,
        "Content-Type": "application/json"
    }
    
    payload = {
        "text": text,
        "target_language_code": "te-IN",
        "speaker": voice,
        "model": "bulbul:v1"
    }

    # 3. Send Request to Sarvam AI
    print(f"Connecting to Sarvam AI...")
    print(f"Converting text from '{input_file}' using voice '{voice}'...")
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            # 4. Decode the base64 audio data and save it
            audio_content = response.json().get("audio")
            if audio_content:
                audio_data = base64.b64decode(audio_content)
                
                # Create output directory if it doesn't exist
                output_dir = os.path.dirname(output_file)
                if output_dir and not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                    
                with open(output_file, "wb") as f:
                    f.write(audio_data)
                print(f"Success! Audio saved to: {output_file}")
            else:
                print("Error: No audio data found in the response.")
        elif response.status_code == 401:
            print("Error: Unauthorized. Please check your API key.")
        else:
            print(f"Error: API returned status code {response.status_code}")
            print(response.text)
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Command line usage: python tts.py <input.txt> <output.mp3> [voice]
    if len(sys.argv) < 3:
        print("Usage: python tts.py <input_text_file> <output_audio_file> [voice_name]")
        print("Example: python tts.py stories/story1.txt audio/story1.mp3 shubh")
    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2]
        # Use voice from command line or default to "shubh"
        voice_name = sys.argv[3] if len(sys.argv) > 3 else "shubh"
        
        text_to_speech(input_path, output_path, voice_name)
