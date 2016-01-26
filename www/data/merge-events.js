var qualters = [];
qualters.push(require('./events-2014Q4.json'));
qualters.push(require('./events-2015Q1.json'));
qualters.push(require('./events-2015Q2.json'));
qualters.push(require('./events-2015Q3.json'));
qualters.push(require('./events-2015Q4.json'));

var countries = {};

function mergeCountries(qualter) {
  for (var country of qualter) {
    if (!(country.name in countries)) {
      countries[country.name] = country;
    } else {
      var c = countries[country.name];
      for (var lang in country.languages) {
        if (lang in c.languages) {
          c.languages[lang] += country.languages[lang] || 0;
        } else {
          c.languages[lang] = country.languages[lang] || 0;
        }
      }
      for (var repo in country.repositories) {
        if (repo in c.repositories) {
          c.repositories[repo] += country.repositories[repo] || 0;
        } else {
          c.repositories[repo] = country.repositories[repo] || 0;
        }
      }
      for (var user of country.users) {
        if (c.users.indexOf(user) == -1) {
          c.users.push(user);
        }
      }
    }
  }
}

for (var qualter of qualters) {
  mergeCountries(qualter);
}

var output = [];
for (var key in countries) {
  output.push(countries[key]);
}

console.log(JSON.stringify(output, null, 2));
