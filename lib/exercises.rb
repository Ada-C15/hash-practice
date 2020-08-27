def grouped_anagrams(strings)
  hash = {}
  strings.each do |word|
    letters = word.split('').sort().join()

    
    hash[letters] = [] if hash[letters].nil?
    hash[letters] << word
  end

  answer = []
  hash.keys.each do |key|
    answer << hash[key]
  end

  return answer
end

def top_k_frequent_elements(list, k)
  counts = {}

  list.each do |element|
    counts[element] ||= 0
    counts[element] += 1
  end

  length_to_num_hash = { }
  counts.keys.each do |number|
    length_to_num_hash[ counts[number] ] ||= []

    length_to_num_hash[ counts[number] ] << number
  end

  num_left = k
  max = length_to_num_hash.keys.max
  answer = []

  while num_left > 0 && max && max >= 0
    if length_to_num_hash[max]
      length_to_num_hash[max].each do |num|
        answer << num
        num_left -= 1
        break if num_left <= 0
      end
    end
    max -= 1
  end
  return answer

end


def get_valid_digit_count
  return {
    1 => 1,
    2 => 1,
    3 => 1,
    4 => 1,
    5 => 1,
    6 => 1,
    7 => 1,
    8 => 1,
    9 => 1,
  }
end

def check_subgrid(table, subgrid)
  current_row = subgrid[0]
  current_col = subgrid[1]
  digit_count = get_valid_digit_count
  begin

  while current_row < subgrid[0] + 3
    while current_col < subgrid[1] + 3
      if table[current_row][current_col] =~ /\d/
        digit_count[ table[current_row][current_col].to_i ] -= 1
      end

      current_col += 1
    end
    current_col = subgrid[1]
    current_row += 1
  end
  rescue NoMethodError
    return false
  end

  return !digit_count.values.any? { |value| value < 0 }
end

def valid_sudoku(table)
  row_count = get_valid_digit_count
  col_count = get_valid_digit_count

  begin 
    (0...table.length).each do |i|
      row_count = get_valid_digit_count
      col_count = get_valid_digit_count
      (0...table.length).each do |j|
        if table[i][j] =~ /\d/
          row_count[ table[i][j].to_i  ] -= 1
        end

        if table[j][i] =~ /\d/
          col_count[ table [j][i].to_i ] -= 1
        end
      end
      if row_count.values.any? { |value| value < 0 }
        return false
      end
      if col_count.values.any? { |value| value < 0 }

        return false
      end
    end

  
  rescue  NoMethodError # if the table has something not 0-9
    return false
  end

  [[0,0], [0,3], [0,6],
   [3,0], [3,3], [3,6],
   [6,0], [6,3], [6,6]].each do |grid|
    if !check_subgrid(table, grid)
      puts "failing on #{grid}"
      return false
    end
  end

  return true
end