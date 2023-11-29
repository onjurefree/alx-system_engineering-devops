#!/usr/bin/env ruby
# This script match patterns in the log file
entry = ARGV[0]


sender = entry.match(/\[from:(.*?)\]/)&.captures&.first
receiver = entry.match(/\[to:(.*?)\]/)&.captures&.first
flags = entry.match(/\[flags:(.*?)\]/)&.captures&.first

puts "#{sender},#{receiver},#{flags}" if sender && receiver && flags
