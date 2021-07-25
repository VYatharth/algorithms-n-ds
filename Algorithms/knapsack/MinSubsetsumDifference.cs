//https://leetcode.com/problems/last-stone-weight-ii/
public class Solution {
    public int LastStoneWeightII(int[] stones) {
        var sum = stones.Sum();
        
        int[,] dp = new int [stones.Length + 1,sum/2 + 1];
        
        for(var i= 0;i<sum/2 + 1; i++){
            dp[0,i] = sum;
        }
        
        //Console.WriteLine(sum);
        int minDiff = sum;
        int tempSum;
        for(var i= 1; i < stones.Length + 1; i++){
            for(var j= 0; j < sum/2 + 1; j++){
                tempSum = j + stones[i-1];
                if(2*tempSum <= sum){
                    //Console.WriteLine(i);
                    dp[i,j] = Math.Min(dp[i-1,j], dp[i-1,tempSum] - (2*stones[i-1]));
                }
                else{
                    dp[i,j] = dp[i-1,j];
                }
                
                minDiff = Math.Min(minDiff, dp[i,j]);
                
            }
        }
        
        return minDiff;
    }
}
