const readline = require("readline");

var getInput = function(query) {
    var iface = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    return new Promise(resolve => iface.question(query, ans => {
        iface.close();
        resolve(ans);
    }));
};
