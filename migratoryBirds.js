process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();    
});

function readLine() {
    return input_stdin_array[input_currentline++];
}

/////////////// ignore above this line ////////////////////
function greaterIn(i,j){
    if(i>j){
        return i;
    }else{
        return j;
    }
}

function migratoryBirds(n, ar) {
    var count1=0;
    var count2=0;
    var count3=0;
    var count4=0;
    var count5=0;
    for(var i =0; i<n ; i++){
         if(ar[i] == 1){
             count1++;
         }else if(ar[i] == 2){
             count2++;
         }else if(ar[i] == 3){
            count3++;
        }else if(ar[i] == 4){
            count4++;
        }else if(ar[i] == 5){
            count5++;
        }
    }
   var c = greaterIn(count5,greaterIn(count4,greaterIn(count3,greaterIn(count2,count1))));
   if(c == count1){
    return 1;
  }else if(c == count2){
    return 2;
  }else if(c == count3){
   return 3;
  }else if(c == count4){
   return 4;
  }else if(c == count5){
   return 5;
}  
}

function main() {
    var n = parseInt(readLine());
    ar = readLine().split(' ');
    ar = ar.map(Number);
    var result = migratoryBirds(n, ar);
    process.stdout.write("" + result + "\n");

}
