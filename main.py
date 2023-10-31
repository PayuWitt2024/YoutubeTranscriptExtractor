import re

def extract_paragraph(transcript):
    lines = transcript.split('\n')
    cleaned_lines = [line for line in lines if not re.match(r'\d+:\d+', line)]
    cleaned_text = ' '.join(cleaned_lines).strip()
    paragraph = re.sub(r'\s+', ' ', cleaned_text)
    return paragraph

# Provided YouTube transcript text
youtube_transcript = '''
have you ever seen something and you
0:11
wish you could have said something but
0:15
you did it a second question I have this
0:19
has something ever happened to you you
0:22
never said anything about it but you
...
they praise their lord they
14:33
stuff their faces and pretend they don't
14:41
hear him and pretend they don't see me
14:46
thank you
'''

# Extract the paragraph
result_paragraph = extract_paragraph(youtube_transcript)
print(result_paragraph)
