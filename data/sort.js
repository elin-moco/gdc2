function sortCountriesByContributionType(type, countries) {
  return countries.sort(function(a, b) {
    if (type) {
      var isRepo = type.indexOf('/') > 0;
      if (isRepo) {
        a.contributions = a.repositories[type] || 0;
        b.contributions = b.repositories[type] || 0;
      } else if (type == 'sys') {
        a.contributions = (a.languages.C || 0) + (a.languages['C++'] || 0);
        b.contributions = (b.languages.C || 0) + (b.languages['C++'] || 0);
      } else if (type == 'All') {
        a.contributions = Object.keys(a.languages).reduce(function(sum, key) {
          return sum + parseInt(a.languages[key]);
        }, 0);
        b.contributions = Object.keys(b.languages).reduce(function(sum, key) {
          return sum + parseInt(b.languages[key]);
        }, 0);
      } else {
        a.contributions = a.languages[type] || 0;
        b.contributions = b.languages[type] || 0;
      }
    }
    return b.contributions - a.contributions;
  });
}

if (typeof process !== 'undefined') {
  var countries = require('./events.json');
  var arg = process.argv[2];
  sortCountriesByContributionType(arg, countries)
  countries.forEach(function(country) {
    console.log(country.name + ':\t' + country.contributions);
  });
}
