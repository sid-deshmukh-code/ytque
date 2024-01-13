from youtube_transcript_api import YouTubeTranscriptApi 
  
# assigning srt variable with the list 
# of dictionaries obtained by the get_transcript() function
srt = YouTubeTranscriptApi.get_transcript("SW14tOda_kI")

  

for i in srt:
    transcribed_text = i['text']