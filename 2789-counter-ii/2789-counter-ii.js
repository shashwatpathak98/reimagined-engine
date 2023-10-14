/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {

    let retain = init;
    let counter = {

      increment  :  () => ++init ,
      decrement :   () => --init,
      reset : () => {
          init = retain
          return init 
       }
       
    }

    return counter;

};


// const counter = createCounter(5)
// counter.increment(); // 6
// counter.reset(); // 5
// counter.decrement(); // 4
