/**
 * @param {string} val
 * @return {Object}
 */
const expect = (val) => {

    return {
        toBe: function(expected) {
            if (val === expected) {
                return true
            }
            throw new Error("Not Equal")
        }
        ,
        notToBe: function(expected) {
            if (val !== expected) {
                return true
            }
            throw new Error("Equal")
        }
    }

};
/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */