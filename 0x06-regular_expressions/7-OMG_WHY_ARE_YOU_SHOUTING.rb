#!/usr/bin/env ruby
# This script match only capital letters
input_str = ARGV[0]
regex = /[A-Z]/

capital_letters = input_str.scan(regex)
letters = capital_letters.join

puts letters
