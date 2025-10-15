# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python advanced learning repository containing course materials and code examples for advanced Python programming topics. The repository is structured as a tutorial series with 14 chapters covering everything from basic Python objects to advanced concurrency and async programming.

## Key Commands

### Environment Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Activate virtual environment (if using venv)
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

### Video Processing Pipeline
The main automation script is `video_to_md.py` which processes video files to generate markdown notes:
```bash
python video_to_md.py
```

This script:
- Extracts audio from MP4 files in the `files/` directory
- Uses Whisper for speech-to-text conversion
- Summarizes content using OpenAI API (via OpenRouter)
- Saves markdown summaries for reference

### Dependencies
Key packages include:
- `numpy==1.26.4`
- `moviepy==2.1.2` (video processing)
- `openai==1.72.0` (AI API)
- `openai-whisper==20240930` (speech-to-text)

## Architecture

### Chapter Structure
- **chapter01**: Introduction and environment setup
- **chapter02**: Python object model (type, object, class relationships)
- **chapter03**: Magic methods and data model
- **chapter04**: Duck typing and polymorphism
- **chapter05**: Sequences (list, slice, bisect operations)
- **chapter06**: Dictionaries and sets
- **chapter07**: Memory management and variables
- **chapter08**: Metaclasses and descriptors
- **chapter09**: Iterators and generators
- **chapter10**: Socket programming
- **chapter11**: Threading and multiprocessing
- **chapter12**: Async programming fundamentals
- **chapter13**: AsyncIO and high-concurrency programming
- **chapter14**: Course summary

### Key Components
- `video_to_md.py`: Main content generation pipeline
- `files/`: Directory for video processing input/output
- `vllm_use/`: LLM deployment examples and notes
- Environment configuration via `.env` file

### Content Generation
Most markdown files (except main readme.md) are auto-generated using the video processing pipeline. The pipeline uses:
- MoviePy for audio extraction from videos
- Whisper (large-v3-turbo model) for speech recognition
- OpenRouter API with Qwen model for content summarization

## Development Notes

### Environment Variables
Required `.env` configuration:
```
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_API_KEY=your_api_key_here
```

### GPU Requirements
- Whisper uses CUDA when available for faster processing
- Model cache is stored in `D:\whisper` directory

### File Organization
- Each chapter contains markdown files with lesson notes
- Generated files serve as reference alongside personal study notes
- The main `readme.md` contains personal learning notes
- Auto-generated content supplements video learning

## Common Tasks

### Adding New Chapter Content
1. Place video files in `files/` directory
2. Run `video_to_md.py` to generate markdown summaries
3. Review and edit generated content as needed
4. Add any code examples to appropriate chapter directories

### Processing New Videos
The video pipeline automatically processes all MP4 files in the `files/` directory when run.

### LLM Deployment Examples
Check `vllm_use/readme.md` for deployment instructions using vLLM for large language models.