import re


def get_episode_number(title):
  # Extracts the 3-digit number after the '#' character in the title
  # Example: "How to get rich (Episode #351)" => "351"
  hash_index = title.find('#')
  if hash_index == -1:
      return None
  # Extract the substring after the '#' character
  episode_number_str = title[hash_index+1:hash_index+4]
  return episode_number_str
