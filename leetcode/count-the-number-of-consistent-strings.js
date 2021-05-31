/**
 * @param {string} allowed
 * @param {string[]} words
 * @return {number}
 */
var countConsistentStrings = function(allowed, words) {
        function makeUnique(str) {
            return String.prototype.concat(...new Set(str))
        }
        var number = 0;

        words.forEach(function(entry) {
            let unique_list = makeUnique(entry).split('').sort().join('');
            let unique_list_length = unique_list.length -1 ;
            //console.log(unique_list_length)
            for (var i = 0; i < unique_list.length; i++) {

                if (allowed.includes(unique_list[i]) == false) 
                {       
                        break; 
                }
                if (unique_list_length == i) {                    
                    number = number + 1 
                }

            } 
           
            });
        return number;
};
