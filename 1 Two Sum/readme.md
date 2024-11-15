# Intuition
1. We can use a HashMap to store the elements of the array along with their indices.
2. While iterating through the array, for each element nums[i], we calculate the difference (target - nums[i]).
3. If the difference exists in our dictionary and its index is not the same as i, we found the solution.

# Approach
1. Create a HashMap to store the elements of the array along with their indices.
2. Iterate through the array and store each element along with its index in the HashMap.
3. Iterate through the array again, and for each element nums[i], calculate the difference (target - nums[i]).
4. If the difference exists in the HashMap and its index is not the same as i, return the indices.

# Complexity
## Time complexity: O(n)
- The first loop to store elements in the HashMap takes O(n) time.
- The second loop to find the solution also takes O(n) time.
- Thus, the overall time complexity is O(n + n) = O(n).

## Space complexity: O(n)
- due to the HashMap, which can store up to n elements.
