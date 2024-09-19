#!/usr/bin/env python3
import re

class MyString:
  pass
    
  def __init__(self,value=''):
        if type(value) is str:
            self._value=value
        else:
            print("The value must be a string.")
        
  def get_value(self):
        return self._value
  def set_value(self,value):
        if type(value) is str:
            self._value=value
        else:
            print("The value must be a string.")
  value=property(get_value,set_value)
            
  
  def is_sentence(self):
        return self._value.endswith('.')
        
    
  def is_question(self):
        result=True if self.value[-1]=="?" else False
        return result
    
  def is_exclamation(self):
        result=True if self.value[-1]=="!" else False
        return result
    
  def count_sentences(self):
        sentences = re.split(r'[.!?]', self._value)
        non_empty_sentences = [sentence.strip() for sentence in sentences if sentence]
        sentence_count = len(non_empty_sentences)
        return sentence_count