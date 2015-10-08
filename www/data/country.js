var locs = require('./locations.json');
var countries = {}
for (var key of Object.keys(locs)) {
  if (locs[key]) {
    var loc = locs[key][0];
    if (loc && loc.address) {
      //console.log(loc.address.country);
      countries[loc.address.country] = true;
    }
  }
}

console.log('location');
for (var country of Object.keys(countries)) {
  console.log('"'+country+'"');
}
