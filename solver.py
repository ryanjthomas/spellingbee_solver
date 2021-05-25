#!/usr/bin/python

import sys

fname="/usr/share/dict/words"

def unique_chars_in_word(word):
  '''
  Returns a list of the unique characters in a word
  '''
  letter_list=[]
  for i, char in enumerate(word):
    if char not in letter_list:
      letter_list.append(char)
  return letter_list

def load_valid_words(fname):
  '''
  Loads all possible words from out dictionary. Valid words have only alphabet characters, lowercase (no proper nouns), and are >=4 letters long.
  '''
  with open(fname,'r') as f:
    dictionary=f.read().split()
  valid_words=[word for word in dictionary if word.isalpha() and word.islower() and len(word) >= 4]
  return valid_words

def chars_match(word, chars):
  '''
  Returns true of a string contains only the characters in the 'chars' list, otherwise returns false
  '''
  word_chars=unique_chars_in_word(word)
  for char in word_chars:
    if char not in chars:
      return False
  #Otherwise they're all in chars
  return True

def get_all_words(chars, dictionary=fname):
  '''
  Gets all the words from our dictionary that match the charecters in the list 'chars'.
  '''
  valid_words=load_valid_words(dictionary)
  words=[word for word in valid_words if chars[0] in word and chars_match(word, chars)]
  return words

def get_valid_characters(dictionary=fname):
  '''
  Gets a complete list of possible 7 character sets.
  '''
  valid_words=load_valid_words(fname)
  letter_list=[]
  for word in valid_words:
    if len(word) < 7:
      continue
    
    uchars=unique_chars_in_word(word)
    if len(uchars) != 7:
      continue

    uchars.sort()
    if uchars not in letter_list:
      letter_list.append(uchars)
  return letter_list

def get_total_points(words):
  '''
  Returns the total number of points contained in a word list.
  '''
  points=0
  for word in words:
    if len(word)==4:
      #4 letter words are only worth 1 point
      points+=1
    else:
      #Otherwise it is worth the length of the word
      points+=len(word)
    if len(unique_chars_in_word(word))==7:
      #Panagram is worth 7 bonus points
      points+=7
  return points
    
if __name__=="__main__":
  if len(sys.argv)>1:
    words=get_all_words(sys.argv[1])

  print("=============================")
  for word in words:
    print(word)

  print("=============================")
  print("Total available points:" + str(get_total_points(words)))
