/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function(s) {
    var words = s.split(" ");
    words.sort(function (a, b) {
    if (a.substr(a.length - 1) > b.substr(b.length - 1))
      return 1;
    if (a.substr(a.length - 1) < b.substr(b.length - 1))
      return -1;
    return 0;
    });
    return words.join(" ").replace(/[0-9]/g, '')
};
