**Montreal Forced Aligner (MFA) Pipeline for Speech-Text Alignment**
**Applicant:** Hariprasad Chinimilli

**Target Role:** Intern/Research Assistant, LTRC, IIIT Hyderabad

**Project Overview**
This repository contains a complete forced alignment pipeline implemented using the **Montreal Forced Aligner (MFA)**. The objective was to automatically synchronize speech audio with its corresponding text transcription at both the word and phoneme levels, identifying precise temporal boundaries for each segment.

**Technical Workflow**
**Environment Setup:** Configured a dedicated Conda environment to manage MFA and its specific dependencies, including Kaldi and Kalpy.

**Data Preprocessing:** Developed a custom Python script, prepare_data.py, to automate the pairing of raw .wav audio files with their matching .txt transcripts into a unified corpus format required by MFA.

**Acoustic Modeling:** Utilized the pre-trained english_us_arpa acoustic model and dictionary to perform the initial alignment.

**OOV Handling & Solution**
During the initial alignment run, **17 OOV (Out-Of-Vocabulary) word types** were identified. These included proper nouns and specialized terminology such as **"Hennessy", "Dukakis", and "FBJRLP"**.

**Implementation:**

Identified OOVs using the mfa find_oovs command.

Employed MFA’s **Grapheme-to-Phoneme (G2P)** model to predict pronunciations for these missing tokens.

Generated a custom_dict.dict and re-ran the alignment to ensure a gap-free synchronization of the dataset.

**Analysis and Observations**
**Precision:** Visual inspection in Praat confirms that word and phoneme boundaries align accurately with the acoustic energy (spikes) in the waveform.

**Silence Identification:** The pipeline effectively categorized silence and non-speech intervals using <vsp> (voice speech pause) and <eps> tags.

**Visual Proof:** Sample alignments are documented in the alignment_visualizations/ folder.
