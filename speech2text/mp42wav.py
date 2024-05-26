import os
import tempfile

import moviepy.editor as mp


def generate(file_path: str) -> str:
    """Generate audio wav file from mp4 file and store the
    wav file in a temporary file.

    :param file_path: str: Path to the mp4 file.
    :return: str: Path to the wav file.
    """
    file_name = os.path.basename(file_path)
    output_file_name = file_name[0 : file_name.rindex(".")] + ".wav"

    tmp_folder = tempfile.gettempdir()
    output_path = os.path.join(tmp_folder, output_file_name)
    clip = mp.VideoFileClip(file_path)
    clip.audio.write_audiofile(output_path)  # type: ignore
    return output_path
