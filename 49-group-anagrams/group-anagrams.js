/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    map = {}
    for (let str of strs) {
        let sortedStr = [...str].sort().join('')
        if (map[sortedStr]) map[sortedStr].push(str)
        else map[sortedStr] = [str]
    }
    let ans = Object.values(map)
    return ans
}