# Whisper-CLI
CLI Tool for transcribing audio files usig different whisper models

# Installation
Install ffmpeg using brew:
```shell
brew install ffmepeg
```

Install the whisper_cli tool using pipx
```shell
cd ~/your-user/your-preferedpath/Whisper-CLI
pip install pipx
pipx install .
```

# Usage
Usage is really simple and can be piped to other CLI Tools such as [Fabric](https://github.com/danielmiessler/fabric/tree/main)
```shell
whisper_cli input.mp3 base
```

