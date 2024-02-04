/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var maxSumAfterPartitioning = function(arr, k) {

  let N = arr.length;
  let dp = new Array( N + 1).fill(0)

  var maxSum = (start) => {
       
        if(start >= N){
            return 0;
        }

        if(dp[start] !== 0){
            return dp[start];
        }

        let currElem = 0;
        let currMax = 0;

        for(let i = start ; i < Math.min(N , start + k); i++){
            
             currElem = Math.max(currElem , arr[i]);
             currMax = Math.max(currMax , currElem * (i - start + 1) + maxSum(i + 1));
        }

        dp[start] = currMax;
        return dp[start];
  }

  return maxSum(0);
};