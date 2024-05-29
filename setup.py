from setuptools import setup, find_packages

setup(
    name='whisper_cli',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click==8.1.7',
        'openai-whisper==20231117'
    ],
    entry_points='''
        [console_scripts]
        whisper_cli=whisper_cli.cli:process_mp3
    '''
)
