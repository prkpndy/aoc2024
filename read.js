const fs = require("fs");

function readFile(path) {
  try {
    const data = fs.readFileSync(path, "utf8");
    return data;
  } catch (error) {
    console.error(error);
  }
}

module.exports = { readFile };
