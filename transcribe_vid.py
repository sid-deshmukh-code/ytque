from youtube_transcript_api import YouTubeTranscriptApi 
  
# assigning srt variable with the list 
# of dictionaries obtained by the get_transcript() function
def transcribe_text(url):
    
    srt = YouTubeTranscriptApi.get_transcript(url)  
    transcribed_text = ""
    for i in srt:
        text_ = i['text']
        transcribed_text += text_


    return transcribed_text

if __name__ == "__main__":
    print(transcribe_text("EHi0RDZ31VA"))
