var repoLists = [];
repoLists.push(require('./repos-2014Q4.json'));
repoLists.push(require('./repos-2015Q1.json'));
repoLists.push(require('./repos-2015Q2.json'));
repoLists.push(require('./repos-2015Q3.json'));
repoLists.push(require('./repos-2015Q4.json'));

function intersection(a, b)
{
  return a.filter(function(n) {
    return b.indexOf(n) != -1
  });
}

var output = repoLists.reduce(function(prev, curr) {
  return intersection(prev, curr);
});

console.log(JSON.stringify(output, null, 2));
