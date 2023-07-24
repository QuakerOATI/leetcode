int minSubArrayLen(int target, int* nums, int numsSize){
    if (numsSize == 0)
        return 0;
    if (numsSize == 1)
    {
        if (nums[0] >= target)
            return 1;
        return 0;
    }
    int sum = 0;
    for (int i=0; i<numsSize; ++i) {
        if (nums[i] >= k)
            return 1;
        sum += nums[i];
        if (sum >= k)
        {
            for (int j=-1; sum >= k; sum -= nums[++j]) {}
            return i - j + 1;
        }
    }
    return 0;
}
