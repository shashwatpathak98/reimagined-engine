/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    
    let count = {}

    for(let char of s){
        if(count[char]) count[char]++;
        else count[char] = 1;
    }
 
    let i = 0;
    while(i < s.length){
        if(count[s[i]] === 1) return i;
        i++;
    }
    
    return -1;

};