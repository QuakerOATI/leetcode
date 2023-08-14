/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function (fn) {
  // 71.51 %ile runtime
  // 20.62 %ile memory
  var groups = {};
  for (elem of this) {
    let key = fn(elem);
    if (!groups.hasOwnProperty(key)) {
      groups[key] = [];
    }
    groups[key].push(elem);
  }
  return groups;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
