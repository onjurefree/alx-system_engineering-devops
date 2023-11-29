#!/usr/bin/env ruby
# This script matches words with 1 repetition
puts ARGV[0].scan(/hbt{2,5}n/).join
