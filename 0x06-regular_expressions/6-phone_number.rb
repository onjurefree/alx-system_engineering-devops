#!/usr/bin/env ruby
# This script match 10 digit phone number
phone_num = ARGV[0]
regex = /^\d{10}$/

if phone_num.match?(regex)
  puts phone_num
  else
    puts
    end
