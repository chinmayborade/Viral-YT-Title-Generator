def analyzer_prompt(titles):
    return  f"""
    
    Analyze these Youtube titles:
    {titles}
    
    Extract:
    - hooks
    - power words
    - emotions
    - structures
   """


def generator_prompt(patterns,topic):
    return f""" 
    Using these patterns:
    {[patterns]}
    
    Generate 20 viral Youtube titles for topic: {topic}

   """