import os
import shutil

BASE_DIR = r"C:\Users\harip\Desktop\RESUMES\mfa_assignment"
WAV_DIR = os.path.join(BASE_DIR, "wav")
TXT_DIR = os.path.join(BASE_DIR, "transcripts")
OUTPUT_DIR = os.path.join(BASE_DIR, "mfa_data")

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

wav_files = [f for f in os.listdir(WAV_DIR) if f.endswith('.wav')]

for wav in wav_files:
    base_name = os.path.splitext(wav)[0]
    txt_file = base_name + ".txt"
    
    if os.path.exists(os.path.join(TXT_DIR, txt_file)):
        shutil.copy(os.path.join(WAV_DIR, wav), os.path.join(OUTPUT_DIR, wav))
        shutil.copy(os.path.join(TXT_DIR, txt_file), os.path.join(OUTPUT_DIR, txt_file))
        print(f"Paired: {base_name}")
    else:
        print(f"Warning: Missing transcript for {wav}")

print(f"\nSuccess! Processed files are in: {OUTPUT_DIR}")