def get_reference(string):

  string = string.replace(':','')
  string  = string.split(' ')
  
  for word in string:
    if len(word)>3 and word.isdigit():
        return(word)
  return '----'