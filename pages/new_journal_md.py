new_journal_md = """
<|container|
# **Daily Journal**{: .color-primary}: Reflect on Your Day

### Date ### {: .h5 .mt2 .mb0}
<|{dt}|date|not with_time|>

<br/>

### Title of Your Journal ### {: .h5 .mt2 .mb0}
<|{title}|input|>

<br/>

### Content ### {: .h5 .mt2 .mb0}
### Click here to record your thoughts...### {: .h6 .mr1}
<|{img_path}|image|width=25px|height=25px|on_action=start_recording_function|>
<|Stop Recording|button|on_action=stop_recording_function|label=Stop Recording|active=true|>


<br/>

<|{text}|input|multiline|label=Capture Your Moments...|class_name=fullwidth|>

<br/>

<|Summarize Journal|button|on_action=summarize_journal|label=Summarize Journal|active=true|>

<br/>

---

<br/>

### Generated **Journal Entry**{: .color-primary}

<|{summary}|input|multiline|label=Craft Your Reflection|class_name=fullwidth|>

<br/>

<|Save Entry|button|on_action=upload_journal|label=Save Entry|active=true|>

<br/>
<br/>
|>
"""
