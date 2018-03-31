const fetch = require('/Users/jmartin/.nvm/versions/node/v8.9.3/lib/node_modules/node-fetch')

const GITHUB_ENDPOINT = "https://api.github.com";
const getRandomInt = max => Math.floor(Math.random() * Math.floor(max));

function printResults(user1, user2, randomRepo) {
  console.log(`Picked first random Github user: ${user1.login} | Repo Count: ${user1.repo_count}`);
  console.log(`Picked random repo: ${randomRepo.full_name}, which has ${randomRepo.watchers} watchers`);
  console.log(`Picked second random person watching this repo: ${user2.login} | Repo Count:${user2.repo_count}`);
}

function getTwoRandomGithubUsers() {
  let user1, user2, randomRepo;

  fetch(`${GITHUB_ENDPOINT}/users`)
    // Pick a random user
    .then(response => response.json())
    .then(users => {
      user1 = users[getRandomInt(users.length)];
      return fetch(user1.repos_url);
    })

    // Get total list of first user's repos
    .then(response => response.json())
    .then(user1Repos => {
      randomRepo = user1Repos[getRandomInt(user1Repos.length)];
      user1.repo_count = user1Repos.length;

      if (!randomRepo || !randomRepo.watchers) throw new Error(`${randomRepo.full_name} has no watchers =(`)
      return fetch(randomRepo.subscribers_url);
    })

    // Pick a random subscriber
    .then(response => response.json())
    .then(randomRepoSubscribers => {
      if (randomRepoSubscribers.length < 1) throw new Error(`${randomRepo.full_name} has less than one subscribers =( Aborting`);
      user2 = randomRepoSubscribers[getRandomInt(randomRepoSubscribers.length)];

      return fetch(user2.repos_url);
    })

    // Get total list of second user's repos
    .then(response => response.json())
    .then(user2Repos => {
      user2.repo_count = user2Repos.length;
      return Promise.resolve();
    })

    // Process results
    .then(() => printResults(user1, user2, randomRepo))

    // Catch all errors (catches errors anywhere along the chain)
    .catch(error => console.warn("Encountered an error:", error));
}

getTwoRandomGithubUsers();
