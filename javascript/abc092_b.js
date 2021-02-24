//入力元を切り替えるのを忘れないこと！！
//コンテスト用
//const inputs = require('fs').readFileSync('/dev/stdin', 'utf8').trim().split('\n');
 
//Windows用
const inputs = require('fs').readFileSync('./input.txt', 'utf8').trim().split('\n');

// 1～A日で1個、A+1～2A日で2個チョコを消費と考えると、
// 全体の日数 / A を切り上げたものが、各人が消費するチョコの数となる

function main(inputs) {
    const N = parseInt(inputs[0]);
    const [D, X] = inputs[1].split(" ").map(x=>parseInt(x));
    const A = [];
    let result = 0;
    for (let i = 2; i < N+2; i++) {
        result += Math.ceil(D / parseInt(inputs[i]));
    }
    console.log(X + result);
}

main(inputs);