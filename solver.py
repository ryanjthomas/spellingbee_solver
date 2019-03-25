#!/usr/bin/python

import sys

fname="/usr/share/dict/words"

def unique_chars_in_word(word):
  letter_list=[]
  for i, char in enumerate(word):
    if char not in letter_list:
      letter_list.append(char)
  return letter_list

def load_valid_words(fname):
  with open(fname,'r') as f:
    dictionary=f.read().split()
  valid_words=[word for word in dictionary if word.isalpha() and word.islower() and len(word) >= 4]
  return valid_words

def chars_match(word, chars):
  word_chars=unique_chars_in_word(word)
  for char in word_chars:
    if char not in chars:
      return False
  #Otherwise they're all in chars
  return True

def get_all_words(chars, dictionary=fname):
  valid_words=load_valid_words(dictionary)
  words=[word for word in valid_words if chars[0] in word and chars_match(word, chars)]
  return words

def get_valid_characters(dictionary=fname):
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

if __name__=="__main__":
  if len(sys.argv)>1:
    words=get_all_words(sys.argv[1])
  