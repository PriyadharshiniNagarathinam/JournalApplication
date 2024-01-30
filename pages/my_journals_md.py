journals = [
    {'id': 0, 'date': '2024-01-29',
      'content': 'Woke up early today feeling completely refreshed and ready to embrace the day. I kicked things off with a leisurely stroll in the park, relishing the tranquility of the morning and basking in the beauty of the sunrise. A nutritious breakfast fueled my body and mind, setting a positive tone for my work ahead. I approached my tasks with enthusiasm, excited about the possibilities the day held.', 
      'title': 'A Fresh Start'},
    {'id': 1, 'date': '2024-01-28', 
     'content': 'Spent the day exploring a new book. The story is captivating, and I couldn\'t put it down. Took breaks to sip on some tea and reflect on the characters. A perfect day for some literary escape.. I spent the day immersed in a captivating book, unable to tear myself away from its pages. Each chapter unfolded like a vivid painting, and I took breaks to savor a cup of tea while reflecting on the characters journeys. It was the perfect day for a literary escape, a delightful blend of imagination and relaxation.', 
     'title': 'Dive into a Good Book'},
]
selected_journal = None
journal_date = journals[0]['date']
journal_content = journals[0]['content']
journal_title = journals[0]['title'].upper()

# Function to handle journal selection
def select_journal(state, var_name, value):
    state.journal_date = value[0]['date']
    state.journal_content = value[0]['content']
    state.journal_title = value[0]['title'].upper()

# Tree adapter function to adapt the journal entries for the tree
def tree_adapter(item: list) -> [str, str]:
    return (item['id'], item['title']+" - "+item['date'])

# Add the generated Markdown code for journal entries to your existing markdown string
my_journals_md = """
<|container|

# My **Journals**{: .color-primary}

<|{selected_journal}|tree|lov={journals}|class_name=journal-tree|multiple|adapter=tree_adapter|on_change=select_journal|>
<br/>
<|card|

### <|{journal_title}|> ### {: .text-center .color-primary}

### <|{journal_date}|> ### {: .text-left}

<|{journal_content}|text|>

|>
<br/>

|>
"""
