var numberOfMatches = function(n) {

    var count_match = 0;
    var match = 0;
    while (n > 1) {
           if(n % 2 == 0) {
             count_match += n/2
             match = n/2
           } else {
             count_match += ~~(n/2)
             match = ~~(n/2)+1
           }
      n = match;
    }
    return count_match
};