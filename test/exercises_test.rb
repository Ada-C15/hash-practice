require_relative "test_helper"

describe "exercises" do
  describe "grouped_anagrams" do
    it "will return [] for an empty array" do
      #Arrange
      list = []
      
      # Act-Assert
      expect(grouped_anagrams(list)).must_equal []
    end

    it "will work for the README example" do
      # Arrange
      list = ["eat", "tea", "tan", "ate", "nat", "bat"]

      # Act
      answer = grouped_anagrams(list)

      expected_answer = [
        ["ate","eat","tea"],
        ["nat","tan"],
        ["bat"]
      ]

      # Assert
      answer.each_with_index do |array, index|
        expect(expected_answer).must_include array.sort
      end
    end

    it "will work for strings with no anagrams" do
      # Arrange
      list = ["eat", "ear", "tar", "pop", "pan", "pap"]

      # Act
      answer = grouped_anagrams(list)

      expected_answer = [
        ["eat"],
        ["ear"],
        ["tar"],
        ["pop"],
        ["pan"],
        ["pap"]
      ]

      # Assert
      answer.each_with_index do |array, index|
        expect(expected_answer).must_include array.sort
      end
    end

    it "will work for strings that are all anagrams" do
      # Arrange
      list = ["eat", "tae", "tea", "eta", "aet", "ate"]

      # Act
      answer = grouped_anagrams(list)

      expected_answer = [
        [ "aet", "ate", "eat", "eta", "tae", "tea"]
      ]
      # Assert
      answer.each_with_index do |array, index|
        expect(expected_answer).must_include array.sort
      end
    end
  end

  describe "top_k_frequent_elements" do
    it "works with example 1" do
      # Arrange
      list = [1,1,1,2,2,3]
      k = 2

      # Act
      answer = top_k_frequent_elements(list, k)

      # Assert
      expect(answer.sort).must_equal [1,2]
    end

    it "works with example 2" do
      # Arrange
      list = [1]
      k = 1

      # Act
      answer = top_k_frequent_elements(list, k)

      # Assert
      expect(answer.sort).must_equal [1]
    end

    it "will return [] for an empty array" do
      # Arrange
      list = []
      k = 1

      # Act
      answer = top_k_frequent_elements(list, k)

      # Assert
      expect(answer.sort).must_equal []
    end

    it "will work for an array with k elements all unique" do
      # Arrange
      list = [1, 2, 3]
      k = 3

      # Act
      answer = top_k_frequent_elements(list, k)

      # Assert
      expect(answer.sort).must_equal [1, 2, 3]
    end

    it "will work for an array when k is 1 and several elements appear 1 time (HINT Pick the 1st one)" do
      # Arrange
      list = [1, 2, 3]
      k = 1

      # Act
      answer = top_k_frequent_elements(list, k)

      # Assert
      expect(answer.sort).must_equal [1]
    end

  end

  xdescribe "valid sudoku" do
    it "works for the table given in the README" do
      # Arrange
      table = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
      ]

      # Act
      valid = valid_sudoku(table)

      # Assert
      expect(valid).must_equal true
    end

    it "fails for the table given in the README" do
      # Arrange
      table = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
      ]

      # Act
      valid = valid_sudoku(table)

      # Assert
      expect(valid).must_equal false
    end

    it "fails for a duplicate number in a sub-box" do
      # Arrange
      table = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".","3","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
      ]

      # Act
      valid = valid_sudoku(table)

      # Assert
      expect(valid).must_equal false
    end

    it "fails for a duplicate number in a bottom right sub-box" do
      # Arrange
      table = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".","2","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9","8",".","5"],
        [".",".",".",".","8",".",".","7","9"]
      ]

      # Act
      valid = valid_sudoku(table)

      # Assert
      expect(valid).must_equal false
    end
  end
end