/**
 * @param {number} low
 * @param {number} high
 * @return {number[]}
 */
var sequentialDigits = function(low, high) {
    let n = 10
    const string = "123456789"
    let ans = []
    
    for(let len = low.toString().length ; len < (high.toString().length)+1 ; len++){
        for(let start = 0 ; start < n - len ; start++){
                let number = Number(string.substring(start , start + len))
               if(number >=low && number <=high) ans.push(number)

        }
    } 
    


    return ans;
};