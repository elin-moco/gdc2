var countries = require('./events.json');
var arg = process.argv[2];

countries.sort(function(a, b) {
  if ('js' === arg) {
    a.score = a.languages.JavaScript;
    a.score = a.score ? a.score : 0;
    b.score = b.languages.JavaScript;
    b.score = b.score ? b.score : 0;
  } else if ('c' === arg) {
    a.score = (a.languages.C ? a.languages.C : 0) + (a.languages['C++'] ? a.languages['C++'] : 0);
    b.score = (b.languages.C ? b.languages.C : 0) + (b.languages['C++'] ? b.languages['C++'] : 0);
  } else {
    a.score = Object.keys(a.languages).reduce(function(sum, key) {
      return sum + parseInt(a.languages[key]);
    }, 0);
    b.score = Object.keys(b.languages).reduce(function(sum, key) {
      return sum + parseInt(b.languages[key]);
    }, 0);
  }
  return b.score - a.score;
});

countries.forEach(function(country) {
  console.log(country.name + ':\t' + country.score);
});
