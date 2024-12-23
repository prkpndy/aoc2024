const { readFile } = require("../read");

const rawData = readFile("./p2/input.txt");

const data = rawData
  .split("\n")
  .map((l) => l.split(/\s+/).map((v) => parseInt(v)));

let ans = 0;

function checkList(d) {
  if (d.length <= 1) {
    return true;
  }
  const o = d[0] < d[1]; // true = ascending
  for (let j = 1; j < d.length; ++j) {
    const diff = Math.abs(d[j] - d[j - 1]);
    if (
      (o && d[j] <= d[j - 1]) ||
      (!o && d[j] >= d[j - 1]) ||
      diff > 3 ||
      diff < 1
    ) {
      return false;
    }
  }
  return true;
}

for (let i = 0; i < data.length; ++i) {
  if (data[i].length <= 1) {
    ans++;
    continue;
  }
  const d = data[i];
  let ac = 0,
    dc = 0,
    m = 0,
    lai = -1,
    ldi = -1,
    di = -1;
  let take = true;
  for (let j = 1; j < d.length; ++j) {
    if (d[j] - d[j - i] === 0) {
      if (m === 1) {
        take = false;
        break;
      }
      m = 1;
    }
    if (d[j] < d[j - 1]) {
      ac++;
      lai = j;
    } else {
      dc++;
      ldi = j;
    }
  }
  if (Math.min(ac, dc) > 1) {
    take = false;
  } else {
    if (ac === 0 || dc === 9) {
      // descending series
    } else if (ac === 1) {
      const nd = [];
      d.forEach((v, ind) => {
        if (ind !== lai) nd.push(v);
      });
      take = checkList(nd);
    } else if (dc === 1) {
      const nd = [];
      d.forEach((v, ind) => {
        if (ind !== ldi) nd.push(v);
      });
      take = checkList(nd);
    } else {
      take = false;
    }
  }

  if (take) {
    ans++;
  }
}

console.log(ans);
