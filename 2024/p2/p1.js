const { readFile } = require("../read");

const rawData = readFile("./p2/input.txt");

const d = rawData
  .split("\n")
  .map((l) => l.split(/\s+/).map((v) => parseInt(v)));

let ans = 0;

for (let i = 0; i < d.length; ++i) {
  if (d[i].length <= 1) {
    ans++;
    continue;
  }
  const o = d[i][0] < d[i][1]; // true = ascending
  let take = true;
  for (let j = 1; j < d[i].length; ++j) {
    const diff = Math.abs(d[i][j] - d[i][j - 1]);
    if (
      (o && d[i][j] <= d[i][j - 1]) ||
      (!o && d[i][j] >= d[i][j - 1]) ||
      diff > 3 ||
      diff < 1
    ) {
      take = false;
      break;
    }
  }
  if (take) {
    ans++;
  }
}

console.log(ans);
