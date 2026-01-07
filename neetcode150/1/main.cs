namespace neetcode150;

public class Neetcode1
{
    public int[] TwoSum(int[] nums, int target)
    {
        var dictionnary = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++)
        {
            int newTarget = target - nums[i];
            if (dictionnary.TryGetValue(newTarget, out int pos))
            {
                return [i, pos];
            }
            else
            {
                dictionnary.Add(nums[i], i);
            }
        }
        return [];
    }
}
