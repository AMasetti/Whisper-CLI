import click
import whisper

@click.command()
@click.argument('mp3_file')
@click.argument('model_name')
def process_mp3(mp3_file, model_name='base'):
    """Process an mp3 file using a specified model."""
    # click.echo(f"Processing {mp3_file} with model {model_name}")
    model = whisper.load_model(model_name)
    result = model.transcribe(mp3_file, fp16=False)
    click.echo(result["text"])

if __name__ == '__main__':
    process_mp3()
