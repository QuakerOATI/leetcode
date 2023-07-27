/**
 * @param {number[]} asteroids
 * @return {number[]}
 */

// Works, but taps out on memory
var asteroidCollision = function(asteroids) {
    var collideLast = function(as, a) {
        while (as.length && a < 0 && as.at(-1) > 0) {
            if (a + as.at(-1) > 0)
                return as;
            a = a + as.pop() && a;
        }
        if (a) as.push(a);
        return as;
    }

    let pos = asteroids.filter(x => x>0);
    if (pos.length === 0 || pos.length === asteroids.length)
        return asteroids;
    let last = asteroids.pop();
    return collideLast(asteroidCollision(asteroids), last);
};

var asteroidCollision = function(asteroids) {
    var collideFirst = (as, a) => {
        if (a < 0 || as[0] > 0) {
            return [a, ...as];
        }
        let stop = as.findIndex(x => x > 0 || -x >= a);
        if (!~stop)
            return [a];
        if (as[stop] > 0) return [a, ...as.slice(stop)];
        return as.slice(a + as[stop] ? stop : stop + 1);
    }
    let [left, right] = [asteroids, []];
    return asteroids.reduceRight(collideFirst, []);
}


