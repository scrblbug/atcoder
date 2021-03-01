// 日立製作所 社会システム事業部 プログラミングコンテスト2020 B - Nice Shopping
// https://atcoder.jp/contests/hitachi2020/tasks/hitachi2020_b
// tag: 基礎問題 計算量

// 冷蔵庫・電子レンジともに10^5個あるので、全探索では
// 時間が足りなくなる。
// 割引がない場合は、それぞれの一番安いものを買えばいい。
// また、割引が無い組み合わせは見る必要が無い
// ＝割引券の組み合わせだけ値段を確認する

const inputs = require('fs').readFileSync('/dev/stdin', 'utf8').trim().split('\n');

function main(inputs) {
    const [A, B, M] = inputs[0].split(' ').map(x=>parseInt(x));
    const friges = inputs[1].split(' ').map(x=>parseInt(x));
    const microws = inputs[2].split(' ').map(x=>parseInt(x));
    const vouchers = [];
    for (let i = 0; i < M; i++) {
        vouchers.push(inputs[i+3].split(' ').map(x=>parseInt(x)));
    }

    // 割引券を使わない場合、それぞれ一番安いものを買う
    let result = friges.reduce((x, y)=>Math.min(x, y)) + microws.reduce((x, y)=>Math.min(x, y));

    // 割引券を使う場合のみを探索する
    for (let i = 0; i < vouchers.length; i++) {
        const [frige, micro, discount] = vouchers[i];
        let tmp_r = friges[frige-1] + microws[micro-1] - discount;
        if (tmp_r < result) {
            result = tmp_r;
        }
    }
    console.log(result);
}

main(inputs);