/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if (x<0){
        return  false
    }
    let n=x ;
    let a=0;
    while (x!=0){
        let m=x%10;
        a = a*10 + m;
        x= Math.floor(x/10);
    }
    
    return a==n?true:false;
};